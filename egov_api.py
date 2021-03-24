import uuid
import requests
import json
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>SAI 2021</h1><p>API on Flask.</p>"

@app.route('/api/getData', methods=['POST'])
def get_data():
    content = request.json

    pinfl = content['pinfl']
    passSerialNumber = content['passSerialNumber']
    myuuid = uuid.uuid4()

    print("pinfl: " + pinfl)
    print("passSerialNumber: " + passSerialNumber)
    print('Your UUID is: ' + str(myuuid))

    params = {
        'query_id': str(myuuid),
        'pinfl': pinfl,
        'passSerialNumber': passSerialNumber,
        'client_id': 'ucell',
        'secret_client': 'dWNlbGxfbXJ6X3JlYWRlcl9lZ292XzIwMjE=',
        'user_id': 'Test_User',
        'pd_allow': 'true'
    }
    jsonData = json.dumps(params)
    print(jsonData)

    headers = {'Content-type': 'application/json'}
    response = requests.post('http://mrz-api.egov.uz/mrz/getData',
                             data=jsonData,
                             headers=headers)

    #Code response
    #79 - no data found or incorrect
    #82 - some fields are empty
    #88 - Autentification error


    print(response.status_code)
    print(response.content)

    return response.content






if __name__ == '__main__':
    app.run(host= 'localhost',debug=True)