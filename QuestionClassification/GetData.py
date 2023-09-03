import json
from sklearn.model_selection import train_test_split
from datasets.dataset_dict import DatasetDict
from datasets import Dataset

class TDIUC:
    def __init__(self):
        self.label2id = {
            "color" : 0, 
            "object_presence":1,  
            "absurd":2, 
            "counting" : 3,
            "scene_recognition" : 4, 
            "object_recognition" : 5,
            "positional_reasoning" : 6,
            "attribute" : 7,
            "sport_recognition" : 8,
            "activity_recognition": 9,
            "sentiment_understanding" : 10,
            "utility_affordance" : 11
        }
        
        self.id2label = {
            0 : "color", 
            1 : "object_presence",  
            2 : "absurd", 
            3 : "counting",
            4 : "scene_recognition", 
            5 : "object_recognition",
            6 : "positional_reasoning",
            7 : "attribute",
            8 : "sport_recognition",
            9 : "activity_recognition",
            10 : "sentiment_understanding",
            11 : "utility_affordance"
        }
        
    def get_tdiuc(self):
        with open('/home/public/yunvqa/clip/clip/dataset/TDIUC/tdiuc/raw/annotations_merged/mscoco_train2014_merged.json', 'r') as f:
            json_data = json.load(f)
        result_data = []

        for i in range(len(json_data)):
            result_data.append({ "label": self.label2id[json_data[i]["question_type"]],"text": json_data[i]["question"],})
        tdiuc = {}

        X_train, X_test = train_test_split(result_data, test_size=0.2, random_state=123)

        tdiuc['test'] = X_test
        tdiuc['train'] = X_train
        
        X_train_labels = [item['label'] for item in X_train]
        X_test_labels = [item['label'] for item in X_test]

        X_train_texts = [item['text'] for item in X_train]
        X_test_texts = [item['text'] for item in X_test]

        tdiuc = {'train':Dataset.from_dict({'label':X_train_labels,'text':X_train_texts}),
            'test':Dataset.from_dict({'label':X_test_labels,'text':X_test_texts})}

        tdiuc = DatasetDict(tdiuc)
        return tdiuc, self.id2label, self.label2id
    
