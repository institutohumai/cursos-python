#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Envía un mail en texto plano desde la línea de comandos o desde un script de
python. Usa un archivo de configuración para tomar un usuario y password
defaults, pero pueden pasarse como argumentos a la función.
Example:
    python send_email.py "Hola mundo!" other_email@server.com "Mensaje."
Debe crearse un config_email.yaml como este:
    gmail:
      user: usuario
      pass: password
"""

import sys
import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate


SMTP_SERVER = "smtp.gmail.com"
# PORT = 465  # port if using SMTP_SSL
PORT = 587


def send_email(subject, to, email_user, email_pass,
               message_text=None, message_html=None, files=None):

    # parametros
    to_list = to.split(",")
    files = files.split(",") if files else []

    # construye las distintas partes de un mail
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_user
    msg['To'] = to
    msg['Date'] = formatdate(localtime=True)

    # agrega texto al cuerpo del mensaje y luego html, si lo hay
    if message_text:
        msg.attach(MIMEText(message_text, "plain"))
    if message_html:
        msg.attach(MIMEText(message_html, "html"))

    # agrega archivos adjuntos
    for f in files:
        with open(f, "rb") as fil:
            part = MIMEApplication(fil.read(), Name=basename(f))
            part[
                'Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    # abre una sesión y envía el mail
    # s = smtplib.SMTP_SSL(SMTP_SERVER, PORT)
    s = smtplib.SMTP(SMTP_SERVER, PORT)
    s.ehlo()  # no need with SMTP_SLL
    s.starttls()  # no need with SMTP_SLL
    s.login(email_user, email_pass)
    s.sendmail(email_user, to_list, msg.as_string())
    s.close()

    print("Se envió exitosamente un reporte a " + to)


if __name__ == '__main__':

    if len(sys.argv) > 3:
        send_email(*sys.argv[1:])

    else:
        print("Se deben especificar los siguientes argumentos:",
              "    asunto mensaje [destinatario1,destinatario2...]")
