
def test_editing_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.editing_first_group()
    app.session.logout()