from flask import Flask, jsonify

# Dictionary of Justice League
justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


dict = {}

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
    return jsonify ()

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
