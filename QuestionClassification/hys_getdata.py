import json
from sklearn.model_selection import train_test_split


class TDIUC:
    def __init__(self):
        self.int2label = {
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
        
        self.label2int = {
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
        #for i in range (len(q_json_data)):
        for i in range(len(json_data)):
            result_data.append({ "label": self.int2label[json_data[i]["question_type"]],"text": json_data[i]["question"],})
        tdiuc = {}

        X_train, X_test = train_test_split(result_data, test_size=0.3, random_state=123)

        tdiuc['test'] = X_test
        tdiuc['train'] = X_train
        
        return tdiuc

if __name__ == "__main__":
    data = TDIUC()
    print(data.get_tdiuc()['test'][0])
    
