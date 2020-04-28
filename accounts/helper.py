from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import string
import random
import threading


def email_auth_num():
    LENGTH = 8
    string_pool = string.ascii_letters + string.digits
    auth_num = ""
    for i in range(LENGTH):
        auth_num += random.choice(string_pool)
    return auth_num

class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html):
        self.subject = subject
        self.body = body
        self.from_email = from_email
        self.recipient_list = recipient_list
        self.fail_silently = fail_silently
        self.html = html
        threading.Thread.__init__(self)

        
    def run (self):
        msg = EmailMultiAlternatives(self.subject,self.body,self.from_email,self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html,"text/html")
        msg.send(self.fail_silently)

def send_mail(subject,recipient_list,body='',from_email='rkgnsp03@gmail.com',fail_silently=False,html=None,*args,**kwargs):
    EmailThread(subject,body,from_email,recipient_list,fail_silently,html).start()