
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
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        #wd.find_element_by_name("theform").click()
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.home)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("day1", contact.day1)
        self.change_field_value("month1", contact.month1)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("day2", contact.day2)
        self.change_field_value("month2", contact.month2)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)


    def change_field_value(self, field_firstname, text, field_day, field_month):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_firstname).click()
            wd.find_element_by_name(field_firstname).clear()
            wd.find_element_by_name(field_firstname).send_keys(text)
        if field_day is not None:
            if not wd.find_element_by_xpath(field_day).is_selected():
                wd.find_element_by_xpath(field_day).click()
        if field_month is not None:
            if not wd.find_element_by_xpath(field_month).is_selected():
                wd.find_element_by_xpath(field_month).click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.init_contact_creation()
        #select first contact
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()


    def editing_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.init_contact_creation()
        self.select_first_contact()
        wd.find_element_by_xpath("//form[@name='MainForm']//img[@title='Edit']").click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


