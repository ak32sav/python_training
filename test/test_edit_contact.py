from model.contact import Contact
import random

def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fname="fname1", lname="lname1", nickname="nickname1", home_phone="0987654321", email="email1@gmail.com"))
    contact = Contact(fname="edited fname1", lname="edited lname1", nickname="edited nickname1", home_phone="edited 0987654321", email="edited email1@gmail.com")
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    contact.id = random_contact.id
    app.contact.edit_contact_by_id(contact, random_contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(random_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)