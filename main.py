import pandas
import datetime as dt
import random as rand
import smtplib

email = "email@gmail.com"
password = "password"

birthday_data = pandas.read_csv("birthdays.csv")
birthdays = birthday_data.to_dict("records")
letters = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]

random_letter = rand.choice(letters)

today = dt.datetime.now()
today_day = today.day
today_month = today.month


def send_email(to="", text=""):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs=to,
                            msg=f"Subject:Happy Birthday!!!\n\n{text}")


for bdays in birthdays:
    if bdays["month"] == today_month and bdays["day"] == today_day:
        with open(f"{random_letter}") as letter:
            birthday_letter = letter.read().replace("Angela", "Paul").replace("[NAME]", f"{bdays['name']}")
        send_email(bdays["email"], birthday_letter)

print(birthday_letter)
