def def spamming_email_4_gmail(message):
    import smtplib
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    print smtpserver.login('source@gmail.com', 'Password')
    smtpserver.sendmail('source@gmail.com','destination@gmail.com',str(message))
    print 'done!'
    smtpserver.close()(message):
