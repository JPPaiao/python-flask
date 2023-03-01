from flask import Flask, jsonify, request
from markupsafe import escape
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello_world():
    return { "menssage": "Hello world!" }

@app.route("/user/<username>")
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route("/user", methods=['POST'])
def show():
    req = request.get_json()
    return req

@app.route("/plan")
def plan():
    tabela = pd.read_excel('caixa-mensal-2023.xlsx')
    caixa = tabela['CAIXA']
    js = { "caixa": caixa }
    # return jsonify(js)
    return f'<div>{caixa}</div>'
