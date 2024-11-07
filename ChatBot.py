from BotDefinition import OpenAIBot
engine = "gpt-4"
chatbot = OpenAIBot(engine)

while True:
    prompt = input()

    if prompt.upper() == 'END CHAT':
        break
    response = chatbot.generate_response(prompt)
    print(response)