import gradio as gr

def chat_handler(message, history):
    return "Hello World"

interface = gr.ChatInterface(chat_handler)

if __name__ == "__main__":
    interface.launch(show_api=False)