from transformers import AutoTokenizer
from transformers import DataCollatorWithPadding
import evaluate
import numpy as np
from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer
import torch

class DistilBERT():
    def __init__(self, id2label, label2id):
        self.model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=12, id2label=id2label, label2id=label2id)
        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
        self.data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer)
        self.accuracy = evaluate.load("accuracy")
    
    def preprocess_function(self,examples):
        return self.tokenizer(examples["text"], truncation=True)

    def tokenize(self, data):
        return data.map(self.preprocess_function, batched=True)

    def compute_metrics(self, eval_pred):
        predictions, labels = eval_pred
        predictions = np.argmax(predictions, axis=1)
        return self.accuracy.compute(predictions=predictions, references=labels)

    def train(self, tokenized_data):
        # tokenized_tdiuc = self.tokenize(data)
        training_args = TrainingArguments(
            output_dir="tdiuc-test",
            learning_rate=2e-5,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            num_train_epochs=2,
            weight_decay=0.01,
            evaluation_strategy="epoch",
            save_strategy="epoch",
            load_best_model_at_end=True,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized_data["train"],
            eval_dataset=tokenized_data["test"],
            tokenizer=self.tokenizer,
            data_collator=self.data_collator,
            compute_metrics=self.compute_metrics,
        )
        
        trainer.train()
