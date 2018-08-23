# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
        app.helper.session.login(username="admin", password="secret")
        app.helper.group.create(Group(name="1st group", header="header", footer="footer"))
        app.helper.session.logout()

def test_add_empty_group(app):
        app.helper.session.login(username="admin", password="secret")
        app.helper.group.create(Group(name="", header="", footer=""))
        app.helper.session.logout()

