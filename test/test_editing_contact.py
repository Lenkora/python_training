from model.contact import Contact

def test_editing_first_name(app):
    app.contact.editing_first_contact(Contact(firstname="NEW firstname"))


def test_editing_first_day2(app):
    #сменила вторую дату на 11
    app.contact.editing_first_contact(Contact(aday="11"))

