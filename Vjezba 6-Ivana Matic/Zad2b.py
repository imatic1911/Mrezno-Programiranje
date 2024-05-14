from smtplib import SMTP

smtp = SMTP()

SMTP_HOST = '127.0.0.1'
SMTP_PORT = '1025'
SMTP_TIMEOUT = 10

smtp.set_debuglevel(True)
smtp.connect(SMTP_HOST, SMTP_PORT)
smtp.ehlo()

message = 'Poruka poslana iz pythona!'
sender = 'ivana.matic@aspira.com'
recipient = 'anteprojic@gmail.com'

try:
    smtp.sendmail(sender, recipient, message)
except:
    print('Error while sending..')

smtp.quit()
