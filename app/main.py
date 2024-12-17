from fastapi import FastAPI, HTTPException
from bson.objectid import ObjectId
from app.database import db
from fastapi.middleware.cors import CORSMiddleware

from app.models import Form, Response, serialize_id

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.post("/api/forms")
async def create_form(form: Form):
    print(form.model_dump())
    result = db.forms.insert_one(form.model_dump())
    return {"formId": serialize_id(result.inserted_id)}

@app.get("/api/forms/{form_id}")
async def get_form(form_id: str):
    form = db.forms.find_one({"_id": ObjectId(form_id)})
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")
    form["_id"] = serialize_id(form["_id"])
    return form

@app.post("/api/responses")
async def submit_response(response: Response):
    form = db["forms"].find_one({"_id": ObjectId(response.form_id)})
    if not form:
        raise HTTPException(status_code=404, detail="Form not found")

    response_data = response.model_dump()
    db.responses.insert_one(response_data)
    return {"message": "Responses submitted successfully"}

@app.get("/api/responses/{form_id}")
async def get_responses(form_id: str):
    responses = db["responses"].find({"form_id": form_id})
    r_response = []
    for response in responses:
        response["_id"] = serialize_id(response["_id"])
        r_response.append(response["answers"])
    return r_response
