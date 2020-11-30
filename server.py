from flask import Flask, Response, render_template
from mongo_api import *
from data.config import *

app = Flask(__name__)

#SWAGGER UI must run in INCOGNITO MODE or CLEAR THE BROWSER CATCH

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')

@app.route('/artists', methods=['GET'])
def mongo_read_artists():
    data = {
        "database": f"{database_name}",
        "collection": f"{collection_name}",
    }

    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI(data)
    convert1 = obj1.read()
    artist_list = {'name':[]}

    for i in range(len(convert1)):
        artist_list['name'].append(convert1[i]['artist'])

    response = str(artist_list)   
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/artists/<artist_id>', methods=['GET'])
def mongo_read_one(artist_id):
    data = {
        "database": f"{database_name}",
        "collection": f"{collection_name}"
    }

    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')

    obj1 = MongoAPI(data)
    convert1 = obj1.read()
    artist_list = {'name':[]}

    for i in range(len(convert1)):
        artist_list['name'].append(convert1[i]['artist'])

    print(artist_list)
    print(artist_list['name'][int(artist_id)])

    response = "{'name': '" + str(artist_list['name'][int(artist_id)]) + "'}"

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
    print("*** SWAGGER UI must run in INCOGNITO MODE or CLEAR THE BROWSER CATCH ***")
    app.run(debug=True, port=5001, host='0.0.0.0')

#SWAGGER UI must run in INCOGNITO MODE or CLEAR THE BROWSER CATCH