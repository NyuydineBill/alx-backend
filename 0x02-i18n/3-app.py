#!/usr/bin/env python3
"""
Flask app with Babel integration and locale selection.
"""

from flask import Flask, render_template, request
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

@babel.localeselector
def get_locale():
    """
    Select the best match language based on the request.
    """
<<<<<<< HEAD
    # Check if the locale is specified in the query parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
=======
>>>>>>> dc61a8d0a1b2e93f036ba2090f093f2ae0b420a9
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Route for the index page.
    """
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
