from flask import Flask, request, Markup, render_template, flash, Markup, os, json 

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html') 

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)

def get_state_options():
    listOfStates = thislist(())
    for x in counties:
        if listOfStates.count(x["State"]) == 0:
            listOfStates.append(x["State"])
    		
    options = ""
    for x in listOfStates:
        options = options + Markup("<option value=\"" + s + "\">" + s + "</option>")
	
    return render_template('response.html', states = options)
    	
if __name__=="__main__":
    app.run(debug=False)
