from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

@app.route("/")
def render_main():
    return render_template('home.html', x = get_state_options(counties))
    
def get_state_options(counties):
    listOfStates = list(())
    options = ""
    for x in counties:
        if listOfStates.count(x["State"]) == 0:
            listOfStates.append(x["State"])
            
    for s in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
    return options 
                                   
@app.route("/reponse")
def render_response():
    return render_template('response.html', x = get_state_options(counties))

if __name__=="__main__":
    app.run(debug=False)
