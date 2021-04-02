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
    def high_income_counties(counties):
        """Return a LIST of the counties with a median household income over $90,000."""
        y = []
        for x in counties:
            if x["Income"]["Median Houseold Income"] > 90000:
                addCounty = x["County"]
                y.append(addCounty)
        return y
                                   
if __name__=="__main__":
    app.run(debug=False)
