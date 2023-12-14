from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6'


class ContactForm(FlaskForm):
    name = StringField('Your name', validators=[DataRequired()])
    email = StringField('Your email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    f = open('projects.json')
    data = json.load(f)
    f.close()
    return render_template('about.html', projects=data['projects'])


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print(form.message.data)
        return render_template('contact.html', form=form, success=True)
    else:
        return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
