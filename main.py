from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:launchcode@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('base.html', title= "This is my blog!")


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    if request.method == 'POST':
        return redirect('/')
    else:
        return render_template('blog.html', title="Add a new blog entry")


if __name__ == '__main__':
    app.run()
