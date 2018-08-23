

def test_delete_group(app):
    app.helper.session.login(username="admin", password="secret")
    app.helper.group.delete_first_group()
    app.helper.session.logout()