from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from asyncio.windows_events import NULL
from pickle import TRUE
from tkinter import *
from pyfirmata import Arduino, SERVO
#from test import *

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///status.db'
#db = SQLAlchemy(app)

#class Status(db.Model):
#	id = 

@app.route("/", methods=['GET', 'POST'])
def index():
	if (request.method == 'POST'):
		if 'on' in request.form.to_dict():
			#ledon()
			return redirect('/')
		if 'off' in request.form.to_dict():
			#ledoff()
			return redirect('/')
		if 'blink' in request.form.to_dict():
			#Blink()
			return redirect('/')
		else:
			#task_content = request.form['content']
			#servoctrl(task_content)
			return redirect('/')
	else:
		return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)