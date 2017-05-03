from model.contact import Contact


def test_editing_first_contact(app):
    app.contact.editing_first_contact(Contact(firstname="NEW firstname"))


def test_editing_first_contact(app):
    app.contact.editing_first_contact(Contact(day1="//div[@id='content']/form/select[1]//option[10]"))