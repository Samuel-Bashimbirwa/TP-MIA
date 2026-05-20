# Main Entrypoint - Flask Web Server (MVC: App Bootstrapper)
import sys
import os
# Insert parent folder into path to ensure backend package imports resolve perfectly under any runtime context
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask
from backend.config import init_db

# Initialize Flask with specific directories pointing to the frontend assets and templates
# This enables us to cleanly separate frontend styling/templates from backend logic
app = Flask(
    __name__,
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/templates')),
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend/static'))
)
app.secret_key = "icam_pbl_secret_key"

# Bootstrap Database (MySQL with transparent high-fidelity offline fallback)
mysql, db_status = init_db(app)

# --- ROUTE TO CONTROLLER BINDINGS ---
# We import our controllers containing operational business logic

from backend.controllers import home_controller, exercise_controller, wish_controller, campus_controller

@app.route('/')
def index():
    """Route: / - Fulfills Exercise 1 (Homepage) and Exercise 7."""
    return home_controller.index_route(db_status)

@app.route('/list-items')
def list_items():
    """Route: /list-items - Fulfills Exercise 2 (Dynamic loop list)."""
    return exercise_controller.list_items_route(db_status)

@app.route('/table-squares')
def table_squares():
    """Route: /table-squares - Fulfills Exercise 5 (Table and HTML tags explanation)."""
    return exercise_controller.table_squares_route(db_status)

@app.route('/students')
def students():
    """Route: /students - Fulfills Exercise 3 (Fetch student emails list)."""
    return wish_controller.students_route(mysql, db_status)

@app.route('/student-campuses')
def student_campuses():
    """Route: /student-campuses - Fulfills Exercise 4 (Fetch student & campus names JOIN)."""
    return wish_controller.student_campuses_route(mysql, db_status)

@app.route('/table-db')
def table_db():
    """Route: /table-db - Fulfills Exercise 6 (Database records inside styled table)."""
    return wish_controller.table_db_route(mysql, db_status)

@app.route('/list')
def list_wishes():
    """Route: /list - Fulfills Exercise 7 dynamic database listing menu option."""
    return wish_controller.list_route(mysql, db_status)

@app.route('/dashboard')
def dashboard():
    """Route: /dashboard - Fulfills Exercise 7 administration panel hub."""
    return wish_controller.dashboard_route(mysql, db_status)

@app.route('/add')
def add():
    """Route: /add - Fulfills Exercise 8 wish input form with database dropdown."""
    return wish_controller.add_route(mysql, db_status)

@app.route('/addsave')
def addsave():
    """Route: /addsave - Fulfills Exercises 9 and 10 forms displaying and DB insertion."""
    return wish_controller.addsave_route(mysql, db_status)

@app.route('/add-campus')
def add_campus():
    """Route: /add-campus - Fulfills Exercise 11 campus input form."""
    return campus_controller.add_campus_route(mysql, db_status)

@app.route('/add-campus-save')
def add_campus_save():
    """Route: /add-campus-save - Fulfills Exercise 11 campus database insertion."""
    return campus_controller.add_campus_save_route(mysql, db_status)

# Standard startup trigger
if __name__ == '__main__':
    # Starts the web application server
    app.run(debug=True)
