from course import Course
from status import CourseStatus
from delivery import DeliveryMode

course1 = Course("Advanced Programming", 30, CourseStatus.OPEN, DeliveryMode.ONLINE)
course2 = Course("Web Interface Programming 2", 25, CourseStatus.CLOSED, DeliveryMode.IN_PERSON)

course1.display_info()
course2.display_info()

course1.close_registration()
course1.display_info()
print("========")
try:
    course2.reopen_course()
except ValueError as e:
    print("Error:", e)
course2.display_info()
print("========")

try:
    course3 = Course("Testing techinques", 20, "open", DeliveryMode.HYBRID)
except ValueError as e:
    print("Error:", e)

try:
    course3 = Course("Testing techinques - 2nd attempt", 20, CourseStatus.OPEN, DeliveryMode.ONLINE)
except ValueError as e:
    print("Error:", e)

course3.display_info()

try:
    course4 = Course("Testing techinques - 3", 61, CourseStatus.OPEN, DeliveryMode.IN_PERSON)
except ValueError as e:
    print("Error:", e)

try:
    course4 = Course("Testing techinques - 3", 0, CourseStatus.OPEN, DeliveryMode.IN_PERSON)
except ValueError as e:
    print("Error:", e)

try:
    course4 = Course("Valid capacity", 18, CourseStatus.OPEN, DeliveryMode.IN_PERSON)
except ValueError as e:
    print("Error:", e)

course4.display_info()

try:
    course5 = Course("Testing delivery", 22, CourseStatus.OPEN, "online")
except ValueError as e:
    print("Error:", e)

try:
    course5 = Course("Testing delivery", 22, CourseStatus.OPEN, DeliveryMode.ONLINE)
except ValueError as e:
    print("Error:", e)

course5.display_info()

print("===== Test reopen_course method validation ===== ")
course2.cancel_course()
course2.display_info()

try:
    course2.reopen_course()

except ValueError as e:
    print("Error:", e)

print(course2.is_open_for_registration())
print(course5.is_open_for_registration())

print("=== challenge 4 ===")
try:
    bad_course = Course("Bad Course", 20, "open", "online")
    bad_course.display_info()
except ValueError as e:
    print("Error:", e)

try:
    bad_course = Course("Bad Course", 20, CourseStatus.OPEN, "online")
    bad_course.display_info()
except ValueError as e:
    print("Error:", e)

try:
    bad_course = Course("Not that bad Course", 20, CourseStatus.OPEN, DeliveryMode.IN_PERSON)
    bad_course.display_info()
except ValueError as e:
    print("Error:", e)