from model.contact import Contact

def test_editing_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="проверка"))
    app.contact.editing_first_contact(Contact(firstname="NEW firstname"))


def test_editing_first_day2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="проверка", aday="10", amonth="April"))
    app.contact.editing_first_contact(Contact(aday="11", amonth="November", bday="21", bmonth="April"))
