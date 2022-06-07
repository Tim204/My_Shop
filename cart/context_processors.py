""" Makes the cart instance Available globally 
    to all templates.
"""

from .cart import Cart

def cart(request):
    """Defining a cart object that is visible on all templates"""
    return {'cart': Cart(request)} # Makes the cart object available 
                                   # as a variable named "cart"