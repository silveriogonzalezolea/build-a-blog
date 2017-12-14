from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:launchcode@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = "$$#^^&*JNFDFVRG("

#Create Blog class and a constructor with title and body parameters
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(250))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/')
def index():
   return redirect('/blog')



@app.route("/newpost", methods = ['POST','GET'])
def newpost():
    
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_blog = Blog(title, body)
        db.session.add(new_blog)
        db.session.commit()

    return render_template("newpost.html", title ="Create something assho--!")

@app.route("/blog", methods = ['POST', 'GET'])
def blog():
    if request.method == 'POST':
        blog_title= request.form['title']
        blog_body= request.form['body']
        
        title_error = ""
        body_error = ""

        if blog_title == "":
            title_error = "Please add a blog title."
            

        if blog_body =="":
            body_error = "Please add some content to the new blog post."
            

            #messages = [blog_title,blog_body, body_error, title_error]
        
        if title_error or body_error:
            return render_template("newpost.html", blog_title = blog_title, blog_body = blog_body, 
            title_error = title_error, body_error = body_error)
        
        else:
            new_blog = Blog(blog_title, blog_body)
            db.session.add(new_blog)
            db.session.commit()

            return render_template("single_entry.html", blog = new_blog)

    else:
        is_blog_id = request.args.get('id')
        if is_blog_id:
            single_blog = Blog.query.filter_by(id = is_blog_id).first()
            return render_template("single_entry.html", blog = single_blog)
        else:
            blogs = Blog.query.all()
            return render_template("all_entries.html", blogs = blogs, title = "MiBlogs")


if __name__ == "__main__":
    app.run()

