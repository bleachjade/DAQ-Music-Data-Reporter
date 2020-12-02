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

    response = (artist_list)   
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/artists/albums', methods=['GET'])
def mongo_read_artists_album():
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
    artist_list = {}

    for i in range(len(convert1)):
        artist_list[str(convert1[i]['artist'])] = str(convert1[i]['number_of_albums'])

    response = (artist_list)   
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/artists/fans', methods=['GET'])
def mongo_read_artists_fans():
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
    artist_list = {}

    for i in range(len(convert1)):
        artist_list[str(convert1[i]['artist'])] = str(convert1[i]['number_of_fans'])

    response = (artist_list)   
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/artists/contacts', methods=['GET'])
def mongo_read_artists_contacts():
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
    artist_list = {}

    for i in range(len(convert1)):
        artist_list[str(convert1[i]['artist'])] = convert1[i]['contacts'][0]

    response = (artist_list)   
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
    jsonobg = {}

    for i in range(len(convert1)):
        artist_list['name'].append(convert1[i]['artist'])

    print(artist_list)
    print(artist_list['name'][int(artist_id)])

    jsonobg['artist_name'] = str(artist_list['name'][int(artist_id)])

    response = jsonobg
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/artists/songs', methods=['GET'])
def mongo_read_artists_songs():
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
    artist_list = {}
    all_tracks = []
    
    print(int(len(convert1)))

    for i in range(int(len(convert1))):
        track = []

        for a in range(len(convert1[i]['top_tracks'])):
            track.append(convert1[i]['top_tracks'][a]['title'])
        all_tracks.append(track)

    for i in range(int(len(convert1))):
        for a in range(len(all_tracks)):
            artist_list[str(convert1[i]['artist'])] = (all_tracks[i])

    response = (artist_list)   
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')
  
if __name__ == '__main__':
    print("*** SWAGGER UI must run in INCOGNITO MODE or CLEAR THE BROWSER CATCH ***")
    app.run(debug=True, port=5001, host='0.0.0.0')

#SWAGGER UI must run in INCOGNITO MODE or CLEAR THE BROWSER CATCH