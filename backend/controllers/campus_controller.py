# Campus Controller - Manages adding new campuses (MVC: Controller)
from flask import render_template, request
from backend.models.campus import CampusModel

def add_campus_route(mysql, db_status):
    """
    Renders the campus registration page listing currently available campuses.
    Fulfills Exercise 11.
    """
    try:
        # Load all campuses from database
        campus_rows = CampusModel.get_all_campuses(mysql)
        return render_template('add_campus.html', campus_rows=campus_rows, db_status=db_status)
    except Exception as e:
        return render_template('add_campus.html', campus_rows=[], error=str(e), db_status=db_status)

def add_campus_save_route(mysql, db_status):
    """
    Handles registering new campus location submitted from the campus form.
    Fulfills Exercise 11 database insertion.
    """
    # Retrieve campus name from GET URL query parameters
    campus_name = request.args.get('campus_name')
    
    success_message = None
    error = None
    
    if campus_name:
        try:
            # Insert new campus into table and commit changes
            rows_inserted = CampusModel.add_campus(mysql, campus_name)
            success_message = f"Campus location '{campus_name}' ({rows_inserted} row) registered!"
        except Exception as e:
            error = str(e)
            
    # Load all campuses again to render dynamic listing table
    try:
        campus_rows = CampusModel.get_all_campuses(mysql)
    except Exception as e:
        campus_rows = []
        error = str(e)
        
    return render_template('add_campus.html',
                           campus_rows=campus_rows,
                           success_message=success_message,
                           error=error,
                           db_status=db_status)
