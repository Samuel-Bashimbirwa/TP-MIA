# Wish Model - Handles database operations for the MobilityWish table (MVC: Model)

class WishModel:
    @staticmethod
    def get_all_wishes_with_campus(mysql):
        """
        Retrieves all mobility wishes joined with their respective campus name.
        Matches SQL JOIN logic for Exercises 4, 6 and 7.
        """
        # Create a Cursor object to interact with the database server
        cur = mysql.connection.cursor()
        
        # SQL statement performing a JOIN to fetch studentMail and campusName
        sql = """
            SELECT MobilityWish.studentMail, Campus.campusName 
            FROM MobilityWish 
            JOIN Campus ON MobilityWish.Campus_idCampus = Campus.idCampus
        """
        
        # Execute query
        cur.execute(sql)
        
        # Commit query transaction
        mysql.connection.commit()
        
        # Fetch all results returned by the JOIN query
        wishes = cur.fetchall()
        
        # Close the cursor connection
        cur.close()
        
        return wishes

    @staticmethod
    def add_mobility_wish(mysql, student_mail, campus_id):
        """
        Inserts a student mobility choice (wish) into the database.
        Matches the database saving logic from Exercise 10.
        """
        # Create a Cursor object to execute the insert query
        cur = mysql.connection.cursor()
        
        # SQL query to insert values
        sql = "INSERT INTO MobilityWish(studentMail, Campus_idCampus) VALUES (%s, %s)"
        
        # Values tuple retrieved from the input form
        val = (student_mail, campus_id)
        
        # Execute insert statement passing parameterized arguments
        cur.execute(sql, val)
        
        # Commit transaction to persist changes in database
        mysql.connection.commit()
        
        # Count of rows inserted (should be 1)
        rowcount = cur.rowcount
        
        # Close the cursor connection
        cur.close()
        
        return rowcount
