from flask_restx import Resource, fields
from app import api, db
from app.models import Prompt
from app.openai_api import ChatGptBotApi

ns = api.namespace('prompts', description='Prompt operations')

prompt_model = api.model('Prompt', {'text': fields.String})
prompt_model_view = api.model('Prompt', {'id': fields.Integer,'text': fields.String})

chatbot_api = ChatGptBotApi()

# apis with with no query parameter i.e. get all prompts & create a new prompt
@ns.route('/')
class PromptListResource(Resource):
    @ns.marshal_list_with(prompt_model_view)
    def get(self):
        """Get all prompts"""
        prompts = Prompt.query.all()
        return prompts

    @ns.expect(prompt_model)
    def post(self):
        """Create a new prompt"""
        data = api.payload
        new_prompt = Prompt(text=data['text'])
        db.session.add(new_prompt)
        db.session.commit()
        return {'message': 'Prompt created successfully'}

# apis with query parameter -> id i.e. is delete, update a prompt & get prompt and its response
@ns.route('/<int:id>')
class PromptResource(Resource):
    @ns.marshal_with(prompt_model)
    def get(self, id):
        """Get a specific prompt by ID"""
        prompt = Prompt.query.get(id)
        response = chatbot_api.get_response(id)
        if prompt:
            return {'id': id, 'prompt': prompt['text'], 'response': response}
        return {'message': 'Prompt not found'}, 404

    @ns.expect(prompt_model)
    def put(self, id):
        """Update a prompt's text by ID"""
        prompt = Prompt.query.get(id)
        if not prompt:
            return {'message': 'Prompt not found'}, 404

        data = api.payload
        prompt.text = data['text']
        db.session.commit()
        return {'message': 'Prompt updated successfully'}

    def delete(self, id):
        """Delete a prompt by ID"""
        prompt = Prompt.query.get(id)
        if prompt:
            db.session.delete(prompt)
            db.session.commit()
            return {'message': 'Prompt deleted successfully'}
        return {'message': 'Prompt not found'}, 404
