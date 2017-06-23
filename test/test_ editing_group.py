from model.group import Group
import random


def test_editing_some_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group_date = Group(name="New group")
    new_group_date.id = group.id
    app.group.editing_group_by_id(group.id, new_group_date)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(new_group_date)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        groups_from_ui = app.group.get_group_list()
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        groups_from_db = map(clean, new_groups)
        assert sorted(groups_from_db, key=Group.id_or_max) == sorted(groups_from_ui, key=Group.id_or_max)

#def test_editing_first_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.editing_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    #сделаем простую проверку, убедимся, что новый список длинее чем старый на ед-цу
#    assert len(old_groups) == len(new_groups)