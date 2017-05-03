# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="malkons", middlename="don", lastname="perli", nickname="opr", title="dert",
                               company="esrt", address="street arbat", home="8394-33", mobile="4-4",
                               work="345-3", fax="345-213", email="test@gmaik.ty", email2="pes@kf.re", email3="pdt@ll.et",
                               homepage="prospact",
                               day1="//div[@id='content']/form/select[1]//option[12]",
                               month1="//div[@id='content']/form/select[2]//option[3]", byear="1988",
                               day2="//div[@id='content']/form/select[3]//option[19]",
                               month2="//div[@id='content']/form/select[4]//option[3]", ayear="1930",
                               address2="street borovaya", phone2="44-532",
                               notes="primer"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                               company="", address="", home="", mobile="",
                               work="", fax="", email="", email2="", email3="",
                               homepage="",
                               day1="//div[@id='content']/form/select[1]//option[1]",
                               month1="//div[@id='content']/form/select[2]//option[1]", byear="",
                               day2="//div[@id='content']/form/select[3]//option[1]",
                               month2="//div[@id='content']/form/select[4]//option[1]", ayear="",
                               address2="", phone2="",
                               notes=""))