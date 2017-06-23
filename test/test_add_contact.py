from model.contact import Contact

def test_add_contact(app, db, json_contacts, check_ui):
    contact =json_contacts
    old_contact = db.get_contact_list()
    app.contact.create(contact)
#проверка, что old_contacts больше на единицу списка: new_contacts
    new_contact = db.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)