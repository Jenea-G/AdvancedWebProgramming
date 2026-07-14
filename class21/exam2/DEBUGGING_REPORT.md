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
Successfully started the app by running: "flask --app app run --debug "

## BuildError: Could not build url for endpoint 'albums' and 'add'

**File:**  
base.html

**Problem:**  
What was incorrect?
We dint create albums and add functions

- <a href="{{ url_for('albums') }}"> All Albums </a>
- <a href="{{ url_for('add') }}"> Add Album </a>

**Fix:**  
What did you change?
added correct names for existing functions index() and add_album()

**Test:**  
How did you confirm that it worked?
No more buildError showing, the index page is displaying "No albums have been added." as expected and add_album button shows the form
