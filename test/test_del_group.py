from model.group import Group


def test_delete_first_group(app):
    #ситуация, когда нет ни одной группы, в самом тесте проверить наличие хоть одной группы,
# если оно не выполняется, то автоматически создать подходящую группу
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    #сделаем простую проверку, убедимся, что новый список длинее чем старый на ед-цу
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups == new_groups

