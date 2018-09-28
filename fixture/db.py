import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name.strip(), header=header.strip(), footer=footer.strip()))
        finally:
            cursor.close()
            return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, phone2, email, email2, email3, address from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, phone2, email, email2, email3, address) = row
                list.append(Contact(id=str(id), fname=firstname.strip(), lname=lastname.strip(),
                                    email=email.strip(), email2=email2.strip(), email3=email3.strip(),
                                    home_phone=home.strip(), mobile_phone=mobile.strip(), work_phone=work.strip(), secondary_phone=phone2.strip(),
                                    address=address.strip().replace("\r\n", "\n")))
        finally:
            cursor.close()
            return list

    def destroy(self):
        self.connection.close()