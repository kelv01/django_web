#creating utils for user message

from twilio.rest import Client
from django.conf import settings


def calculate_price(drink_type, size):
    prices = {
        'espresso': {'small': 2.00, 'medium': 2.50, 'large': 3.00}, 
        'latte': {'small': 3.00, 'medium': 3.50, 'large': 4.00}, 
        'cappuccino': {'small': 3.00, 'medium': 3.50, 'large': 4.00}, 
        'americano': {'small': 2.50, 'medium': 3.00, 'large': 4.50}, 
        'cocacola': {'small': 1.50, 'medium': 2.00, 'large': 2.50}, 
        'sprite': {'small': 1.50, 'medium': 2.00, 'large': 2.50}, 
        'fanta': {'small': 1.50, 'medium': 2.00, 'large': 2.50}, 
        'milkshake': {'small': 3.50, 'medium': 4.00, 'large': 4.50}, 
        'mango_juice': {'small': 3.00, 'medium': 3.50, 'large': 4.00}, 
        'passion_juice': {'small': 3.00, 'medium': 3.50, 'large': 4.00}, 
    }

def send_order_confirmation_sms(name, phone, drink_type, size, price):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message_body = (
        f"Thank you {name} for your order of {drink_type} "
        f"({size}) for {price} dollars."
        f"Total price: ${price:.2f}\n\n"
    )
    
    message = client.messages.create(
        body=message_body,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone
    )
    