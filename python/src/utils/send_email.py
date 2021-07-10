import smtplib
from email.mime.text import MIMEText
import threading
from random import randint


class SendEmail:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    @staticmethod
    def __send(email, senha, titulo, mensagem, destinos):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(email, senha)

        message = MIMEText(mensagem)
        message['subject'] = titulo
        message['from'] = email
        message['to'] = ''.join(destinos)
        server.sendmail(email, destinos, message.as_string())
        server.quit()
        print('email enviado para', ', '.join(destinos))

    def send(self, titulo, mensagem, destinos):
        target = self.__send
        email = self.email
        senha = self.__senha
        t = threading.Thread(target=target, args=(
            email, senha, titulo, mensagem, destinos))
        t.start()

    def codigo_verificacao(self, destino):
        codigo = ''
        for n in range(6):
            codigo += str(randint(0, 9))
        mensagem = f'Seu código de verificação é: {codigo}'
        self.send('Código de verificação Guia fone', mensagem, [destino])
        return codigo


# send_email = SendEmail('email', 'senha')
