from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash, session

class Movie:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.synopsis = data['synopsis']
        self.rating = data['rating']
        self.image = data['image']
        self.link = data['link']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.used = data['used'] # set on creation like user_id
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data:dict):
        query = "INSERT INTO movies (title, synopsis, link, rating, used, image, user_id, created_at, updated_at) VALUES ( %(title)s, %(synopsis)s, %(link)s, %(rating)s, 0, %(image)s, %(user_id)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data:dict):
        query = "SELECT * FROM movies WHERE id=%(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return []

    @classmethod
    def get_all(cls, data:dict):
        query = "SELECT * FROM movies WHERE user_id = %(user_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return []
    

    @classmethod
    def update(cls, data:dict):
        query = 'UPDATE movies SET title=%(title)s, synopsis=%(synopsis)s, rating=%(rating)s, used=%(used)s, image=%(image)s, updated_at=NOW() WHERE (id=%(id)s);'
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM movies WHERE (id=%(id)s);'
        return connectToMySQL(DATABASE).query_db(query, data)


# REPLACE ALL "NOT IN" CHECKS, THEY DO NOTHING

    @staticmethod
    def validate(data:dict):
        is_valid = True
        # All fields required
        if 'title' not in data:
            flash("Movie needs a title.", "err_title")
            is_valid = False
        elif len(data['title']) < 2:
            flash("Title needs to be longer than 2 characters.", "err_title")
            is_valid = False
        if 'synopsis' not in data:
            flash("Movie needs a synopsis.", "err_synopsis")
            is_valid = False
        elif len(data['synopsis']) < 2:
            flash("Synopsis needs to be longer than 2 characters.", "err_synopsis")
            is_valid = False
        if 'rating' not in data:
            flash("Movie needs a rating.", "err_rating")
            is_valid = False
        if 'image' not in data:
            flash("Movie needs a image.", "err_image")
            is_valid = False

        # if 'date_of' not in data:
        #     flash("Movie needs a date.", "err_date")
        #     is_valid = False
        # elif len(data['date_of']) < 6:
        #     flash("Date of needs to be longer than 6 characters.", "err_date")
        #     is_valid = False
        # if 'whappened' not in data:
        #     flash("Movie needs a location.", "err_happened")
        #     is_valid = False
        # elif len(data['whappened']) < 2:
        #     flash("What happened needs to be longer than 2 characters.", "err_happened")
        #     is_valid = False
        # if not bool(data['nosasq']):
        #     flash("Movie needs a number of sasquatches.", "err_sasq")
        #     is_valid = False
        # # Number of sasquatches > 1
        # elif bool(data['nosasq']) and int(data['nosasq']) < 1:
        #     flash("If there are no sasquatches, it isn't a sighting.", "err_sasq")
        #     is_valid = False
        return is_valid