from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (
    book_detail,
    book_list,
    book_list_sort,
    create_book,
    delete_book,
    update_book_details,
    update_book_status,
)

urlpatterns = [
    path("", book_list, name="book_list"),
    path(_("create_book/"), create_book, name="create_book"),
    path(
        _("update_book_details/<int:pk>/"),
        update_book_details,
        name="update_book_details",
    ),
    path(_("book_detail/<int:pk>/"), book_detail, name="book_detail"),
    path(_("delete_book/<int:pk>/"), delete_book, name="delete_book"),
    path(
        _("update_book_status/<int:pk>/"), update_book_status, name="update_book_status"
    ),
    path(
        _("book_list_sort/<filter>/<direction>/"), book_list_sort, name="book_list_sort"
    ),
]
