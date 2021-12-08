from flask import Flask, render_template, request, redirect, jsonify

from pprint import pprint


app = Flask(__name__)

import gspread 
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credential = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
sheet = client.open("empresas").sheet1


@app.route('/formulario', methods=['POST']) 
def formulario():
    user = sheet.get_all_records()
    new_id = (users[0]['id']+1)
    Nombre = request.form["Nombre"]
    Empresa = request.form["Empresa"]
    Mail = request.form["Mail"]
    sheet = client.open("empresas").sheet1
    insertRow =[new_id, "Nombre", "Mail", "Empresa"]

    sheet.insert_row(insertRow,2)
     
    return redirect('/empresas')


@app.route("/contacto" , methods=["POST"])
def conact():
    Nombre = request.form["Nombre"]
    Empresa = request.form["Empresa"]
    Mail = request.form["Mail"]
    user = sheet.get_all_records()

    
    return redirect('/empresas')    


@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/importancia')
def importancia():
    return render_template("/importancia.html")

@app.route('/puntos_limpios')
def puntos():
    return render_template("/puntos_limpios.html")

@app.route('/empresas')
def empresas():
    return render_template("/empresas.html")

@app.route('/equipo')
def equipo():
    return render_template("/equipo.html")        


   

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template(
        "show.html",
        name_on_template=name_from_form,
        email_on_template=email_from_form
    )




