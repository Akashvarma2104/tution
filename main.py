from fastapi import FastAPI
from pydantic import BaseModel
import openai
import textwrap
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

API_KEY = "sk-8Evdci1AFkmBDMpIUPJbbQ"
BASE_URL = "https://chatapi.akash.network/api/v1"
MODEL = "Meta-Llama-3-1-8B-Instruct-FP8"
PROMPT = (
    "You are a professional Blockchain Consultant with expertise in blockchain technology, cryptocurrencies, smart contracts, and decentralized applications (DApps). "
    "Your role is to provide insightful advice on blockchain implementation, its potential use cases, and best practices for integrating blockchain solutions. "
    "You explain complex blockchain concepts in simple terms, offer technical and strategic insights, and ensure users understand the risks and benefits of blockchain technology. "
    "Your tone is professional, approachable, and tailored to the user's level of knowledge and objectives. "
    "You should limit your response to only essential information. "
    "Your response should be short, crisp, and concise."
)

openai.api_key = API_KEY
openai.api_base = BASE_URL

class UserMessage(BaseModel):
    user_message: str

@app.post("/blockchain-advice/")
async def blockchain_consultant(user_message: UserMessage):
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": PROMPT},
                {"role": "user", "content": user_message.user_message}
            ]
        )
        assistant_message = response["choices"][0]["message"]["content"]
        return {"response": assistant_message.strip()}

    except openai.error.OpenAIError as e:
        return {"error": str(e)}

