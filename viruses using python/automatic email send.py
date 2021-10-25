import smtplib

server  = smtplib.SMTP_SSL("smtp.gmail.com" , 465)
server.login("codemaster041@gmail.com", "codemaster1234")
server.sendmail("codemaster041@gmail.com" , "paridivyansh7@gmail.com" , "Hello  , how are you?")
server.quit()