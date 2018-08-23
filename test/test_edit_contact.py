
def test_edit_contact(app):
    app.helper.session.login(username="admin", password="secret")
    app.helper.contact.edit_first_contact()
    app.helper.session.logout()