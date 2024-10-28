from django.contrib import admin
from django.urls import path, re_path, register_converter
from .views import index, about, addpage, contact, login, show_post, show_category
from .converters import FourDigitYearConverter


register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name="about"),
    path("addpage", addpage, name="add_page"),
    path("contact", contact, name="contact"),
    path("login", login, name="login"),
     path('post/<int:post_id>/', show_post, name='post'),
    # re_path(r"^archive/(?P<year>[0-9]{4})", archive),
    path("category/<int:cat_id>/", show_category, name="category")

]
