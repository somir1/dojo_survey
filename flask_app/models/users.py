from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User():

    def __init__(self, data = None):
            self.id = data['id']
            self.name = data['full_name']
            self.language = data['language']
            self.location = data['location']
            self.comment = data['comment']
            self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user_input;"
        results = connectToMySQL('dojo_survey').query_db(query)
        return User(results[-1])

    @classmethod
    def insert_user(cls, data):
        query = "INSERT INTO user_input(full_name, location, language, comment) VALUES (%(full_name)s, %(location)s, %(language)s, %(comment)s);"

        return connectToMySQL('dojo_survey').query_db(query, data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['full_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['comment']) > 10:
            flash("You have exceeded character limit")
            is_valid = False
        return is_valid
        