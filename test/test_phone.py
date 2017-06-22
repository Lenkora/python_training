import re
from random import randrange

def test_contact_phone_on_home_page(app):

    # выбрать контакт
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))

    # получить список его полей
    contact_from_home_page = app.contact.get_contact_list()[index]    # открыть контакт на редактирование
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.all_phones == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)

    # сравнить firstname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    # сравнить lastname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    # сравнить address
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
#шаблон для замены ненужных символов (очищение строки от известных нам символов)
    return re.sub("[() -]", '', s)

#Сравниваем с редактируемой страницей и основной
def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile,
                                        contact.work, contact.phone2]))))
# первая lambda необходимо оставить строчки, которые не пустые (lambda x: x != "")
# filter удаляет пустые значения None
# map помогает применять значение clear ко всему списку

def merge_emails_like_on_home_page(contact):
    return "\n".join([contact.email, contact.email2, contact.email3])