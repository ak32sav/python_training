from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="The 1st group", header="header", footer="footer"))
    app.group.edit_first_group(Group(name="Edited group name", header="Edited group header", footer="Edited group footer"))

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="The 1st group", header="header", footer="footer"))
    app.group.edit_first_group(Group(name="New group name"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="The 1st group", header="header", footer="footer"))
    app.group.edit_first_group(Group(header="New group header"))
