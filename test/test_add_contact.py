# -*- coding: utf-8 -*-

from model.contact import *
import pytest
import random
import string

#для имен
def random_string_name(prefix, maxlen):
    symbols = string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#для телефонов
def random_string_phones(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#для почт
def random_string_emails(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" + \
           "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + ".ru"


testcontact = [Contact(firstname="")] + [
        Contact(firstname=random_string_name("firstname", 10), lastname=random_string_name("lastname", 10),
                nickname=random_string_name("nickname", 10),home=random_string_phones("home", 10),
                mobile=random_string_phones("mobile", 10),work=random_string_phones("work", 10),
                email=random_string_emails("email", 10), email2=random_string_emails("email2", 10),
                email3=random_string_emails("email3", 10), ayear="%s" % (random.choice(range(1970,2017))))

        for i in range(5)
]

@pytest.mark.parametrize("contact", testcontact, ids=[repr(x) for x in testcontact])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
#проверка, что old_contacts больше на единицу списка: new_contacts
    assert len(old_contact) + 1 == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


