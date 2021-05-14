# Import Flask
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine, reflect=True)

measurement = base.classes.measurement
station = base.classes.station

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    a = (f"Available Routes: <br>"
        f"/api/v1.0/precipitation <br>"
        f"/api/v1.0/stations <br>"
        f"/api/v1.0/tobs <br>"
        f"/api/v1.0/<start> <br>"
        f"/api/v1.0/<start>/<end> <br>")
    return a

@app.route("/api/v1.0/precipitation")
def precipitation():
    p = session.query(measurement.date, measurement.prcp).filter(measurement.date >= dt.date(2016, 8, 23)).all()

    p_1 = {date:prcp for date,prcp in p}


    return jsonify(p_1)


if __name__ == '__main__':
    app.run(debug=True)
