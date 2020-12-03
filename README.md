
# DAQ-Music-Data-Reporter
A Music Data API and Data Display app. Our API can be used to report various information about music. It can also be used to view the song’s popularity over the past few days or a certain amount of time, as well as checking if the song is available for streaming in that country or not.

# Members
Department of Computer Engineering, Software and Knowledge Engineering.

| Student ID  | Name | GitHub |
| --- | --- | --- |
| 6110545562  | Pawaris Wongsalung (Brew)  | [@kabilza](https://github.com/kabilza) |
| 6110545481  | Chananya Photan (Fin)  | [@forfeen](https://github.com/forfeen) |
| 6110545503  | Nattapol Boonyapornpong (Jade)  | [@bleachjade](https://github.com/bleachjade) |
| 6110545678  | Arisa Pangpeng (Mew)  | [@kidstylex](https://github.com/kidstylex) |



# Our Datasource API
- [Deezer API Documentation (deezerdevs) | RapidAPI](https://rapidapi.com/deezerdevs/api/deezer-1?endpoint=53aa5085e4b07e1f4ebeb429)    
- [Genius API Documentation (brianiswu) | RapidAPI](https://rapidapi.com/brianiswu/api/genius)    
- [Billboard-API API Documentation (LDVIN) | RapidAPI](https://rapidapi.com/LDVIN/api/billboard-api)    
- [Shazam API Documentation (apidojo) | RapidAPI](https://rapidapi.com/apidojo/api/shazam)   

## Requirements
 
| Name     | Version                                                                        | Description                                                                                                         |
| -------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Python    | [version 3 and above](https://www.python.org/downloads/)                       | Python is needed for running Flask APIs server.                 |
| Flask | [1.1.1](https://pypi.org/project/Flask/) | Since Flask is written in Python, we need Python to compile the code and run. It also handles the work of sending JSONs data.|
| PIP | [any latest version](https://pip.pypa.io/en/stable/installing/) | Needed for installing extra dependencies for Python|
| Flask CORS | [3.0.9](https://flask-cors.readthedocs.io/en/latest/) | Needed for testing cross site APIs reading and graphing data locally on localhost, use PIP to install.|
 
# Getting Started

1. Clone the repository.
```
$ git clone https://github.com/kabilza/DAQ-Music-Data-Reporter.git
```
2. Change directory to the directory that contains `server.py` directory
```
$  cd DAQ-Music-Data-Reporter
```
3. Create virtualenv in the directory and active virtualenv.
```
$  virtualenv venv
```
##### On MacOS and Linux:
```
  $ source venv/bin/activate
```
 
##### On Windows:
```
  $ venv\Scripts\activate
```
4. Install all required packages.
##### On MacOS and Linux:
```
  (venv) pip3 install -r requirements.txt
```
 
##### On Windows:
```
  (venv) pip install -r requirements.txt
```
5. Running the project 
##### On MacOS and Linux:
```
  (venv) python3 server.py 
```
 
##### On Windows:
```
  (venv) python server.py 
```
