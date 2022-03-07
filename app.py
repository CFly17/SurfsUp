from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd

# SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the SQLite database above in our classes:
Base = automap_base()

# Reflect database so we can save our references to each table:
Base.prepare(engine, reflect=True)

# Create variables for each class so we can reference them later:
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)


# this variable deepends on where the code is run.
# if we wanted to import our app.py file into another Python file named example.py,
# the variable __name__ would be set to 'example'
app = Flask(__name__)

# NOTE:
# When creating routes, we follow the naming convention /api/v1.0/
# followed by the name of the route. This convention signifies
# that this is version 1 of our application


@app.route('/')
def welcome():
    return(
        '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# (1) add the line of code that calculates the date 
    # one year ago from the most recent date in the database (line 59)
# (2) add query to get the date and precipitation for the previous year (lines 60-1)
# (3) create a dictionary, date as the key and precipitation as the value
    # use jsonify() to format our results into a JSON structured file. 

@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
# Navigate to see it by adding 'api/v1.0/precipitation' to the end of the web address.


# (1) query all stations (line 73)
# (2) unravel results into a one-dimensional array
    #  Use list() function, then convert array into a list (line 74). 
    #  Then we'll jsonify the list and return it as JSON (line 75).
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# (1) calculate the date one year ago from the last date in the database (line 82)
# (2) query primary station for temperature observations in the previous year (line 83-5)
# (3) Unravel to list and convert to JSON
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# LAST ROUTE
# we need starting and end dates for this one!
# 'sel' list holds min, max and avg queries
# the 'if-not' statement allows us to 
    # get start and end dates to calculate temperatures
    # query database using list we just made
    # unravel results to one-dimensional array
    # convert array to a list
    # convert list to JSON
# The asterisk in (*sel) means we will have multiple results
# @app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

