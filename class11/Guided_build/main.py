from course import Course
from status import CourseStatus

course1 = Course("Advanced Programming", 30, CourseStatus.OPEN)
course2 = Course("Web Interface Programming 2", 25, CourseStatus.CLOSED)

course1.display_info()
course2.display_info()

course1.close_registration()
course1.display_info()

course2.reopen_course()
course2.display_info()

try:
    course3 = Course("Testing techinques", 20, "open")
except ValueError as e:
    print("Error:", e)

try:
    course3 = Course("Testing techinques - 2nd attempt", 20, CourseStatus.OPEN)
except ValueError as e:
    print("Error:", e)

course3.display_info()