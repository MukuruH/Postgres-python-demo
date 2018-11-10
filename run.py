from flask import Flask, jsonify, request
from database import DatabaseConnection

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/db')
def db_endpoint():
    db = DatabaseConnection()

    rowcount = db.create_parcel('mac pro', 'kiwatule', 'ntinda', 999000, '2018-07-21', False)
    print(rowcount)

    parcels = db.get_all_parcel()
    print(parcels)

    for parcel in parcels:
        print('######')
        item = ''
        item += ' ' + parcel['name']
        item += ' ' + parcel['source']
        item += ' ' + parcel['destination']
        item += ' ' + str(parcel['price'])
        item += ' ' + str(parcel['delivery_date'])
        item += ' ' + str(parcel['delivered'])
        print(item)
    return str(parcels)


if __name__ == '__main__':
    app.run(debug=True)
