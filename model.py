from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///sqlite.db'
app.config['FLASK_ADMIN_SWATCH'] ='cerulean'

db = SQLAlchemy(app)
class Movies (db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    title = db.Column( db.String(100), unique = True, nullable = False)
    def __repr__(self):
        return '< Title % r >' %self.title

admin = Admin(app, name = 'movielog', template_mode = 'bootstrap3')
admin.add_view(ModelView(Movies, db.session))

class Music(db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    title = db.Column( db.String(100), unique = True, nullable = False)
    def __repr__(self):
        return '< Title % r >' %self.title
admin.add_view(ModelView(Music, db.session))

class Actors(db.Model):
    Id = db.Column(db.Integer, primary_key = True)
    title = db.Column( db.String(100), unique = True, nullable = False)
    def __repr__(self):
        return '< Title % r >' %self.title

db.create_all()
admin.add_view(ModelView(Actors, db.session))

if __name__=='__main__':
    app.run(debug=True)
