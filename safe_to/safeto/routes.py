from flask import render_template, url_for, flash, redirect, request
from safeto import app, db
from safeto.forms import ReportForm
from safeto.models import Post

@app.route("/") 
@app.route("/home")
def home():
    posts = None
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/report/new", methods=['GET', 'POST'])
def new_report():
    form = ReportForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, location=form.location.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your report has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('create_report.html', title='New Report',
                           form=form, legend='New Report')

@app.route("/report/<int:report_id>")
def report(report_id):
    post = Post.query.get_or_404(report_id)
    return render_template('report.html', title=post.title, post=post)

@app.route("/report/<int:report_id>/update", methods=['GET', 'POST'])
def update_report(report_id):
    post = Post.query.get_or_404(report_id)
    form = ReportForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.location = form.location.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('report', report_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.location.data = post.location
    return render_template('create_report.html', title='Update Report',
                           form=form, legend='Update Report')

@app.route("/report/<int:report_id>/delete", methods=['POST'])
def delete_report(report_id):
    post = Post.query.get_or_404(report_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))