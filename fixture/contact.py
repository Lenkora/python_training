from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

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
        self.contact_cache = None

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
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # submit deletion contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.init_home_creation()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def init_home_creation(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def editing_first_contact(self, new_contact_data):
        self.editing_contact_by_index(0)
        self.contact_cache = None

    def editing_contact_by_index(self, index,  new_contact_data):
        wd = self.app.wd
        self.init_home_creation()
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//form[@name='MainForm']//img[@title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def editing_contact_by_id(self, id,  new_contact_data):
        wd = self.app.wd
        self.init_home_creation()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[id].click()



    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.init_home_creation()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.init_home_creation()
            self.contact_cache = []
    #удобнее всего выбрать нужную строку, потом разбить её на ячейки
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                first_name = cells[2].text
                last_name = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=first_name, lastname=last_name, id=id,
                                                  address=address,all_emails=all_emails, all_phones=all_phones ))
        return list(self.contact_cache)
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.init_home_creation()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.init_home_creation()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=first_name, lastname=last_name, id=id, address=address, email=email, email2=email2,
                       email3=email3, home=home, mobile=mobile, work=work,
                       phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)