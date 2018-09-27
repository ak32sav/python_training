import re
from random import randrange
from model.contact import Contact

def test_contact_info_on_homepage(app, db):
    contacts_hp = app.contact.get_contacts_list()
    contacts_db = db.get_contact_list()
    contacts_db.sort(key=Contact.id_or_max)
    contacts_hp.sort(key=Contact.id_or_max)
    print("\n")
    for i in range(0, len(contacts_db)):
        if contacts_hp[i].id == '111':
            print("address1:\n<" + contacts_hp[i].address + ">")
            print("address2:\n<" + contacts_db[i].address + ">")
            print("\nEND")
            print(len(contacts_hp[i].address))
            print(len(contacts_db[i].address))
            a = contacts_hp[i].address
            b = contacts_db[i].address
            for j in range(0,len(a)):
                 if a[j] == b[j]:
                     print(1)
                 else:
                    print(0)
                    print(a[j])
                    print(b[j])
            assert contacts_hp[i] == contacts_db[i]
            assert contacts_hp[i].emails == merge_emails_like_on_homepage(contacts_db[i])
            assert contacts_hp[i].address == contacts_db[i].address
            assert contacts_hp[i].all_phones == merge_phones_like_on_homepage(contacts_db[i])
    # assert contact_from_homepage == contact_from_edit_page
    # assert contact_from_homepage.emails == merge_emails_like_on_homepage(contact_from_edit_page)
    # assert contact_from_homepage.address == contact_from_edit_page.address
    # assert contact_from_homepage.all_phones == merge_phones_like_on_homepage(contact_from_edit_page)

# def test_contact_info_on_homepage(app):
#     all_contacts = app.contact.get_contacts_list()
#     index = randrange(len(all_contacts))
#     contact_from_homepage = all_contacts[index]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_homepage == contact_from_edit_page
#     assert contact_from_homepage.emails == merge_emails_like_on_homepage(contact_from_edit_page)
#     assert contact_from_homepage.address == contact_from_edit_page.address
#     assert contact_from_homepage.all_phones == merge_phones_like_on_homepage(contact_from_edit_page)

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