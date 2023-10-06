import torch
from PIL import Image
import requests
import json
import sys
from nltk.translate.bleu_score import sentence_bleu
import os
import csv 


sys.path.append('/home/public/yunvqa/vcr/LAVIS')
from lavis.models import load_model_and_preprocess

# annotation
test_ann_path='/home/public/yunvqa/vcr/dataloaders/VCR_train.json'

with open(test_ann_path,'r') as file:
    annotations=json.load(file)

# 결과 저장 경로 
result_path='/home/public/yunvqa/vcr/jh/result' # 필요시 변경 

# setup device to use
device = torch.device("cuda") if torch.cuda.is_available() else "cpu"

# 질문 유형 추출하기 
from transformers import AutoTokenizer 
from transformers import AutoModelForSequenceClassification

tokenizer=AutoTokenizer.from_pretrained("/home/public/yunvqa/Wbridge-2023-F-1/QuestionClassification/tdiuc-test/checkpoint-13942",local_files_only=True)

step1_model=AutoModelForSequenceClassification.from_pretrained("/home/public/yunvqa/Wbridge-2023-F-1/QuestionClassification/tdiuc-test/checkpoint-13942",local_files_only=True)

print('모델 불러오는 중.. ')
step2_model, vis_processors, _ = load_model_and_preprocess(
    name="blip2_t5", model_type="pretrain_flant5xxl", is_eval=True, device=device
)

# 정답 예측 성능 측정 (acc, bleu score )
correct_count_prompt=0
correct_count_ans=0
bleu_scores_prompt=[]
bleu_scores_ans=[]


for annotation in annotations:
    correct_label_index=annotation['label']['weights'].index(1)
    label=annotation['label']['ids'][correct_label_index]

    image_path=annotation['image_id']
    raw_image=Image.open(image_path).convert('RGB')
    question=annotation['question']
    
    # question type 추출
    inputs=tokenizer(question,return_tensors="pt")
    with torch.no_grad():
        logits=step1_model(**inputs).logits
    predicted_class_id=logits.argmax().item()
    question_type=model.config.id2label[predicted_class_id]

    # prompt_ans : prompt tuning 된 모델의 answer
    prompt_ans=step2_model.generate({"image": raw_image, "prompt": "Question Type:{question_type} Question: which city is this? Answer:"})
    # ans : 기존 blip2 모델의 answer 
    ans=step2_model.generate({"image": raw_image, "prompt": "Question: which city is this? Answer:"})
    if label==prompt_ans[0]:
        correct_count_prompt+=1
        
    if label==ans[0]:
        correct_count_ans+=1

    # bleu  for prompt_ans
    bleu_score_prompt = sentence_bleu([label.split()], prompt_ans[0].split())
    bleu_scores_prompt.append(bleu_score_prompt)

    # bleu for ans
    bleu_score_ans=sentence_bleu([label.split()], ans[0].split())
    bleu_scores_ans.append(bleu_score_ans)

# 정확도 계산
accuracy_prompt=correct_count_prompt / len(annotations)
accuracy_ans=correct_count_ans /len(annotations)

# BLEU 점수의 평균 계산
average_bleu_prompt=sum(bleu_scores_prompt) /len(bleu_scores_prompt)
average_bleu_ans = sum(bleu_scores_ans) / len(bleu_scores_ans)

# 결과 저장

with open(os.path.join(result_path,'BLIP2_result.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Metric", "Value (With Prompt Engineering)", "Value (Without Prompt Engineering)"])
    writer.writerow(["Accuracy", accuracy_prompt, accuracy_ans])
    writer.writerow(["Average BLEU", average_bleu_prompt, average_bleu_ans])