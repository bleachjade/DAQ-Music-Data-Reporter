from flask import Flask, Response, render_template
from mongo_api import *

app = Flask(__name__)

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')

@app.route('/songs', methods=['GET'])
def mongo_read():
    data = {
        "database": "Song",
        "collection": "Deezer",
    }
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.read()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/songs/<song_id>', methods=['GET'])
def mongo_read_one(song_id):
    data = {
        "database": "Song",
        "collection": "Deezer",
    }
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    response = obj1.read_one(song_id)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')
  
if __name__ == '__main__':
    data = {
        "database": "Song",
        "collection": "Deezer",
    }
    mongo_obj = MongoAPI(data)

    app.run(debug=True, port=5001, host='0.0.0.0')

