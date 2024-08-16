from flask import request, render_template, Blueprint, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, login_required, current_user
from .models import *
from functools import wraps
from . import db
from datetime import datetime
import os

main_bp = Blueprint('main', __name__)

#landing home page
@main_bp.route('/')
def signin():
    '''
    This function renders the signin page
    '''
    music = {"name": "music", "singer": "sayani"}
    username = "rishav"
    return render_template('home.html', music=music, username=username)