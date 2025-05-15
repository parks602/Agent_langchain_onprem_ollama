import re
import json


def parse_json_output(response_text: str):
    match = re.search(r"```json\s*(\[\s*{.*?}\s*])\s*```", response_text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError as e:
            return {"error": "JSON 파싱 실패", "message": str(e)}
    else:
        return {"error": "응답에 JSON 블록이 없음", "raw_output": response_text}

def parse_function_json(response: str):
    match = re.search(r"```json\s*(\{.*?\})\s*```", response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError as e:
            return {"error": "JSON 파싱 실패", "message": str(e)}
    else:
        return {"error": "응답에 JSON 블록이 없음", "raw_output": response}
        
def summary_prompt(data, open_result):
    """
    모든 주제와 함수 실행 결과를 포함한 최종 요약 프롬프트 생성
    """
    prompt = f"사용자 ID: {data['account_id']}\n"
    prompt += f"문의 제목: {data['question_name']}\n"
    prompt += f"문의 내용: {data['question']}\n\n"
    prompt += "분석된 문의 주제와 함수 결과:\n"

    for job in open_result:
        prompt += f"\n[주제: {job['subject']}]\n"
        prompt += f"작업 수행 결과: {job['function_result']}\n"
    return prompt


def get_tool_list_escaped(tools):
    raw = json.dumps(tools, indent=2, ensure_ascii=False)
    escaped = raw.replace("{", "{{").replace("}", "}}")
    return escaped