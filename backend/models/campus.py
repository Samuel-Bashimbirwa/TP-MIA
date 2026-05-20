# Campus Model - Handles database operations for the Campus table (MVC: Model)

class CampusModel:
    @staticmethod
    def get_all_campuses(mysql):
        """
        Retrieves all campuses. Used to load options in dropdowns (Exercise 8)
        and to view active campuses (Exercise 11).
        """
        # Create a Cursor object to interact with the database server
        cur = mysql.connection.cursor()
        
        # Execute SELECT statement on the Campus table
        cur.execute("SELECT * FROM Campus")
        
        # Commit the transaction
        mysql.connection.commit()
        
        # Fetch all campus rows
        campuses = cur.fetchall()
        
        # Close the cursor connection
        cur.close()
        
        return campuses

    @staticmethod
    def add_campus(mysql, campus_name):
        """
        Inserts a new campus into the database (Exercise 11).
        """
        # Create a Cursor object to execute the insert query
        cur = mysql.connection.cursor()
        
        # SQL statement to insert campus name
        sql = "INSERT INTO Campus(campusName) VALUES (%s)"
        
        # Execute insert statement passing sanitized campus name
        cur.execute(sql, (campus_name,))
        
        # Commit transaction to persist changes in the database
        mysql.connection.commit()
        
        # Get count of inserted rows
        rowcount = cur.rowcount
        
        # Close the cursor connection
        cur.close()
        
        return rowcount
