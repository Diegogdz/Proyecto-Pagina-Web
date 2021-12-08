# Flask Setup
import os
from flask import Flask, jsonify, request, abort
app = Flask(__name__)
# Google Sheets API Setup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)
gsheet = client.open("tei101").sheet1

@app.route('/x')
def index():
    return jsonify(gsheet.get_all_records())

if __name__=="__main__":
    app.run(debug=True)