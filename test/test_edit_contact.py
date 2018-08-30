from model.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(fname="fname1", lname="lname1", nickname="nickname1", home_phone="0987654321", email="email1@gmail.com"))
    app.contact.edit_first_contact()
