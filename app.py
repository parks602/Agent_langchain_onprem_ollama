from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from typing import Dict, Any
from llm.generator import run_generator
app = FastAPI()
load_dotenv()
# 입력 데이터 모델 정의
class QuestionRequest(BaseModel):
    question_name: str
    question: str
    account_id: str

# POST 엔드포인트
@app.post("/generate")
def generate_response(request: QuestionRequest):
    data = request.dict()
    result = run_generator(data)
    return result
