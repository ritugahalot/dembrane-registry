# Portal Registry

The registry service for the portal, containing data information.

## Setup

Clone the repository and enter the root of the repo.

Initialize the repo by typing the following in your terminal:

```
$ poetry install
```

## Run APIs on local

change to directory app
```
$ uvicorn main:app --reload
```

run application http://localhost:8000/docs

### Adding and committing:
Add files to commit with: 
```
$ git add [FILENAME]
```

Commit your files with:
```
$ git commit -m [your commit message here]
```

Push your changes to the repository with:
```
$ git push
```

#### How to trigger pytest

```
pytest app/tests/
```

