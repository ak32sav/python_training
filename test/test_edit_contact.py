from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="fname1", lname="lname1", nickname="nickname1", home_phone="0987654321", email="email1@gmail.com"))
    contact = Contact(fname="edited fname1", lname="edited lname1", nickname="edited nickname1", home_phone="edited 0987654321", email="edited email1@gmail.com")
    old_contacts = app.contact.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)