def spamming_email_4_gmail(source, Password, destination, message):
    #code by Hud Seidu Daannaa MSc, CEH
    #parameters
    #source      = 'source@gmail.com'
    #destination = 'destination@gmail.com'
    #Password    = 'Pa55w0rd'
    
    #
    import smtplib
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    print smtpserver.login(source, Password)
    smtpserver.sendmail(source, destination, str(message))
    print 'done!'
    #smtpserver.close()(message):
    

source             = '@gmail.com'
source_Password    = ''
destination        = '@gmail.com'
Number_of_times = 100

for message in range(Number_of_times):
    spamming_email_4_gmail(source, source_Password, destination, message)
