import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import stripe

from config.settings import API_KEY, EMAIL_KEY, SMTP_SERVER, FROM_EMAIL

stripe.api_key = API_KEY

def buy(name: str, price: int ):
    product = stripe.Product.create(name=name) # (name=)

    price = stripe.Price.create(
        currency='rub',
        unit_amount=price,
        product_data={'name': name}
    )

    resp = stripe.checkout.Session.create(
      success_url="https://example.com/success",
      line_items=[{"price": price['id'], "quantity": 1}],
      mode="payment",
    )
    return resp

def send_mail(_to_mail, _subject ,_message):
    msg = MIMEMultipart()

    to_email = _to_mail
    message = _message

    msg.attach(MIMEText(message, 'plain'))
    msg['Subject'] = _subject

    server = SMTP_SERVER
    server.connect('smtp.mail.ru', 25)
    try:
        server = SMTP_SERVER
        server.starttls()
        server.login(FROM_EMAIL, EMAIL_KEY)
        server.sendmail(FROM_EMAIL, to_email, msg.as_string())

        server.quit()
    except smtplib.SMTPDataError as e:
        print(f' Ошибка при отправке письма: {e}')
