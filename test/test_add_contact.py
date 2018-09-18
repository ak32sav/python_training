# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone():
        return "".join([random.choice(string.digits) for i in range(10)])

def random_email():
        return "".join([random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(3,20))]) + "@gmail.com"

testdata = [Contact(fname="", lname="", nickname="", home_phone="", email="")] + [
        Contact(fname=random_string("fname",10), lname=random_string("lname",10), nickname=random_string("nickname",10), home_phone=random_phone(), email=random_email())
        for i in range(4)
        ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
        old_contacts = app.contact.get_contacts_list()
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contacts_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



