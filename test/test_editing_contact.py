from model.contact import Contact

def test_editing_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="проверка"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="NEW firstname")
    contact.id = old_contact[0].id
    app.contact.editing_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_editing_first_day2(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="проверка", aday="10", amonth="April"))
#    app.contact.editing_first_contact(Contact(aday="11", amonth="November", bday="21", bmonth="April"))
