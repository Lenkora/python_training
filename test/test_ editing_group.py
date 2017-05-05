from model.group import Group

def test_editing_first_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.editing_first_group(Group(name="New group"))

def test_editing_first_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.editing_first_group(Group(header="New header"))