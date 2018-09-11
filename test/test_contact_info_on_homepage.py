import re
from random import randrange


def test_contact_info_on_homepage(app):
    all_contacts = app.contact.get_contacts_list()
    index = randrange(len(all_contacts))
    contact_from_homepage = all_contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage == contact_from_edit_page
    assert contact_from_homepage.emails == merge_emails_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones == merge_phones_like_on_homepage(contact_from_edit_page)

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