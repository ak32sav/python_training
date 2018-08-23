# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.create_contact(Contact(fname="fname1", lname="lname1",nickname="nickname1",home_phone="0987654321",email="email1@gmail.com"))
        app.session.logout()

