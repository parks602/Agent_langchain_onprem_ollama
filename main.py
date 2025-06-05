import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:8001/generate"

    data = {
        "question_name": "제니가 사라졌어요",
        "question": "3월 15일에 접속했더니 제니가 500만 정도 사라졌습니다. 확인 부탁드립니다.",
        "account_id": "user001",
    }
    response = requests.post(url, json=data)

    print("Status:", response.status_code)
    print("Response:", response.json())
