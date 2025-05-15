from .functions_tools import get_category_tools
from .tools import function_registry
from langsmith import traceable

def get_item_usage_count(user_id, user_type, item_name, start_date, end_date):
    return f"[TEST] {user_id}({user_type}) 유저가 {start_date}~{end_date} 동안 {item_name} 사용 횟수는 42회입니다."


def get_account_info(account_id: str) -> str:
    # 여기에 MSSQL 쿼리 실행하는 로직을 연결
    return f"{account_id} 계정의 캐릭터 목록과 최근 접속 기록입니다."

@traceable
def run_tool_response(tool_call):
    """
    사용자가 선택한 함수 목록을 실행하고 결과를 반환합니다.
    """
    result = function_registry[tool_call["name"]](
        **tool_call["parameters"]
    )
    return result