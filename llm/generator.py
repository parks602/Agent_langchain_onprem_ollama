from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from .prompts import OPENNING_SYSTEM_PROMPOT, FINAL_PROMPT, FUNCTION_SELECT_PROMPT
from .functions import parse_json_output, parse_function_json, summary_prompt, get_tool_list_escaped
from .functions_tools import get_category_tools
from .tool_runner import run_tool_response
import json

def model_load():
    llm = OllamaLLM(base_url="http://localhost:11434", model="phi4", temperature=0.0)
    return llm


def openning_prompt(data):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                OPENNING_SYSTEM_PROMPOT.format(
                    account_id=data["account_id"], question_name=data["question_name"]
                ),
            ),
            ("human", "{question}"),
        ]
    )
    return prompt


def function_select_prompt(data, subject_name, subject_description, tool_list):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                FUNCTION_SELECT_PROMPT.format(
                    account_id=data["account_id"],
                    question_name=data["question_name"],
                    subject_name=subject_name,
                    subject_description=subject_description,
                    tool_list = get_tool_list_escaped(tool_list)
                ),
            ),
            ("human", "{question}"),
        ]
    )
    return prompt


def final_prompt_make(info):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                FINAL_PROMPT.format(
                    info=info,
                ),
            ),
            ("human", "{question}"),
        ]
    )
    return prompt

def open_chain_run(llm, data):
    open_prompt = openning_prompt(data)
    open_chain = open_prompt | llm | StrOutputParser() | RunnableLambda(parse_json_output)
    open_result = open_chain.invoke({"question": data["question"]})
    
    return(open_result)

def function_chain_run(llm, data, job):
    tool_list = get_category_tools(job['subject'])
    function_prompt = function_select_prompt(data, job['subject'], job['parse'], tool_list)
    function_chain = function_prompt | llm | StrOutputParser() | RunnableLambda(parse_function_json)
    function_result = function_chain.invoke({"question": data["question"]})
    return(function_result)


def final_chain_run(llm, info_prompt):
    final_prompt = final_prompt_make(info_prompt)
    final_chain = final_prompt | llm | StrOutputParser()
    final_result = final_chain.invoke({"question": ""})
    return(final_result)

def run_generator(data):
    # LLM 모델 로드
    llm = model_load()
    
    open_result = open_chain_run(llm, data)
    if len(open_result) > 0:
        for job in open_result:
            tool_call = function_chain_run(llm, data, job)

            function_result = run_tool_response(tool_call)
            job['function_result'] =function_result
    
    info_prompt = summary_prompt(data, open_result)
    final_result = final_chain_run(llm, info_prompt)
    
    print(final_result)
    return function_result
