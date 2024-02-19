import stripe

from config.settings import API_KEY

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

