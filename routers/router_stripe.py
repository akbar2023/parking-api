from fastapi import APIRouter
import stripe



router = APIRouter (
  tags = ["Stripe"],
  prefix = "/stripe" 
)


stripe.api_key = "sk_test_51O51uqLH8U7iHbp0Gpvcdn65e5leEzI8vSAJeh0wySmeQHF969kUCgeZfNtUsblEXtyJDXisT8JFiVfKQqcw2sUd00JEihEBdG"

YOUR_DOMAIN = "http://localhost"


@router.post('/checkout')
async def stripe_checkout():
  try:
    checkout_session = stripe.checkout.Session.create(
      line_items = [
        {
          # price_id du produit à vendre
          'price': 'price_1O51yeLH8U7iHbp0pw4GJ2qj',
          'quantity': 1
        }
      ],
      mode= 'subscription',
      payment_method_types= 'card',
      success_url=YOUR_DOMAIN + '/success.html',
      cancel_url=YOUR_DOMAIN + '/cancel.html'
    )
    return checkout_session
  except Exception as e:
    return str(e) 