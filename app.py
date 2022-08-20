import sqlite3, socket
from flask import Flask, redirect, render_template, request, url_for
from asyncio.windows_events import NULL
from pickle import TRUE
from tkinter import *
from pyfirmata import Arduino, SERVO

#from test import *

myip = socket.gethostbyname_ex(socket.gethostname())[2][1]

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
	coneccao = sqlite3.connect("automSQL.db")
	cursor = coneccao.cursor()
	if (request.method == 'POST'):
		if 'controle' in request.form.to_dict():
			task_content = request.form.to_dict()

			aux = "select * from automacao WHERE ambiente = " + "'" + task_content['controle'] + "'"
			cursor.execute(aux)
			status = cursor.fetchall()

			if(task_content['val'] == 'ON'):
				if(status[0][3] == 'ON'):
					pass
				else:
					aux = "UPDATE automacao SET status = 'ON' WHERE ambiente = " + "'" + task_content['controle'] + "'"
					cursor.execute(aux)
					if(task_content['controle'] == 'Sala'):
						pin = 2
						#led(pin, 1)
					elif(task_content['controle'] == 'Cozinha'):
						pin = 7
						#led(pin, 1)
					elif(task_content['controle'] == 'Quarto'):
						pin = 8
						#led(p, 1)
					elif(task_content['controle'] == 'Suite'):
						pin = 12
						#led(pin, 1)
					elif(task_content['controle'] == 'Banheiro'):
						pin = 13
						#led(pin, 1)
					elif(task_content['controle'] == 'Alarme Casa'):
						pin = 4
						#Blink(pin, True)
			elif(task_content['val'] == 'Alterar'):
				pin = 9
				aux = "UPDATE automacao SET status = '" + task_content['content'] + "%' WHERE ambiente = 'Garagem'"
				cursor.execute(aux)
				#servoctrl(pin, task_content['content']*1.8)
			else:
				if (status[0][3] == 'OFF'):
					pass
				else:
					aux = "UPDATE automacao SET status = 'OFF' WHERE ambiente = " + "'" + task_content['controle'] + "'"
					cursor.execute(aux)
					if(task_content['controle'] == 'Sala'):
						pin = 2
						#led(pin, 0)
					elif(task_content['controle'] == 'Cozinha'):
						pin = 7
						#led(pin, 0)
					elif(task_content['controle'] == 'Quarto'):
						pin = 8
						#led(pin, 0)
					elif(task_content['controle'] == 'Suite'):
						pin = 12
						#led(pin, 0)
					elif(task_content['controle'] == 'Banheiro'):
						pin = 13
						#led(pin, 0)
					elif(task_content['controle'] == 'Alarme Casa'):
						pin = 4
						#Blink(pin, False)

			cursor.execute("select * from automacao")
			status = cursor.fetchall()
			coneccao.commit()
			coneccao.close()

			return render_template('index.html', contents=status)
	else:
		cursor.execute("select * from automacao")
		status = cursor.fetchall()
		return render_template('index.html', contents=status)

listaAmbientes = [
	("Sala","Lampada","","OFF",0,"18/08/2022 08:00:00","18/08/2022 18:00:00"),
	("Sala","Alarme","Seg Ter Qua Qui Sex Sab Dom","ON",24,"",""),
	("Sala","Temperatura","Seg Ter Qua Qui Sex Sab Dom","ON",24,"",""),
	("Cozinha","Lampada","Seg Ter Qua Qui Sex Sab Dom","OFF",0,"08:00:00","18:00:00"),
	("Quarto","Lampada","","OFF",4,"18/08/2022 08:00:00",""),
	("Suite","Lampada","","OFF",2,"","18/08/2022 18:00:00"),
	("Banheiro","Lampada","Seg Ter Qua Qui Sex Sab Dom","OFF",24,"",""),
	("Alarme Casa","Alarme","Seg Ter Qua Qui Sex Sab Dom","OFF",24,"",""),
	("Garagem",	"Portão","Seg Ter Qua Qui Sex Sab Dom",'0%',24,"","")
]

if __name__ == "__main__":
	app.run(host=myip, debug=True)