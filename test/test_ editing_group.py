from model.group import Group

def test_editing_first_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.editing_first_group(group)
    new_groups = app.group.get_group_list()
    #сделаем простую проверку, убедимся, что новый список длинее чем старый на ед-цу
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key= Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_editing_first_header(app):
#    old_groups = app.group.get_group_list()
#    app.group.editing_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    #сделаем простую проверку, убедимся, что новый список длинее чем старый на ед-цу
#    assert len(old_groups) == len(new_groups)