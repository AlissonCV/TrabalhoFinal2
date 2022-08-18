import sqlite3

con = sqlite3.connect('automSQL.db')

cur = con.cursor()

listaAmbientes = [
	("Alarme Casa","Alarme","Seg Ter Qua Qui Sex Sab Dom","ON",24,"",""),
	("Garagem",	"Portão","Seg Ter Qua Qui Sex Sab Dom","0%",24,"","")
]

cur.executemany("insert into automacao values (?,?,?,?,?,?,?)", listaAmbientes)

con.commit()
con.close()