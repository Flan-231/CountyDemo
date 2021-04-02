from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html', options=get_state_options())

@app.route("/fact")
def fact():
    state = request.args['state']
    return render_template('fact.html', funFact = fun_fact_by_state(state))
    
def get_state_options():
    listOfStates = []
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
        if not(county["State"] in listOfStates):
            listOfStates.append(county["State"])
    options = ""
    for s in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options 

def fun_fact_by_state(state):
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    highest = 0
    lowest = 100
    
    for x in counties:
        if x["State"] == state:
            occupied = x["Housing"]["Housing Units"] / x["Housing"]["Households"]
            occupied = occupied * 10
            if occupied > highest:
                highest = occupied
                highCounty = x["County"]
            elif occupied == 0:
    	        lowest = lowest
            elif occupied < lowest:
                lowest = occupied
                lowCounty = x["County"]
    	
    return "The county with the highest occupancy rate in " + state + " is " + highCounty + " (" + str(highest) + "%)" + " and the county with the lowest occupancy rate in " + state + " is " + lowCounty + " (" + str(lowest) + "%)"

                                   
if __name__=="__main__":
    app.run(debug=False)
