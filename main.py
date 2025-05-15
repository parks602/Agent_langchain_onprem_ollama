import requests
from dotenv import load_dotenv
from llm.generator import run_generator

if __name__ == "__main__":

    load_dotenv()

    data = {
        "question_name": "제니가 사라졌어요",
        "question": "3월 15일에 접속했더니 제니가 500만 정도 사라졌습니다. 확인 부탁드립니다.",
        "account_id": "user001",
    }
    result = run_generator(data)
