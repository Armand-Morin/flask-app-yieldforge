# -*- encoding: utf-8 -*-

import os
from flask import Flask
from .config import Config
from apps import views

app = Flask(__name__)

app.config.from_object( Config ) 


