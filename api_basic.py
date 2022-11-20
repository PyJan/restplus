from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

a_language = api.model('Language', {'language': fields.String('input_language')})

languages = [{'language': 'python'}]

@api.route('/language')
class Language(Resource):

    def get(self):
        return languages

    @api.expect(a_language)
    def post(self):
        languages.append(api.payload)
        return 'language added', 201

if __name__ == '__main__':
    app.run(debug=True)

