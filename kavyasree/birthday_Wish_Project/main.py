import smtplib

my_email = "sravanisravani45857@gmail.com"
password = "tesyzaooslbjeele"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="gowdakavya418@gmail.com",
                        msg="Subject:Best Birthday Wishes...\n\nHappy Birthday!🎉😊 May your day be as sweet and delightful as a birthday cake!🎂\nCheers to you on your big day! 🥂🍾🎉"
                        )
