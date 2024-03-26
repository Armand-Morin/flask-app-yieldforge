# -*- encoding: utf-8 -*-

import os
from flask_minify import Minify
from flask import Flask, render_template, request
from jinja2 import TemplateNotFound

app = Flask(__name__, template_folder='templates')

class Config(object):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = (os.getenv('DEBUG', 'False') == 'True')
    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')
    SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_9999')

app.config.from_object(Config)

DEBUG = app.config['DEBUG']

if not DEBUG:
    Minify(app=app, html=True, js=False, cssless=False)

app.logger.info('DEBUG = ' + str(DEBUG))
app.logger.info('Page Compression = ' + ('FALSE' if DEBUG else 'TRUE'))
app.logger.info('ASSETS_ROOT = ' + app.config['ASSETS_ROOT'])

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/', defaults={'page_path': 'index.html'})
@app.route('/<path:page_path>')
def index(page_path):
    try:
        segment = get_segment(request)
        # Serve the file (if exists) from templates/home/FILE.html
        return render_template('home/' + page_path, segment=segment)
    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

def get_segment(request): 
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index.html'
        return segment    
    except Exception as e:
        app.logger.error(f"Error getting segment: {e}")
        return 'index.html' 

if __name__ == "__main__":
    app.run()
