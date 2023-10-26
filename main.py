import smtplib
import os

def send_email(message):
    sender = 'anna.mihailovma@gmail.com'
    password = os.getenv('EMAIL_PASSWORD')
    # создаём объект сеанса клиента SMTP
    # передаём в параметры сервер и порт
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # запускаем шифрованный обмен
    server.starttls()
    try:
        server.login(sender, password)
        server.sendmail(sender, sender, f'Subject: CLICK ME PLEASE!\n{message}')
        return 'The message was sent successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please!'

def main():
    message = input('Type your message: ')
    send_email(message=message)

if __name__ == '__main__':
    main()
