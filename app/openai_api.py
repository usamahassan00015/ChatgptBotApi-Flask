import openai
from app.models import Prompt
from app import db

class ChatGptBotApi:
    def __init__(self):
        #openai.api_key = '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'
        openai.api_key = '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'

    def create_prompt(self, prompt_text):
        new_prompt = Prompt(text=prompt_text)
        db.session.add(new_prompt)
        db.session.commit()
        return {'message': 'Prompt created successfully'}

    def get_response(self, prompt_id):
        prompt = Prompt.query.get(prompt_id)
        if prompt:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt.text,
                max_tokens=50
            )
            return {'response': response.choices[0].text.strip()}
        return {'message': 'Prompt not found'}, 404