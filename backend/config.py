from flask_mysqldb import MySQL

# Module-level definitions for global configuration variables to satisfy linters
mysql = None
db_status = None

# In-Memory Database emulation class to allow 100% offline functionality
class MockConnection:
    # Class-level variables persist data across web requests
    # Set exact data structures and default values from your phpMyAdmin SQL dump
    _campuses = [
        (3, 'Douala'),
        (4, 'Kinshasa'),
        (1, 'Lille'),
        (2, 'Nantes'),
        (6, 'Paris-Sénart'),
        (5, 'Toulouse')
    ]
    _wishes = [
        (19, 'céline@icam.fr', 1),
        (3, 'david@icam.fr', 1),
        (16, 'jean-luc@icam.fr', 2),
        (21, 'jean-michel@icam.fr', 2),
        (22, 'jean@icam.fr', 3),
        (12, 'junie@icam.fr', 1),
        (7, 'marie@icam.fr', 1),
        (1, 'michel@icam.fr', 1),
        (23, 'nicolas@icam.fr', 2),
        (2, 'pierre@icam.fr', 2),
        (4, 'tanguy@icam.fr', 2)
    ]

    def cursor(self):
        return MockCursor(self)

    def commit(self):
        pass

    def close(self):
        pass

class MockCursor:
    def __init__(self, connection):
        self.connection = connection
        self.results = []
        self.rowcount = 0

    def execute(self, sql, params=None):
        sql_upper = sql.upper().strip()
        
        # 1. Select student emails (TP3)
        # We query the MobilityWish table. Row 1 (index 1) contains studentMail.
        if "SELECT * FROM MOBILITYWISH" in sql_upper or "SELECT * FROM `MOBILITYWISH`" in sql_upper:
            self.results = self.connection._wishes
            self.rowcount = len(self.results)
            
        # 2. Select campuses dropdown options (TP8)
        elif "SELECT * FROM CAMPUS" in sql_upper or "SELECT * FROM `CAMPUS`" in sql_upper:
            self.results = self.connection._campuses
            self.rowcount = len(self.results)
            
        # 3. Select wishes and campuses joined (TP4, TP6, TP7)
        # Executing JOIN query matching Exercise 4
        elif "SELECT" in sql_upper and "MOBILITYWISH" in sql_upper and "CAMPUS" in sql_upper:
            res = []
            for wish in self.connection._wishes:
                campus_name = "Unknown"
                for c in self.connection._campuses:
                    if c[0] == int(wish[2]): # wish[2] is Campus_idCampus
                        campus_name = c[1]
                        break
                res.append((wish[1], campus_name)) # wish[1] is studentMail
            self.results = res
            self.rowcount = len(self.results)
            
        # 4. Insert mobility wish (TP10)
        # INSERT INTO MobilityWish(studentMail, Campus_idCampus) VALUES (%s, %s)
        elif "INSERT INTO MOBILITYWISH" in sql_upper:
            if params:
                student_mail, campus_id = params[0], int(params[1])
                # Check for duplicates in mock
                exists = any(w[1] == student_mail and w[2] == campus_id for w in self.connection._wishes)
                if not exists:
                    new_id = len(self.connection._wishes) + 1
                    # In mock dataset we insert: (idMobilityWish, studentMail, Campus_idCampus)
                    self.connection._wishes.append((new_id, student_mail, campus_id))
                self.rowcount = 1
                
        # 5. Insert new campus (TP11)
        elif "INSERT INTO CAMPUS" in sql_upper:
            if params:
                campus_name = params[0]
                new_id = len(self.connection._campuses) + 1
                self.connection._campuses.append((new_id, campus_name))
                self.rowcount = 1
        else:
            self.results = []
            self.rowcount = 0

    def fetchall(self):
        return self.results

    def close(self):
        pass

class MockMySQL:
    def __init__(self):
        self.connection = MockConnection()

def init_db(app):
    global mysql, db_status
    
    # List of database names to try: 'PBLMIA11' (matching the SQL dump) and 'MIAPBL11-STUDENT' (from the instructions)
    db_names = ['PBLMIA11', 'MIAPBL11-STUDENT']
    connected = False
    
    # Initialize Flask-MySQLdb once
    mysql = MySQL(app)
    
    for db_name in db_names:
        try:
            print(f"[DB] Attempting connection to local MySQL database '{db_name}'...")
            app.config['MYSQL_HOST'] = '127.0.0.1'
            app.config['MYSQL_USER'] = 'root'
            app.config['MYSQL_PASSWORD'] = ''
            app.config['MYSQL_DB'] = db_name
            
            # Accessing the connection within app context triggers verification
            with app.app_context():
                conn = mysql.connect
                cursor = conn.cursor()
                cursor.execute("SELECT 1")
                cursor.close()
                
            db_status = "MySQL Server"
            print(f"[DB] Local MySQL database connection to '{db_name}' successfully established!")
            connected = True
            break
        except Exception as e:
            print(f"[DB] Connection to database '{db_name}' was unsuccessful: {e}")
            
    if not connected:
        print("[DB] Local database unreachable. Using mock database fallback.")
        db_status = "SQLite Mock"
        mysql = MockMySQL()
        
    return mysql, db_status

