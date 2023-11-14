from langchain.llms import Ollama
import gradio as gr

class SafetyExpertChatbot:
    def __init__(self, base_url, model_name):
        self.ollama = Ollama(base_url=base_url, model=model_name)
        self.demo = gr.Blocks()
        self._setup_ui()

    def _setup_ui(self):
        with self.demo:
            self.chatbot = gr.Chatbot()
            self.msg = gr.Textbox()
            self.clear = gr.ClearButton([self.msg, self.chatbot])
            self.msg.submit(self.run_ollama, inputs=[self.msg, self.chatbot], outputs=[self.msg, self.chatbot])

    def run_ollama(self, text, chat_history):
        ollama_response = self.ollama(text)
        chat_history.append((text, ollama_response))
        return "", chat_history

    def launch(self):
        self.demo.launch()

if __name__ == "__main__":
    print("Loading Safety Expert Chatbot...")
    chatbot_app = SafetyExpertChatbot(base_url='http://localhost:11434', model_name="safety_expert")
    chatbot_app.launch()