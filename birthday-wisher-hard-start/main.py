##################### Hard Starting Project ######################
import random
import smtplib
import pandas

user='manisharora402@gmail.com'
password = 'qapmerkryumfiweg'

from datetime import datetime
data = pandas.read_csv('birthdays.csv')
today = datetime.now()
today_tuple = (today.month,today.day)

birthday_dict = {(data_row.month,data_row.day) : data_row for(index,data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace('[NAME]',birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com',587) as connection:
        connection.starttls()
        connection.login(user, password)
        connection.sendmail(from_addr=user, to_addrs=birthday_person['email'],msg=f"Subject:Happy birthday!!\n{content}"
                            )

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



