from fastapi import FastAPI, Response
from pydantic import BaseModel


app = FastAPI()


class Body(BaseModel):
    text: str


@app.get('/')
def root():
    return Response("<h1>A self-documenting API that uses the FastAPI framework</h1>")


@app.post('/generate')
def predict(body: Body):
    return {"text": body.text}
