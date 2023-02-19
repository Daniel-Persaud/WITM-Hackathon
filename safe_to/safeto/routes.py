from flask import render_template, url_for, flash, redirect, request
from safeto import app, db
from safeto.forms import ReportForm
from safeto.models import Report

@app.route("/") 
@app.route("/home")
def home():
    reports = None
    reports = Report.query.all()
    return render_template('home.html', reports=reports)


@app.route("/resources")
def resources():
    return render_template('resources.html', title='Resources')

@app.route("/report/new", methods=['GET', 'POST'])
def new_report():
    form = ReportForm()
    if form.validate_on_submit():
        report = Report(category=form.category.data, location=form.location.data, description=form.description.data)
        db.session.add(report)
        db.session.commit()
        flash('Your report has been submitted!', 'success')
        return redirect(url_for('home'))
    return render_template('create_report.html', title='New Report',
                           form=form, legend='New Report')

@app.route("/report/<int:report_id>")
def report(report_id):
    report = Report.query.get_or_404(report_id)
    return render_template('report.html', category=report.category, report=report)

@app.route("/report/<int:report_id>/update", methods=['GET', 'POST'])
def update_report(report_id):
    report = Report.query.get_or_404(report_id)
    form = ReportForm()
    if form.validate_on_submit():
        report.category = form.category.data
        report.description = form.description.data
        report.location = form.location.data
        db.session.commit()
        flash('Your report has been updated!', 'success')
        return redirect(url_for('report', report_id=report.id))
    elif request.method == 'GET':
        form.category.data = report.category
        form.description.data = report.description
        form.location.data = report.location
    return render_template('create_report.html', title='Update Report',
                           form=form, legend='Update Report')

@app.route("/report/<int:report_id>/delete", methods=['POST'])
def delete_report(report_id):
    report = Report.query.get_or_404(report_id)
    db.session.delete(report)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('home'))