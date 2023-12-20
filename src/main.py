import torch
import gradio
from transformers import AutoModelForCausalLM, AutoTokenizer

torch.set_default_device("cuda")

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2", torch_dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2", trust_remote_code=True)

def chat_handler(message, history):
    history_str = '\n'.join(history)
    inputs = tokenizer.encode_plus(history_str, message, return_tensors="pt", return_attention_mask=False)
    outputs = outputs = model.generate(**inputs, max_length=200)
    answers = tokenizer.batch_decode(outputs)
    
    for answer in answers:
        yield answer

interface = gradio.ChatInterface(chat_handler)

if __name__ == "__main__":
    interface.queue().launch(show_api=False)