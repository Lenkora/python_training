# -*- coding: utf-8 -*-

from model.contact import *
import pytest

from data.contacts import contant as testcontact

@pytest.mark.parametrize("contact", testcontact, ids=[repr(x) for x in testcontact])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
#проверка, что old_contacts больше на единицу списка: new_contacts
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


