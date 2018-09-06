# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
        old_contacts = app.contact.get_contacts_list()
        contact = Contact(fname="fname1", lname="lname1", nickname="nickname1", home_phone="0987654321", email="email1@gmail.com")
        app.contact.create(contact)
        assert len(old_contacts) + 1 == app.contact.count()
        new_contacts = app.contact.get_contacts_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



