# export FLASK_APP=main.py
#flask run --host='localhost' --port='5301'


from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/employee_pack', methods=['GET'])
def redir_employee_pack():

    url = 'http://0.0.0.0:5301/get_pack'
    employee_level = request.args.get('employee_level')
    employee_level_req = {'employee_level':employee_level}

    try:
        req = requests.post(url, json=employee_level_req).json()
        return jsonify(req)
    except requests.exceptions.ConnectionError:
        return 'Proxy is online, but ws1 is offline.'


