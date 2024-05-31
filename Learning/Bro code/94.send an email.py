import smtplib

sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "password"
subject = "Python email test"
body = "I wrote an email"

# header
message = f"""From: Boffins{sender}
To: Huzaifa{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)
print("Logged in...")
server.sendmail(sender, receiver, message)
print("Email has been send!")