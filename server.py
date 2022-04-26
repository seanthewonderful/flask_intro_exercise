"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = [
  'lame', 'dweebish', 'non-too-smart', 'ugly', 'really ugly', 'dumb as dirt',
  'unfortunate to behold', 'the punchline of a joke', 'a sad, strange little man'
]


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html>
    <html>
    Hi! This is the home page.
    <a href="http://localhost:5555/hello">Say Hello</a>
    <a href="http://localhost:5555/diss">Get Dissed</a>
    </html>
    """


@app.route('/diss')
def diss():
      return """
      <!doctype html>
      <html>
        <head>
          <title>Hi There!</title>
        </head>
        <body>
          <h1>Hi There!</h1>
          <form action="/dissed">
            What's your name? <input type="text" name="person">
            <label for="disses">Choose a diss</label>
            <select name="disses">
              <option value="">--Choose wisely--</option>
              {% for diss in disses %}
                <option value="{diss}">{diss}</option>
              {% endfor %}
            </select>
            <input type="submit" value="Submit">
          </form>
        </body>
      </html>
      """
    

@app.route('/dissed')
def dissed():
    player = request.args.get("person")

    diss = request.args.get("disses")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""
    
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <label for="compliments">Choose a compliment</label>
          <select name="compliments">
            <option value="">--Choose wisely--</option>
            <option value="{AWESOMENESS[0]}">{AWESOMENESS[0].title()}</option>
            <option value="{AWESOMENESS[1]}">{AWESOMENESS[1].title()}</option>
            <option value="{AWESOMENESS[2]}">{AWESOMENESS[2].title()}</option>
            <option value="{AWESOMENESS[3]}">{AWESOMENESS[3].title()}</option>
            <option value="{AWESOMENESS[4]}">{AWESOMENESS[4].title()}</option>
            <option value="{AWESOMENESS[5]}">{AWESOMENESS[5].title()}</option>
            <option value="{AWESOMENESS[6]}">{AWESOMENESS[6].title()}</option>
            <option value="{AWESOMENESS[7]}">{AWESOMENESS[7].title()}</option>
            <option value="{AWESOMENESS[8]}">{AWESOMENESS[8].title()}</option>
            <option value="{AWESOMENESS[9]}">{AWESOMENESS[9].title()}</option>
            <option value="{AWESOMENESS[10]}">{AWESOMENESS[10].title()}</option>
            <option value="{AWESOMENESS[11]}">{AWESOMENESS[11].title()}</option>
            <option value="{AWESOMENESS[12]}">{AWESOMENESS[12].title()}</option>
            <option value="{AWESOMENESS[13]}">{AWESOMENESS[13].title()}</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliments")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0", port=5555)
