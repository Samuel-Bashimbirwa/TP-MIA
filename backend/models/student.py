# Student Model - Handles database operations for the Student table (MVC: Model)

class StudentModel:
    @staticmethod
    def get_all_students(mysql):
        """
        Retrieves all students from the database.
        Equivalent to Exercise 3 database execution logic.
        """
        # Create a Cursor object to interact with the database server
        cur = mysql.connection.cursor()
        
        # Execute the SQL SELECT statement on the MobilityWish table
        cur.execute("SELECT * FROM MobilityWish")
        
        # Commit changes to register transaction state
        mysql.connection.commit()
        
        # Fetch all results returned by the query
        students = cur.fetchall()
        
        # Close the cursor connection to release resources
        cur.close()
        
        return students
