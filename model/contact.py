from sys import maxsize

class Contact:

    def __init__(self, id=None, fname=None, lname=None, nickname=None,
                 home_phone=None, mobile_phone=None, work_phone=None, secondary_phone=None, all_phones=None,
                 email=None, email2=None, email3=None, emails=None, address=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.nickname = nickname
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.secondary_phone = secondary_phone
        self.all_phones = all_phones
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.emails = emails
        self.address = address


    def __repr__(self):
        #return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.fname, self.lname, self.home_phone, self.work_phone, self.mobile_phone, self.secondary_phone, self.all_phones)
        return "\n========================\nID: %s\nFirst name: %s\nLast name: %s" \
               "\nHome phone: %s\nWork phone: %s\nMobile phone: %s\nSecondary phone: %s\nAll phones: \n%s" \
               "\nEmail: %s\nEmail2: %s\nEmail3: %s\nAll emails:\n%s" \
               "\nAddress:\n%s" \
               % (self.id, self.fname, self.lname,
                  self.home_phone, self.work_phone, self.mobile_phone, self.secondary_phone, self.all_phones,
                  self.email, self.email2, self.email3, self.emails,
                  self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and (self.fname == other.fname and self.lname == other.lname)

    def id_or_max(c):
        if c.id:
            return int(c.id)
        else:
            return maxsize