import openai

openai.api_key = "Enter Your API Key Here"

class OpenAIBot:
    def __init__(self,engine):
        self.conversation = [{"role": "system", "content": "You are a helpful assistant."}]
        self.engine = engine
    def add_message(self, role, content):
        self.conversation.append({"role": role, "content": content})
    def generate_response(self, prompt):
        self.add_message("user", prompt)
        try:
            response = openai.ChatCompletion.create( model=self.engine, messages=self.conversation)
            assistant_response = response['choices'][0]['message']['content'].strip()
            self.add_message("assistant", assistant_response)
            return assistant_response
        except:
            print('Error Generating Response!')