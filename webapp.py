from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json 

app = Flask(__name__)

def main():
    with open('county_demographics.json') as song_data:
        counties = json.load(demographics_data)

@app.route("/")
def render_main():
        get_state_options(counties)
        return render_template('home.html', x = options)
    
def get_state_options(counties):
    listOfStates = list(())
    for x in counties:
        if listOfStates.count(x["State"]) == 0:
            listOfStates.append(x["State"])
    		
    options = ""
    for s in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>"
    return options
                                   
@app.route("/reponse")
def render_response(options)
    return render_template('response.html')

if __name__=="__main__":
    app.run(debug=False)
