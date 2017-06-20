from model.group import Group
from random import randrange

def test_editing_some_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.editing_group_by_index(index, group)
    #сделаем простую проверку, убедимся, что новый список длинее чем старый на ед-цу
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key= Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_editing_first_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.editing_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    #сделаем простую проверку, убедимся, что новый список длинее чем старый на ед-цу
#    assert len(old_groups) == len(new_groups)