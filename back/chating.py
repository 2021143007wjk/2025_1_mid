from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

class Chating_text(BaseModel):
    text : str

class Chatbot_operation:
    def __init__(self):
        self.model_token = ""
        self.model_name = "google/gemma-2-2b-it"

        os.environ['HF_TOKEN'] = self.model_token
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map="auto",
            torch_dtype=torch.bfloat16,
        )
    
    def chatbot_operation(self, question: str):
        input_text = question
        input_ids = self.tokenizer(input_text, return_tensors="pt").to("cuda")

        outputs = self.model.generate(**input_ids, max_length=512)
        return self.tokenizer.decode(outputs[0])