from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm
import gunicorn

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/contactus", methods=['GET', 'POST'])
def contact():
	if request.method == 'POST':
		flash('Your details have been successfully updated!', 'success')
		return render_template('contact.html')
	else:
		return render_template('contact.html')


if __name__ == '__main__':
	app.run(debug=True)