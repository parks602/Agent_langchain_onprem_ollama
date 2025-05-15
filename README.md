# Agent_langchain_onprem_ollama

**onprem\_AI\_agent**는 게임 고객의 다양한 문의를 자동으로 분석하고, 적절한 함수를 호출하여 신속하고 정확한 응답을 제공하는 온프레미스 AI 에이전트입니다.
이 프로젝트는 LangChain, Ollama, LangSmith와 같은 최신 LLM 오케스트레이션 도구를 활용하여, 로컬 환경에서 빠르고 안정적인 고객 지원 시스템을 구현하는 것을 목표로 합니다.

***

## 프로젝트 개요

* **목표**: 게임 고객의 다양한 문의 사항을 자동으로 분석하고, 적절한 함수를 호출하여 신속하고 정확한 응답을 제공하는 AI 에이전트를 개발합니다.
* **특징**:
    * LangChain 기반의 에이전트 설계 및 도구 체계 구성
    * Ollama를 통한 로컬 LLM 실행
    * LangSmith를 활용한 추론 추적 및 디버깅
    * Unsloth의 Dynamic 4-bit 양자화된 Phi-4-mini-instruct 모델 사용
    * 모델 기능이 포함된 Modelfile을 통해 Ollama에서 컴파일 및 실행

***

## 기능 및 구성

이 프로젝트는 고객 문의를 처리하기 위해 다양한 도구(툴)를 정의하고, LangChain의 에이전트 체계를 활용하여 적절한 도구를 선택하고 실행합니다.

### 도구 구성

* <strong>결제 관련 도구 (PAYMENT\_TOOLS)</strong>:
    * `user_payment_history`: 유저의 전체 결제 내역 조회
    * `user_payment_history_by_date`: 지정된 날짜 범위 내 결제 내역 조회
    * `user_refund_history`: 유저의 환불 내역 조회
* <strong>계정 관련 도구 (ACCOUNT\_TOOLS)</strong>:
    * `get_account_info`: 계정의 캐릭터 목록 및 최근 접속 기록 조회
    * `get_character_info`: 캐릭터 정보 조회
    * `get_character_item_usage`: 캐릭터의 아이템 사용 내역 조회

각 도구는 LangChain의 `Tool` 클래스를 사용하여 정의되며, 에이전트는 고객의 문의에 따라 적절한 도구를 선택하여 실행합니다.

***

## LLM 및 Ollama 구성

이 프로젝트는 로컬 환경에서 LLM을 실행하기 위해 Ollama를 사용합니다.

### 사용 모델

* **모델**: [unsloth/Phi-4-mini-instruct-GGUF](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF)
* **양자화 방식**: Dynamic 4-bit 양자화 (Unsloth의 Dynamic 2.0 Quants)
* **특징**:
    * 일반적인 4-bit 양자화보다 높은 정확도
    * 메모리 사용량은 BnB 4-bit 대비 10% 미만 증가
    * 로컬 환경에서 효율적인 추론 가능

### Modelfile 구성

Ollama는 모델의 설정을 정의하는 `Modelfile`을 사용하여 모델을 컴파일하고 실행합니다.
이 프로젝트에서는 `Modelfile`을 통해 에이전트의 기능을 정의하고, 이를 Ollama에서 컴파일하여 사용합니다.

***

## LangChain 및 LangSmith 통합

LangChain은 LLM 에이전트의 구성과 도구 체계를 관리하는 데 사용되며, LangSmith는 추론 과정의 추적 및 디버깅을 지원합니다.

* **LangChain**:
    * 에이전트 구성 및 도구 체계 정의
    * 고객 문의에 따른 적절한 도구 선택 및 실행
* **LangSmith**:
    * 추론 과정의 추적 및 디버깅
    * 에이전트의 성능 모니터링 및 평가

이러한 통합을 통해 에이전트의 동작을 실시간으로 모니터링하고, 문제 발생 시 신속하게 디버깅할 수 있습니다.

***

## 성능

이 프로젝트는 고객 문의를 처리하는 데 있어 높은 성능을 제공합니다.

* **처리 시간**: 데이터베이스 조회를 제외한 전체 처리 시간은 평균 10초 이내
* **효율성**: 로컬 환경에서 실행되므로 외부 API 호출에 따른 지연이 없음

이를 통해 빠르고 안정적인 고객 지원이 가능합니다.

***

## 실행 방법

1. Ollama 설치 및 설정
2. `Modelfile`을 사용하여 모델 컴파일
3. LangChain 및 LangSmith 설정
4. `main.py` 실행

자세한 실행 방법은 [GitHub 리포지토리](https://github.com/parks602/Agent_langchain_onprem_ollama)를 참고하시기 바랍니다.

***

## 프로젝트 구조

```
├── db/              # 데이터베이스 관련 모듈
├── llm/             # LLM 및 Ollama 관련 설정
├── main.py          # 메인 실행 파일
├── Modelfile        # Ollama 모델 설정 파일
└── README.md        # 프로젝트 설명 파일
```

***

## 참고 자료

* [unsloth/Phi-4-mini-instruct-GGUF](https://huggingface.co/unsloth/Phi-4-mini-instruct-GGUF)
* LangChain 공식 문서
* Ollama 공식 문서
* LangSmith 공식 문서
