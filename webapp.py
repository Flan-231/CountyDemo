from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

@app.route("/")
def render_main():
    get_state_options()
    return render_template('home.html', x = options)

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

def get_state_options():
    listOfStates = list(())
    for x in counties:
        if listOfStates.count(x["State"]) == 0:
            listOfStates.append(x["State"])
    		
    options = ""
    for x in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
    	
if __name__=="__main__":
    app.run(debug=False)
