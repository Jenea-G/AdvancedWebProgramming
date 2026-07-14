## Application start fail

**File:**  
app.py

**Problem:**

- wrong key name in db address configuration: app.config["SQLALCHEMY_DATABASE_URL"]
- icorrect db initialization in line 17: "db = SQLAlchemy"
- missing parentheses in app.app_context

**Fix:**

- changed the key name to "SQLALCHEMY_DATABASE_URI"
- created a db object with app as an argument, as we create db for this app: "db = SQLAlchemy(app)"
- added parentheses in line 60: "app.app_context()"

**Test:**  
Successfully started the app by running: "flask --app app run --debug "

## BuildError: Could not build url for endpoint 'albums' and 'add'

**File:**  
base.html

**Problem:**  
Nonexistent 'albums' and 'add' functions

- href="{{ url_for('albums') }}"> All Albums </a>
- href="{{ url_for('add') }}"> Add Album </a>

**Fix:**  
added correct names for existing functions/endpoints index() and add_album()

**Test:**  
No more buildError showing, the index page is displaying "No albums have been added." as expected and add_album button loads the form.

## Failed to add and display an album

**File:**  
app.py add_album.html

**Problem:**  
in app.py "/albums/add" route was missing "POST" method and the created album wasn't added to the db thus we commited nothing
in add_album template the method in the form was "GET" not "POST" which didnt sent data to the db.

**Fix:**  
added POST to the "/albums/add" route and to the form.

**Test:**  
Filled in the form and added an album, checked if it appeared in the page

## Failed to edit album

**File:**  
app.py edit_album.html

**Problem:**  
Empty fields of edit form, changes were not saved.

in app.py incorrect template attached to edit_album, wrong redirect point, wrong field name (request.form["amount"]), no commit to db
in edit_album.html nonexistent album attributes "name", "band", and field name - "quantity"

**Fix:**  
in app.py returned correct template "add_album.html" and redirected to "index.html"
corrected the attributes and added db.session.commit()
in edit_album.html renamed attributes "name" and "band" to "title" and "artist", and field name "quantity" to "stock"

**Test:**  
Filled in the form and added an album, checked if it appeared in the page

## Failed to delete album: The method is not allowed for the requested URL.

**File:**  
app.py

**Problem:**  
In app.py "/albums/<int:album_id>/delete" route "GET" method is not allowed, whithout commit changes are not saved to the database

**Fix:**  
Removed method, added db.session.commit()

**Test:**
Tesed by deleting a few albums that were successfully removed.
