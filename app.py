from flask import Flask, request
from config import Config
from models import db, User
from flask_restx import Api, Resource, fields

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    api = Api(app, version='1.0', title='RAD API', description='A simple RAD API', doc='/swagger/')

    ns = api.namespace('users', description='RAD with Python')

    user_model = api.model('User', {
        'id': fields.Integer(readOnly=True, description='User unique identifier'),
        'name': fields.String(required=True, description='User name'),
        'email': fields.String(required=True, description='User email')
    })

    @ns.route('/')
    class UserList(Resource):
        @ns.doc('list_users')
        @ns.marshal_list_with(user_model)
        def get(self):
            """List all users"""
            users = User.query.all()
            return users

        @ns.doc('create_user')
        @ns.expect(user_model)
        @ns.marshal_with(user_model, code=201)
        def post(self):
            """Create a new user"""
            data = request.json
            new_user = User(name=data['name'], email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return new_user, 201

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)