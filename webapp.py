from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

def main():
    

@app.route("/")
def home():
    return render_template('home.html')
    
def get_state_options(counties):
    listOfStates = []
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    for county in counties:
        if not(county["State"]) in listOfStates):
            listOfStates.append(county["State"])
    options = ""
            
    for s in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options 
                                   
@app.route("/reponse")
def render_response():
    return render_template('response.html', x = get_state_options(counties))

if __name__=="__main__":
    app.run(debug=False)
