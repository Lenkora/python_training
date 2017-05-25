from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        #wd.find_element_by_name("theform").click()
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_birthday_date("bday", contact.bday)
        self.change_birthday_date("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_birthday_date("aday", contact.aday)
        self.change_birthday_date("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_birthday_date(self, field_name, date_value):
        wd = self.app.wd
        if date_value is not None:
            select = Select(wd.find_element_by_name(field_name))
            select.select_by_visible_text(date_value)
            #БЫЛО - упрощение кода, чтобы дату воспринимало, как число, а не просто имя
            #if not wd.find_element_by_xpath(field_name).is_selected():
                #wd.find_element_by_xpath(field_name).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.init_home_creation()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def init_home_creation(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def editing_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.init_home_creation()
        self.select_first_contact()
        #open edit form
        wd.find_element_by_xpath("//form[@name='MainForm']//img[@title='Edit']").click()
        #fill contact form
        self.fill_contact_form(new_contact_data)
        #submit edit
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.init_home_creation()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.init_home_creation()
        contact = []
#удобнее всего выбрать нужную строку, потом разбить её на ячейки
        for row in wd.find_elements_by_name("entry"):
            cells = row.find_elements_by_tag_name("td")
            last_name = cells[1].text
            first_name = cells[2].text
            id = row.find_element_by_name("selected[]").get_attribute("value")
            contact.append(Contact(lastname=last_name, firstname=first_name, id=id))
        return contact