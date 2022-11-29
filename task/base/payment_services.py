from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

DOMAIN = 'http://127.0.0.1:8000'


def create_checkout_session(name: str, price: int) -> dict:
    """
    Creates stripe's checkout session and returns 
    dict with session preferences

    Args:
        name (str): name of the product
        price (int): pric of the product in USD cents
    """
    session = stripe.checkout.Session.create(
      line_items=[{
        'price_data': {
          'currency': 'usd',
          'product_data': {
            'name': name,
          },
          'unit_amount': price,
        },
        'quantity': 1,
      }],
      mode='payment',
      success_url= DOMAIN + '/success',
      cancel_url= DOMAIN + '/cancel',
    )
    return session
        