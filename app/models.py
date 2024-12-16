from typing import Optional, List, Union
from pydantic import BaseModel

class Question(BaseModel):
    type: str
    prompt: str
    options: Optional[List[str]] = None

class Form(BaseModel):
    title: str
    questions: List[Question]

class Answer(BaseModel):
    question: str
    response: Union[str, List[str]]

class Response(BaseModel):
    form_id: str
    answers: List[Answer]
    
def serialize_id(id):
    return str(id)