import smtplib
sender_mail="pragayanparamitaguddi111@gmail.com"
recv_email="ppmohapatra321@gmail.com"
pass_word=input("please Enter your password: ")
msg="Hello how are you!!!!"
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender_mail,pass_word)
print("Login successful")
server.sendmail("pragayanparamitaguddi111@gmail.com","ppmohapatra321@gmail.com",msg)
print( 'successfully sent the mail',recv_email)
server.quit()