from model.group import Group

def test_edit_group(app):
    app.group.edit_first_group(Group(name="Edited group name", header="Edited group header", footer="Edited group footer"))

def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="New group name"))

def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="New group header"))
