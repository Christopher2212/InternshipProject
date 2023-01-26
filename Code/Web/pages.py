from flask import Blueprint, render_template, request, redirect, url_for
import os 
from instaloader import *
import pandas as pd  
from Web import mapping 
 
pages = Blueprint('pages', __name__)

@pages.route("/", methods = ["GET","POST"])
def index():
    mapping.makeNetwork("S:\InternshipProject\Other\EdgeandVertListsCSV\BangkokVert.csv","S:\InternshipProject\Other\EdgeandVertListsCSV\BangkokEdge.csv","nodeMap.html")
    #If the user has submitted their username, send them over to other page 
    return render_template("templates/nodeMap.html")