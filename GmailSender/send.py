import smtplib
from email.message import EmailMessage
GMAIL_PASS = "xbnaifkgwppzrptw"
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()
smtp.starttls()
smtp.login("drnam.email@gmail.com", GMAIL_PASS)
email = EmailMessage()
email["Subject"] = "이메일 제목 입니다."
email["From"] = "drnam.email@gmail.com"
email["To"] = "python_test@yopmail.com, python123@yopmail.com"
email.set_content("이메일 내용 입니다.")
smtp.send_message(email)
smtp.quit()