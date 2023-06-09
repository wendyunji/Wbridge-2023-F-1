# **Wbridge-2023-F-1 : Chat VQA:텍스트 및 이미지의 멀티모달분석을 이용한 대화형 인공지능 서비스**
(Supporting Grants Wbridge, 여성 공학 인재 육성 프로그램 / Dongguk University)

## **Summary**
다중 소스 데이터를 사용하는 VQA(Visual Question Answering) 기반의 새로운 대화형 인공지능 시스템을 제안한다. 답변이 제공하는 정보의 완전성을 증가시키고 더 나은 사용자 경험을 제공하고자 텍스트와 이미지로부터 질문 유형 추출 및 설명을 생성하는 멀티 모달 분석 기법을 개발한다. 우선, 다중 소스 분석 속도 향상을 위해 텍스트 및 이미지에 숨겨진 개별 특징을 추출하고 사전에 정의한 질문 유형들 중 하나로 분류한다. 이후 자연어 형태의 설명 문장을 생성하고 정답을 추론한다. 또한 효용성 평가 실험과 최신 VQA 기술과의 비교 분석을 진행한다. 본 방법은 질문 유형 분류 자동화와 설명 생성을 통해 질문의 모호성을 해결할 수 있을 것이라 기대된다. 최종적으로 개선된 질의 응답 시스템을 웹 애플리케이션으로 서비스한다.


## **Dates**
2023년 4월 1일 ~ 2023년 10월 31일


## **개발 목표**
1) 질문 유형 추출 모델을 도입한 새로운 VQA 프레임워크 개발
2) 개발한 VQA 프레임워크를 적용한 대화형 인공지능 이미지 활용 검색 시스템 Chat VQA 개발
3) Chat VQA 웹 프로그램 구현 및 오픈소스로 제안
![image](https://github.com/wendyunji/Wbridge-2023-F-1/assets/127592057/86b76260-bd13-4560-abc8-bb7ca5a1dd53)


## **Details**
### **가. VQA 모델 성능 향상 및 기술 개선 및 대화형 인공지능(Chat Bot) 개발**
#### 가-1. VQA task 문헌연구
- VQA task 관련 모델과 데이터셋을 연구한 문헌들을 수집, 연구해 모델 개발에 활용
#### 가-2. 질문 유형 분류 시스템 개발 및 고도화
* 데이터 셋 전처리 : 오타, 불용어, 특수 문자 삭제(pre-trained 프로그램 이용) 젠더 편향성 확인 등 데이터 정리 / 단어 임베딩, 이미지 임베딩, 데이터 분할 등 전처리 작업
* Pre-trained 모델 학습 및 전이학습 : 여러 학습 모델 비교를 통한 최적 모델 선정
- 성별, 나이, 인종 등과 같은 인적 특성과 관련된 질문을 인식하여 중립적인 답변을 제공하도록 학습, 특정 성별에 대한 편견이 들어간 질문은 자동으로 필터링하여 처리할 수 있도록 함
- attention-based model, tree-based methods와 딥러닝 다중 분류 모델 비교 / 모델의 초기 계층을 동결 및 Output 레이어 정의, 손실함수측정 및 정의, Prefix-Tuning(극소량 파인튜닝)을 통한 정확도 개선 
#### 가-3. 답변 추론 및 설명 생성 기술 개발 및 고도화
* 데이터 셋 전처리 : 특정 성별에 해당하는 편견적인 답변이 생성되지 않도록 학습 데이터셋을 다양하게 구성 / 데이터 증강(Data augmentation) : 이미지에 가우시안 노이즈 포함시키기, 반전, 자르기, 색보정 등 / 추출한 질문 유형이 라벨링 된 데이터 셋 준비, 오타, 불용어, 젠더 편향성 확인 등 데이터 정리
* Pre-trained 모델 학습 : 트랜스포머 기반 모델 아키텍처 구성, 학습 환경 설정 및 학습 파라미터 정의( 예 : optimizer, learning rate, epoch, batch size) 및 텍스트와 이미지 데이터 학습
- 젠더 편향성을 고려하여 모델 학습 시 성별에 대한 정보를 최대한 활용하지 않음
* Pre-trained 모델 평가 및 전이학습 시작 : 답변 생성 성능 측정 및 설명 점수 측정
- 준비된 데이터 분량, 과적합/과소적합 문제 등에 따라 전이학습할 레이어 조정 / 손실 함수(loss function) 정의 및 측정 및 모델 파라미터 업데이트 / 손실 함수 최소화를 통한 전이학습 진행 및 반복
* 전이학습 완료모델 평가
- 조정된 모델로 검증 데이터(validation dataset)의 답변 및 질문 생성 및 실제 레이블과 비교  / BLEU, ROUGE-L, METEOR, Perplexity, CIDEr 평가지표를 사용해 모델 성능 평가
- 답변 생성 기술이 특정 성별에 대한 편견을 반영하지 않도록 일정 주기마다 모델 평가 및 보완 수행

![image](https://github.com/wendyunji/Wbridge-2023-F-1/assets/127592057/52fb6cdf-f0c6-4aff-9369-19ff5a6e9ef1)   
### **나. 웹 서비스 기획/디자인/개발 오픈소스 제공**
웹 개발 프레임워크 아키텍쳐 및 효과적인 사용자 유량 제어 및 관리를 위한 AWS 아키텍쳐
오픈소스 기반 웹 개발 프레임 워크를 사용한다. Flask와 Node.js를 이용하여 Front-End 및 Back-End를 구축하고 이를 Docker Container 환경 위에서 작동할 수 있도록 한다. 또한 Git 형상 관리 프로그램을 활용하여 협업이 가능한 개발환경을 마련한다. 개발된 프로그램은 오픈소스로 제안하여, 다른 개발자들과 사용자들이 이를 활용하고 발전시킬 수 있도록 한다.

## **Gantt Chart**
![image](https://github.com/wendyunji/Wbridge-2023-F-1/assets/127592057/d881e80b-7191-4c0f-ab4f-5aa2bca306e9)

