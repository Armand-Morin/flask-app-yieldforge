# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask   import render_template, request
from jinja2  import TemplateNotFound

from apps import app

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    try:
        segment = get_segment(request)
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template( 'home/' + path, segment=segment )
    
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

def get_segment( request ): 
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment    
    except:
        return None  
