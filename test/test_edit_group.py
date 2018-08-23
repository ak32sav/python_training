

def test_edit_group(app):
    app.helper.session.login(username="admin", password="secret")
    app.helper.group.edit_first_group()
    app.helper.session.logout()