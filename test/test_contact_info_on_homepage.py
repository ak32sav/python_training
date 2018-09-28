import re
from random import randrange
from model.contact import Contact

def test_contact_info_on_homepage(app, db):
    contacts_hp = app.contact.get_contacts_list()
    contacts_db = db.get_contact_list()
    contacts_db.sort(key=Contact.id_or_max)
    contacts_hp.sort(key=Contact.id_or_max)
    for i in range(0, len(contacts_db)):
        assert contacts_hp[i] == contacts_db[i]
        assert contacts_hp[i].emails == merge_emails_like_on_homepage(contacts_db[i])
        assert contacts_hp[i].address == contacts_db[i].address
        assert contacts_hp[i].all_phones == merge_phones_like_on_homepage(contacts_db[i])

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.secondary_phone]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))

# if contacts_hp[i].id == '317':
#     print("<")
#     print(contacts_hp[i])
#     print(">\n========================================================\n")
#     print("<")
#     print(contacts_db[i])
#     print(">\n========================================================\n")
# print(len(contacts_hp[i].emails))
# print(len(contacts_db[i].email) + len(contacts_db[i].email2) + len(contacts_db[i].email3))
# a = contacts_hp[i].emails
# b = merge_emails_like_on_homepage(contacts_db[i])
# for j in range(0,len(a)):
#      if a[j] == b[j]:
#          print("<1:%r:%r>" % (a[j], b[j]))
#      else:
#          print("<0:%r:%r>" % (a[j], b[j]))