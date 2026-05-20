# Home Controller - Manages the portal's index/root operations (MVC: Controller)
from flask import render_template

def index_route(db_status):
    """
    Renders the beautiful glassmorphic home page welcoming the user.
    Fulfills Exercise 1 by mapping '/' to index function returning the welcome code.
    """
    # Return the rendered HTML template page via Jinja2
    return render_template('index.html', db_status=db_status)
