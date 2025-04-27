from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import torch

# from chating import Chating_text, Chatbot_operation
from llama import Chating_text, Chatbot_operation

app = FastAPI()

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

chatbot = Chatbot_operation()

@app.post("/")
async def root():
    return {"message": "chatbot ok"}

@app.post("/chatbot")
async def generate_text(question: Chating_text):
    result = chatbot.chatbot_operation(question.text)
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)