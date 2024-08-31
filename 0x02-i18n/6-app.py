#!/usr/bin/env python3
"""
Flask app with Babel integration, locale selection, and user login emulation.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

class Config:
    """
    Configuration for Flask app and Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    """
    Get a user dictionary or None if the ID is not found or login_as is not passed.
    """
    user_id = request.args.get('login_as')
    if user_id:
        try:
            return users[int(user_id)]
        except (ValueError, KeyError):
            return None
    return None

@babel.localeselector
def get_locale():
    """
    Select the best match language based on the request or user preferences.
    """
    # 1. Check if the locale is specified in the query parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    
    # 2. Check if the user is logged in and has a preferred locale
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user['locale']
    
    # 3. Check the best match from the request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.before_request
def before_request():
    """
    Find a user before processing the request and set it as a global variable.
    """
    g.user = get_user()

@app.route('/')
def index():
    """
    Route for the index page.
    """
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
