from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os

class Chating_text(BaseModel):
    text : str

class Chatbot_operation:
    def __init__(self):
        self.model_token = ""
        self.model_name = "meta-llama/Llama-2-7b-chat-hf"

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

        terminators = [
            self.tokenizer.eos_token_id,
            self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = self.model.generate(
                **input_ids,
                max_new_tokens=2048,
                eos_token_id=terminators,)
        return self.tokenizer.decode(outputs[0]).replace(f'<s>', '').replace('</s>', '')