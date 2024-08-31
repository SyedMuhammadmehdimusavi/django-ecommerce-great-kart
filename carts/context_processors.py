


from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            # Get the single Cart object corresponding to the cart_id
            cart = Cart.objects.get(cart_id=_cart_id(request))
            
            # Retrieve all CartItem objects associated with this Cart
            cart_items = CartItem.objects.filter(cart=cart)
            
            # Sum up the quantities of all items in the cart
            for cart_item in cart_items:
                cart_count += cart_item.quantity
                
        except Cart.DoesNotExist:
            # Handle the case where no Cart is found
            cart_count = 0

    # Return the cart count in the context
    return dict(cart_count=cart_count)
