from model.group import Group

def test_editing_first_name(app):
    app.group.editing_first_group(Group(name="New group"))

def test_editing_first_header(app):
    app.group.editing_first_group(Group(header="New header"))