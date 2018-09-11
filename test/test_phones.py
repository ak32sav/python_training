import re

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # print("EDIT: ")
    # #print(contact_from_edit_page)
    # print("\n".join(map(lambda x: clear(x), [contact_from_edit_page.home_phone, contact_from_edit_page.mobile_phone, contact_from_edit_page.work_phone, contact_from_edit_page.secondary_phone])))
    # print("HOME: ")
    # print(contact_from_homepage.all_phones_from_homepage)
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)

# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#     assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#     assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.secondary_phone]))))