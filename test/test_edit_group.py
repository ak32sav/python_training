from model.group import Group
import random

def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="The 1st group", header="header", footer="footer"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="Edited group name", header="Edited group header", footer="Edited group footer")
    group.id = random_group.id
    app.group.edit_group_by_id(group, random_group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(random_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="The 1st group", header="header", footer="footer"))
#     old_groups = app.group.get_group_list()
#     group = Group(name="New group name")
#     group.id = old_groups[0].id
#     app.group.edit_first_group(group)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="The 1st group", header="header", footer="footer"))
#     old_groups = app.group.get_group_list()
#     group = Group(header="New group header")
#     group.id = old_groups[0].id
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

