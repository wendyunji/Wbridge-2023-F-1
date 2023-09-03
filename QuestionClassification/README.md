## hys_dataloader.ipynb 파일 int2label 구성
- "color" : 0, 
Color Attributes (e.g., ‘What color is the man’s tie?’) : 객체의 색상 속성 질문
- "object_presence" : 1,  
Object Presence (e.g., ‘Is there a cat in the image?’) : 객체의 존재 여부 질문
- "absurd" : 2,  
Absurd (i.e., Nonsensical queries about the image) : vqa 알고리즘이 이미지의 문맥 이해를 바탕으로 질문의 대답 가능 여부(answerable)를 판단할 수 있는지 테스트할 목적으로 구성. 질문에 답할 수 없다면 ‘Does Not Apply’를 출력해야 함. 
- "counting" : 3,  
Counting (e.g., ’How many horses are there?’) : 객체의 개수 질문
- "scene_recognition" : 4,  
Scene Classification (e.g., ‘What room is this?’) : 장면 분류 질문 
- "object_recognition" : 5,  
Subordinate Object Recognition (e.g., ‘What kind of furniture is in the picture?’) : 상위 의미 범주(ex : furniture)를 기반으로 객체의 subordinate-level object classification을 요구하는 질문 
- "positional_reasoning" : 6,  
Positional Reasoning (e.g., ‘What is to the left of the man on the sofa?’) : 특정 개체의 상대적 위치 질문(좌우만 포함, 상하는 포함되지 않음) 
- "attribute" : 7,  
Other Attributes (e.g., ‘What shape is the clock?’) : 객체의 색상 이외 속성 질문
- "sport_recognition" : 8,  
Sport Recognition (e.g.,‘What are they playing?’) : 사진에 해당하는 스포츠를 질문 
- "activity_recognition": 9,  
Activity Recognition (e.g., ‘What is the girl doing?’) : 활동 질문
- "sentiment_understanding" : 10,  
Sentiment Understanding (e.g.,‘How is she feeling?’) : 감정 이해 질문
- "utility_affordance" : 11,  
Object Utilities and Affordances (e.g.,‘What object can be used to break glass?’) : 객체의 용도/효용과 행동유도성 질문 