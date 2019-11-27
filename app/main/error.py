from flask import render_template

from . import main

@main.errorhandler(404)
def notfound(error):
    '''
    function to render the 404 error page
    '''
    return render_template('notfound.html'),404



