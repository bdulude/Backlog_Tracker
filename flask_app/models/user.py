from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (email, password, created_at, updated_at) VALUES (%(eml)s , %(pwd)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_by_email(cls, data:dict):
        query = "SELECT * FROM users WHERE email=%(eml)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return []
    
    @classmethod
    def get_one_by_id(cls, data:dict):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return []

    @staticmethod
    def regi_validation(data):
        is_valid = True
        if len(data['eml']) < 3:
            flash("Email not long enough.", "err_email")
            is_valid = False
        elif not EMAIL_REGEX.match(data['eml']): 
            flash("Invalid email address.", "err_email")
            is_valid = False
        else:
            user = User.get_one_by_email(data)
            if user:
                flash("Account with that email already exists.", "err_email")
                is_valid = False
        if len(data['pwd']) < 8:
            flash("Password must be at least 8 characters.", "err_password")
            is_valid = False
        elif data['pwd'] != data['pwd_conf']:
            flash("Passwords do not match.", "err_password")
            is_valid = False
        return is_valid
    
    @staticmethod
    def login_validation(data):
        is_valid =  True
        user_inst = User.get_one_by_email(data)
        if len(data['pwd']) < 8:
            flash("Password must be at least 8 characters.", "err_login")
            is_valid = False
        if len(data['eml']) < 3:
            flash("Email not long enough.", "err_login")
            is_valid = False
        elif not EMAIL_REGEX.match(data['eml']): 
            flash("Invalid email address.", "err_login")
            is_valid = False
        if user_inst:
            if not bcrypt.check_password_hash(user_inst.password, data['pwd']):
                flash("Invalid Credentials", "err_login")
                is_valid = False
            else:
                session["uuid"] = user_inst.id
                session['email'] = user_inst.email
        else:
            flash("Invalid Credentials", "err_login")
            is_valid = False
        return is_valid