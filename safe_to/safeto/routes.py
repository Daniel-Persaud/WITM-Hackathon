from flask import render_template, url_for, flash, redirect
from safeto import app, db
from safeto.forms import ReportForm
from safeto.models import Post

@app.route("/") 
@app.route("/home")
def home():
    posts = None
    #with app.app_context():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/report/new", methods=['GET', 'POST'])
def new_report():
    form = ReportForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        #with app.app_context():
        db.session.add(post)
        db.session.commit()
        flash('Your report has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('create_report.html', title='New Report', form=form)