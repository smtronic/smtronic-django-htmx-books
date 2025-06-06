from django.forms import CharField, ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from .models import Book


class BookCreateForm(ModelForm):
    title = CharField(
        required=False,
        widget=TextInput(attrs={"class": "clrtxt", "placeholder": _("Title")}),
    )
    author = CharField(
        required=False,
        widget=TextInput(attrs={"class": "clrtxt", "placeholder": _("Author")}),
    )
    price = CharField(
        required=False,
        widget=TextInput(attrs={"class": "clrtxt", "placeholder": _("Price")}),
    )

    class Meta:
        model = Book
        fields = ["title", "author", "price"]


class BookEditForm(BookCreateForm):
    title = CharField(
        required=False,
        widget=TextInput(attrs={"class": "form-control-sm form-control"}),
    )
    author = CharField(
        required=False,
        widget=TextInput(attrs={"class": "form-control-sm form-control"}),
    )
    price = CharField(
        required=False,
        widget=TextInput(attrs={"class": "form-control-sm form-control"}),
    )
