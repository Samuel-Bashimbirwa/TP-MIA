# Wish Controller - Manages DB Student listings and Mobility Wish creations (MVC: Controller)
from flask import render_template, request
from backend.models.student import StudentModel
from backend.models.campus import CampusModel
from backend.models.wish import WishModel

def students_route(mysql, db_status):
    """
    Renders registered student emails.
    Fulfills Exercise 3. Contains detailed line-by-line comments for index().
    """
    # Line 1: Define students route function receiving MySQL database instance and connection status.
    # Line 2: Initialize query execution with a try-except block to catch connection errors.
    try:
        # Line 3: Invoke the StudentModel's static query handler to get student table rows.
        student_rows = StudentModel.get_all_students(mysql)
        # Line 4: Call render_template to output 'students.html' containing the database emails.
        # Line 5: Return the compiled view template with student rows and database state.
        return render_template('students.html', student_rows=student_rows, db_status=db_status)
    except Exception as e:
        # Line 6: In case of SQL connection failures, catch exception details.
        # Line 7: Hand off to view passing the error details to alert the user.
        return render_template('students.html', student_rows=[], error=str(e), db_status=db_status)

def student_campuses_route(mysql, db_status):
    """
    Renders student emails and their selected campuses in an ordered list.
    Fulfills Exercise 4.
    """
    try:
        # Fetch wishes joined with campuses names using the Wish model
        wish_rows = WishModel.get_all_wishes_with_campus(mysql)
        return render_template('student_campuses.html', wish_rows=wish_rows, db_status=db_status)
    except Exception as e:
        return render_template('student_campuses.html', wish_rows=[], error=str(e), db_status=db_status)

def table_db_route(mysql, db_status):
    """
    Renders student emails and selected campuses inside an HTML table layout.
    Fulfills Exercise 6.
    """
    try:
        # Fetch joined records and serve inside the table template
        wish_rows = WishModel.get_all_wishes_with_campus(mysql)
        return render_template('table_db.html', wish_rows=wish_rows, db_status=db_status)
    except Exception as e:
        return render_template('table_db.html', wish_rows=[], error=str(e), db_status=db_status)

def list_route(mysql, db_status):
    """
    Renders the '/list' menu target.
    Fulfills Exercise 7. Shows dynamic list in styled table format.
    """
    # Return table_db view inside Exercise 7 menu context
    return table_db_route(mysql, db_status)

def dashboard_route(mysql, db_status):
    """
    Renders the unified administration panel.
    Fulfills Exercise 7.
    """
    try:
        # Query metrics dynamically to show live statistics
        students_count = len(StudentModel.get_all_students(mysql))
        campuses_count = len(CampusModel.get_all_campuses(mysql))
        wishes_count = len(WishModel.get_all_wishes_with_campus(mysql))
        
        return render_template('dashboard.html', 
                               stat_students=students_count, 
                               stat_campuses=campuses_count, 
                               stat_wishes=wishes_count, 
                               db_status=db_status)
    except Exception as e:
        return render_template('dashboard.html', 
                               stat_students=0, 
                               stat_campuses=0, 
                               stat_wishes=0, 
                               db_status=db_status)

def add_route(mysql, db_status):
    """
    Renders the form allowing wishes input.
    Fulfills Exercise 8.
    """
    try:
        # Load all campuses from database to populate options dropdown list
        campus_rows = CampusModel.get_all_campuses(mysql)
        return render_template('add_wish.html', campus_rows=campus_rows, db_status=db_status)
    except Exception as e:
        return render_template('add_wish.html', campus_rows=[], error=str(e), db_status=db_status)

def addsave_route(mysql, db_status):
    """
    Handles form submission from Exercise 8.
    Fulfills Exercises 9 and 10 (Displays submitted values & inserts in DB).
    """
    # Retrieve parameters submitted via GET method in the URL
    student_email = request.args.get('student')
    campus_choice_id = request.args.get('choice')
    
    success_message = None
    error = None
    
    if student_email and campus_choice_id:
        try:
            # Insert wish into database and commit (Exercise 10)
            rows_inserted = WishModel.add_mobility_wish(mysql, student_email, campus_choice_id)
            success_message = f"{rows_inserted} wish record successfully inserted in the database!"
        except Exception as e:
            error = str(e)
            
    # Reload campuses lists for re-rendering the form page
    try:
        campus_rows = CampusModel.get_all_campuses(mysql)
    except Exception as e:
        campus_rows = []
        error = str(e)
        
    return render_template('add_wish.html', 
                           campus_rows=campus_rows, 
                           student_email=student_email, 
                           campus_id=campus_choice_id, 
                           success_message=success_message, 
                           error=error,
                           db_status=db_status)
