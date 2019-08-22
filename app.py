from flask import Flask, jsonify

# Dictionary 
dict = {}

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Surf's Up API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
 )

@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify (dict)s

@app.route("/api/v1.0/stations")
def stations():
    return jsonify( )

@app.route("/api/v1.0/tobs")
def tobs():    
   return jsonify()

@app.route("/api/v1.0/<start>")
def start():
    return 

@app.route("/api/v1.0/<start>/<end>")
def start/end():    
    

if __name__ == "__main__":
    app.run(debug=True, )
