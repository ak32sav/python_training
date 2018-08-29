# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        app.contact.create(Contact(fname="fname1", lname="lname1", nickname="nickname1", home_phone="0987654321", email="email1@gmail.com"))

