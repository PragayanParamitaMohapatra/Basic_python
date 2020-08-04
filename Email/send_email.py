import smtplib

gmail_user = 'mitanjalimohapatra321@gmail.com'
gmail_app_password = input( "Type your password and press enter: " )
sent_from = gmail_user
sent_to = ['pragayanparamitaguddi111@gmail.com', 'sasmitakjena321@gmail.com']
sent_subject = "Where are all my Robot Women at?"
sent_body = ("Hey, what's up? my dear friend punu baby!\n\n"
             "I hope you have been well!\n"
             "\n"
             "Cheers,\n"
             "Jay\n")
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join( sent_to ), sent_subject, sent_body)
try:
    server = smtplib.SMTP_SSL( 'smtp.gmail.com', 465 )
    server.ehlo()
    server.login( gmail_user, gmail_app_password )
    server.sendmail( sent_from, sent_to, email_text )
    server.close()

    print( 'Email sent!' )
except Exception as exception:
    print( "Error: %s!\n\n" % exception )
