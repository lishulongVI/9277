from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@192.168.91.129/tornado'
db = SQLAlchemy(app)


class News(db.Model):
    __tablename__ = 'news'

    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(2000), nullable=False)
    # content = db.Column(db.String(2000), nullable=False)
    # types = db.Column(db.String(2000), nullable=False)
    # author = db.Column(db.String(2000), nullable=False)
    # created_at = db.Column(db.DateTime,)
    # is_valid = db.Column(db.Boolean,)

    def __repr__(self):
        return '<News %r>' % self.title

if __name__ == '__main__':
    app.run(debug=True)