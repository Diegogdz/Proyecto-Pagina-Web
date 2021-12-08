from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds']
credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
gsheet = client.open("empresas").sheet1






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

@app.route('/forms', methods=['POST'])
def register_user():
    users = gsheet.get_all_records()
    new_id = int(users[-1]['id'])+1
    # return jsonify(req)
    row = [new_id,request.form['Nombre'],request.form['Mail'],request.form['Empresa']]
    gsheet.insert_row(row, 2)
    return redirect('/empresas')

   





