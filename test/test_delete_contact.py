
def test_delete_contact(app):
    app.helper.session.login(username="admin", password="secret")
    app.helper.contact.delete_first_contact()
    app.helper.session.logout()