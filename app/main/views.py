from flask import render_template,request,redirect,url_for,abort
from ..models import Comment,User,Pitch
# We may also use the import * command to import all objects from a specific module e.g from ..models import *
# ,get_pitch,get_comments
from . import main
from .forms import CommentForm, PitchForm,UpdateProfile
from flask_login import login_required, current_user
from .. import db,photos
import markdown2


def save_pitch(pitch):
    Pitch.save_pitch(pitch)

@main.route('/')

def index():
    pitches = Pitch.query.order_by(Pitch.posted.desc()).all()
    '''
    my index page
    :return:
    '''
    return render_template('index.html', pitches=pitches )

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

