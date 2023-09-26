import openai
import os


class Chatbot:
    def __init__(self):
        openai.api_key = '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'

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-edit-001",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)


