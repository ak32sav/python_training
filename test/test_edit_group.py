from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="The 1st group", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="Edited group name", header="Edited group header", footer="Edited group footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="The 1st group", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="New group name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="The 1st group", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(header="New group header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

