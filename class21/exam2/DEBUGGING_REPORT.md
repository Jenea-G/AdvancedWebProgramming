## Application start fail

**File:**  
app.py

**Problem:**  
What was incorrect?

- wrong key name in db address configuration: app.config["SQLALCHEMY_DATABASE_URL"]
- icorrect db initialization in line 17: "db = SQLAlchemy"
- missing parentheses in app.app_context

  **Fix:**  
  What did you change?

- changed the key name to "SQLALCHEMY_DATABASE_URI"
- created a db object with app as an argument, as we create db for this app: "db = SQLAlchemy(app)"
- added parentheses in line 60: "app.app_context()"

**Test:**  
How did you confirm that it worked?

## Bug title

**File:**  
Name of the file.

**Problem:**  
What was incorrect?

**Fix:**  
What did you change?

**Test:**  
How did you confirm that it worked?
