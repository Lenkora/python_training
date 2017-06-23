from model.contact import Contact
import random
import string

contant = [
    Contact(firstname="firstname1", lastname="lastname1", nickname="nickname1", home="home1",mobile="mobile1",
            work="work1", email="email1", email2="email21",email3="email31",ayear="ayear1"),
    Contact(firstname="firstname2", lastname="lastname2", nickname="nickname2", home="home2",mobile="mobile2",
            work="work2", email="email2", email2="email22",email3="email32", ayear="ayear2")
]

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