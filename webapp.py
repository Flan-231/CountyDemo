from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

@app.route("/")
def home():
    render_template('home.html', options=get_state_options())

@app.route("/fact")
def fact():
    state = request.args['state']
    return render_template('reponse.html', funFact = fun_fact_by_state(state))
    
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
    first_county = "ZZZZZZZ"
    for county in counties: 
        if county["County"] < first_county and county ["State"] == state:
            first_county = county["County"]
    return first_county 
                                   
if __name__=="__main__":
    app.run(debug=False)
