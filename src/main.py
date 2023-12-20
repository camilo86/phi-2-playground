import gradio as gr
import transformers as trf

pipeline = trf.pipeline("text-generation", model="microsoft/phi-2", trust_remote_code=True)

def chat_handler(message, history):
    answers = pipeline(message)
    
    for answer in answers:
        yield answer["generated_text"]

interface = gr.ChatInterface(chat_handler)

if __name__ == "__main__":
    interface.queue().launch(show_api=False)