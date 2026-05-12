# implement a basic notification system

# I want an interface / abstract class of Notification
# abstractmethod --> send(self, message)
from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass

# 2. two concrete implementations of this class

# EmailNotification class
class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f"The message '{message}' was successfullly sent to {self.email}")


# SMSNotification class
class SMSNotification(Notification):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        print(f"The message '{message}' was successfullly sent to {self.phone_number}")

# 3. then use them here
emailNotif = EmailNotification("mail@gmail.com")
smsNotif = SMSNotification("438 555 6666")

emailNotif.send("Hi, this is my email test msg")
smsNotif.send("Hi, this is my sms test msg")