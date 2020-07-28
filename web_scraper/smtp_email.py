import smtplib

subject = 'It is a test'
msg = 'And that\'s the message! How are you?'


def send_email(smtp_server, tls_port, usr, pdw, receiver, message):
    conn = smtplib.SMTP(smtp_server, tls_port)
    # start the connection
    conn.ehlo()
    # encrypt
    conn.starttls()
    # login
    conn.login(usr, pdw)
    # sent the email
    conn.sendmail(usr, receiver, message)
    # quit the connection and exit the program
    conn.quit()
    exit(0)


if __name__ == '__main__':
    send_email(
        'smtp.gmail.com',
        587,
        'your.email@domain.com',
        'your_password',
        'receiver.mail@domain.com',
        'Subject: ' + subject + '\n\n' + msg
    )
