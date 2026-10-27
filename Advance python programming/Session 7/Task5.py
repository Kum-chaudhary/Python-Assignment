class notification:
    def send(self):
        print("Sending notification")

class EmailNotification(notification):
    def send(self):
        print("Sending Email notification")

class SMSNotification(notification):
    def send(self):
        print("sending sms notification")

obj1 = EmailNotification()
obj2 = SMSNotification()

obj1.send()
obj2.send()