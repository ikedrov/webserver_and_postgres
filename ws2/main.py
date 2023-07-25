# export FLASK_APP=main.py
#flask run --host='localhost' --port='5301'


from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

benefits = {'junior':['mac', 'coffee', 'fruits'],
            'middle':['junior+', 'gym', 'ensurance'],
            'senior':['middle+', 'taxi', 'parking']}

@app.route('/employee_pack', methods=['POST'])
def redir_employee_pack():

    employee_level = request.json['employee_level']

    if employee_level in benefits:
        benefit_title = employee_level + '_pack'
        employee_benefit_pack = {benefit_title: benefits[employee_level]}

    return jsonify(employee_benefit_pack)



