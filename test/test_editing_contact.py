from model.contact import Contact
from random import randrange


def test_editing_some_name(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="проверка", lastname="NEW_lastname"))
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(firstname="NEW firstname", lastname="NEW_last_name")
    contact.id = old_contact[index].id
    id = contact.id
    app.contact.editing_contact_by_id(id, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = db.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


#def test_editing_first_day2(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="проверка", aday="10", amonth="April"))
#    app.contact.editing_first_contact(Contact(aday="11", amonth="November", bday="21", bmonth="April"))

