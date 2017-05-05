from model.group import Group


def test_delete_first_group(app):
#ситуация, когда нет ни одной группы, в самом тесте проверить наличие хоть одной группы,
# если оно не выполняется, то автоматически создать подходящую группу
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()