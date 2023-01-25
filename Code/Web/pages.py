from flask import Blueprint, render_template, request, redirect, url_for
import os 
from instaloader import *
import pandas as pd  

pages = Blueprint('pages', __name__)

@pages.route("/", methods = ["GET","POST"])
def index():
    #If the user has submitted their username, send them over to other page 
    if request.method == "POST": 
        return redirect(url_for('pages.showBaseData'))
    else: 
        return render_template("index.html")