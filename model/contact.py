from sys import maxsize

class Contact:

    def __init__(self, id=None, fname=None, lname=None, nickname=None, home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None, all_phones_from_homepage=None, email=None):
        self.fname = fname
        self.lname = lname
        self.nickname = nickname
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s" % (self.id, self.fname, self.lname, self.home_phone, self.work_phone, self.mobile_phone, self.secondary_phone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and (self.fname==other.fname and self.lname == other.lname)

    def id_or_max(c):
        if c.id:
            return int(c.id)
        else:
            return maxsize