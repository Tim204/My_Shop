from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label="",) # coerce=int converts the input into an integer
    
    # override- allows you to specify whether you the "quantity" gets added 
    # to an existing quantity in the cart for a specified product(Flase)
    # OR if the existing quantity needs to be overridden with a give quantify(True)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
    