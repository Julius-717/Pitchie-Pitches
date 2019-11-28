from flask import render_template

from . import main


@main.errorhandler(404)
def not_found(error):
    '''
    function to render the 404 error page
    '''
    return render_template('not_found.html'), 404
