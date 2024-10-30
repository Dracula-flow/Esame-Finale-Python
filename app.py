from flask import Flask, render_template, request, url_for
from sqlalchemy import create_engine, text
app=Flask(__name__)

# Home con lista partecipanti parziale
@app.route("/", methods=['POST','GET'])
def index():

    engine = create_engine("mysql+pymysql://root@127.0.0.1/finale_python?charset=utf8mb4")
    with engine.connect() as conn:
        sql = text("SELECT * from runners")
        result = conn.execute(sql)
        runners = result.all()

    return render_template("home.html", runners=runners)

# Pagina di iscrizione alla maratona. NON SO COME FARE.
@app.route("/subscribe", methods=["GET"])
def insert():
    engine = create_engine("mysql+pymysql://root@127.0.0.1/finale_python?charset=utf8mb4")
    with engine.connect() as conn:
        sql = text("SELECT * from runners")
        result = conn.execute(sql)
        runners = result.all()

    return render_template("insert.html", runners=runners)

# Qui andranno tutti i partecipanti con tutti i dati
@app.route("/participants", methods=['GET','POST'])
def subscribe():
    if request.method=='POST':
        nome = request.form['name']
        cognome = request.form['surname']
        email = request.form['email']
        engine = create_engine("mysql+pymysql://root@127.0.0.1/finale_python?charset=utf8mb4")
        with engine.connect() as conn:
            params = {'nome': nome, 'cognome': cognome, 'email': email}
            sql = text("INSERT INTO runners(runner_name, runner_surname, runner_mail) VALUES(:nome,:cognome,:email)")
            conn.execute(sql,params)
            conn.commit() #necessario altrimenti droppa subito

            sql2= text("SELECT * from runners")
            result =conn.execute(sql2)
            runners = result.all()
        return render_template("all.html", runners=runners)
    else:
        engine = create_engine("mysql+pymysql://root@127.0.0.1/finale_python?charset=utf8mb4")
        with engine.connect() as conn:
            sql = text("SELECT * from runners")
            result = conn.execute(sql)
            runners = result.all()

            #Metodo bello, se solo funzionasse
            # stmt = insert().values(runner_name = nome, runner_surname= cognome, runner_mail= email)
            # result= conn.execute(stmt)
            # conn.commit(result)
        return render_template("all.html", runners=runners)

