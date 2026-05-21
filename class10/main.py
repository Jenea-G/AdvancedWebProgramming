from student_record import StudentRecord
from course_section import CourseSection

s1 = StudentRecord("Mary", 4, 35)
s1.display_info()

try:
    s1.update_gpa(5.0)
except ValueError as e:
    print("Error:", e)

try:
    s2 = StudentRecord("Pete", -1, 0)
except ValueError as e:
    print("Error:", e)

try:
    s2 = StudentRecord(" ", 3, 0)
except ValueError as e:
    print("Error:", e)

try:
    s2 = StudentRecord("Pete", 3, -1)
except ValueError as e:
    print("Error:", e)

s2 = StudentRecord("Peter", 2, 10)
s2.display_info()

try:
    s2.add_credits(40)
except ValueError as e:
    print("Error:", e)

try:
    s2.credits = -2
except ValueError as e:
    print("Error:", e)

s2.display_info()

try:
    cs1 = CourseSection("Web dev", 24)
except ValueError as e:
    print("Error:", e)

try:
    cs2 = CourseSection("", 30, 2)
except ValueError as e:
    print("Error:", e) 

try:
    cs2 = CourseSection("Design web", 0)
except ValueError as e:
    print("Error:", e) 

try:
    cs2 = CourseSection("Design web", 30, -1)
except ValueError as e:
    print("Error:", e) 


