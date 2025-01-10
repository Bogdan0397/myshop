from django import forms

PRODUCT_QUNTITY_CHOINSES = [(i, str(i)) for i in range(1,21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUNTITY_CHOINSES,coerce=int)
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)

