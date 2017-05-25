from model.contact import Contact


def test_delete_first_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="проверка"))
    app.contact.delete_first_contact()
    new_contact = app.contacts.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)