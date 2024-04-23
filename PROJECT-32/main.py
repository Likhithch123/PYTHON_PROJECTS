EMAIL = 'your_email'
PASSWORD = 'your_app_password'


import pandas, datetime, smtplib, random

data = pandas.read_csv('../python-projects/PROJECT-32/birthdays.csv')
data_dict = data.to_dict(orient='records')


today = datetime.datetime.now()

letter_number = random.randint(1, 3)


for i in range(len(data_dict)):
    month = data_dict[i]['month']
    day = data_dict[i]['day']
    if today.day == day and today.month == month:
        user_email = data_dict[i]['email']
        with open(f'../python-projects/PROJECT-32/letter_templates/letter_{letter_number}.txt') as letter_file:
            text = letter_file.read()
            text = text.replace('[NAME]', data_dict[i]['name']).replace('Angela', 'Your_Name')
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL , password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=user_email, msg=f'Subject: Happy Birthday.\n\n{text}')
