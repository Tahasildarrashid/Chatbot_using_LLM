import os
import google.generativeai as genai
import gradio as gr

# Configure the Generative AI model with the API key
API_KEY = "AIzaSyAPxs64F2IEHrRED_px8NLFutZ6Nq_kfy8"
genai.configure(api_key=API_KEY)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    full_response = ""
    for chunk in response:
        full_response += chunk.text
    return full_response

# Gradio interface
def chat_interface(question, history=[]):
    if question:
        response = get_gemini_response(question)
        history.append(("You", question))
        history.append(("Bot", response))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("# Gemini LLM Application")

    with gr.Column():
        chatbot = gr.Chatbot()
        with gr.Row():
            input_text = gr.Textbox(placeholder="Ask a question...", show_label=False)
            submit_btn = gr.Button("Send")
        
        submit_btn.click(chat_interface, inputs=[input_text, chatbot], outputs=[chatbot, chatbot])

demo.launch()
