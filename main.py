from flask import Flask, jsonify, request
import updatedb
from questions import getq


app = Flask(__name__) 
  
  
@app.route('/update/', methods = ['POST']) 
def updateDb(): 
    data = request.json
    updatedb.updatedb(data['name'], data['email'], data['score'], data['time'])
    return jsonify(request.json)
  

@app.route('/leaderboard/', methods = ['GET']) 
def leaderboardsz(): 
    return jsonify(updatedb.retrieve_leaderboard())


@app.route('/questions/', methods = ['GET']) 
def questions(): 
    return jsonify(getq())


# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 


