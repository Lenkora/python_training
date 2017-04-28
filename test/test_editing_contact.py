def test_editing_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.editing_first_contact()
    app.session.logout()