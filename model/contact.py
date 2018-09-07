from sys import maxsize

class Contact:

    def __init__(self, id=None, fname=None, lname=None, nickname=None, home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None, email=None):
        self.fname = fname
        self.lname = lname
        self.nickname = nickname
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.fname, self.lname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and (self.fname==other.fname and self.lname == other.lname)

    def id_or_max(c):
        if c.id:
            return int(c.id)
        else:
            return maxsize