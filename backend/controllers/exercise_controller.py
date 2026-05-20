# Exercise Controller - Manages static operations for TP2 and TP5 (MVC: Controller)
from flask import render_template

def list_items_route(db_status):
    """
    Renders the static list of items.
    Fulfills Exercise 2.
    """
    # Line 1: Define route function to list static items.
    # Line 2: The controller receives the database status.
    # Line 3: It calls render_template to render 'list_items.html'.
    # Line 4: It passes the db_status to keep the nav bar updated.
    # Line 5: The rendered HTML is returned to Flask, which serves it to the browser.
    return render_template('list_items.html', db_status=db_status)

def table_squares_route(db_status):
    """
    Renders the HTML table of squares and explains table elements.
    Fulfills Exercise 5.
    """
    # Line 1: Define route function for squares table.
    # Line 2: In standard MVC, calculations can be passed down or handled in the view.
    # Line 3: The controller hands off the view generation to 'table_squares.html'.
    # Line 4: The view dynamically loops through numbers 1 to 4 and squares them.
    # Line 5: It displays a section explaining the tags: <table>, <tr>, <th>, and <td>.
    return render_template('table_squares.html', db_status=db_status)
