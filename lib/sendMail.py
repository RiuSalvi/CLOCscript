import smtplib, config

def sendEmail(receiver, text):
    sender = "CLOC Bot <CLOCBot@checkmarx.com>"

    message = f"""Subject: CLOC Scan Result\r\nTo: {receiver}\r\nFrom: {sender}\r\n\r\n{text}"""

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.login(config.mailtrapUser, config.mailtrapPass)
        server.sendmail(sender, receiver, message)
        server.quit()

    print("Email with the results sent to", receiver)