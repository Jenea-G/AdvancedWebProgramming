# Exceptions

# raise ValueError("This is incorrect")

# number = int("Hello") # this will raise valueError
# python cannot convert hello into integer
# number = int("2") # would be possible

# What is an exception?
# is an error signal that interrupts normal execution.

# something unexpected happened.
# normal execution cannot continue here ** safely **

# not every problem should be handled the same way!

# IMPORTANT: Exceptional situations need to be handled, before they break the code!

def set_gpa(value):
    if value < 0 or value > 4:
        print ("Invalid GPA")

# this /\ would be weak:

#   it signals a problem, but doesnt force the caller to handle it
#   the program may continue in a bad state
#   the error is easier to ignore

def set_gpa(value):
    if value < 0 or value > 4:
        raise ValueError("Invalid GPA")
    
# now, the caller must deal with the problem or the program stops clearly.
# this is the better desin

