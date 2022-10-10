from email.message import EmailMessage
import smtplib
remitente = "beder.ensuncho@outlook.com"
destinatario = "bensunch@hotmail.com"
mensaje = "¡Hola, mundo!"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)
smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(remitente, "Q17fb_mp")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()