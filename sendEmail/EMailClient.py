import os
import smtplib
import imghdr
from email.message import EmailMessage
from sendEmail import template_reader
from bs4 import BeautifulSoup
import json
import re

class GMailClient:
    def sendEmail(self,contacts):
        #EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        #EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
        EMAIL_ADDRESS = 'obulgudachatbot@gmail.com'
        EMAIL_PASSWORD = '7032813306'

        print(contacts);
        msg = EmailMessage()
        msg['Subject'] = 'Detailed Covid-19 Report!'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = contacts[2]
        value = contacts[3]
        print(value)
        #values = value.get("cases")
        values = value.get("Bot")
        print(values)
        msg.set_content("Hello Mr. {} Here is your Covid 19 Report PFA".format(contacts[0]))
        #print(contacts[2])
        template = template_reader.TemplateReader()
        email_message = template.read_course_template("simple")
        #print(email_message)
        country_name1 = "India"
        '''total1 = str(values.get("total"))
        new1 = str(values.get("new"))
        active1 = str(values.get("active"))
        critical1 = str(values.get("critical"))
        recovered1 = str(values.get("recovered"))
        print(new1 + total1)'''
        Dict = values.split('\n')
        newdict = []
        for i in range(2, 10):
            newdict.append(Dict[i])

        print(newdict)
        newdict1 = []
        for j in newdict:
            newdict1.append(re.sub('\D', '', j))
        # using list comprehension
        values=newdict1
        total1 = values[4]
        new1 = values[0]
        active1 = values[1]
        critical1 = values[2]
        recovered1 = values[3]
        #.format(code1=code1, code2=code2, code3=code3, code4=code4, code5=code5

        '''msg.add_alternative(email_message.format(country_name=country_name1, total=total1, new=new1, active=active1, critical=critical1,
                                       recovered=recovered1,subtype='html'))'''



        msg.add_alternative(email_message.format(country_name=country_name1, total=total1, new=new1, active=active1, critical=critical1,
                                    recovered=recovered1), subtype='html')


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            #print("email sent")
    def __init__(self):
        pass