from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    # опция n, которая задает количество генерируемых данных и опция f -куда всё это должно помещаться
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    #название опции и её значение(-n)
    if o == "-n":
        n = int(a) #значит в ней задаётся количество групп
    elif o == "-f":
        f = a


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

        for i in range(n)
]


#f-относительный путь к файлу, который указывается в виде параметра, либо дефолтное значение f = "data/contacts.json"
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

#открываем его на запись
with open(file, "w") as out_cont:
    out_cont.write(json.dumps(testcontact, default=lambda x: x.__dict__, indent=2)) #indent=2 -  в столбец выводит данные