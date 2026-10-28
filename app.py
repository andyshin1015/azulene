import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-6.1-sol")

app = FastAPI(title="azulene")
client = OpenAI()  # reads OPENAI_API_KEY from the environment


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[Message]


class ChatResponse(BaseModel):
    reply: str


@app.get("/health")
def health():
    return {"ok": True, "model": MODEL}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[m.model_dump() for m in req.messages],
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    return ChatResponse(reply=completion.choices[0].message.content or "")
