from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone():
    return "".join([random.choice(string.digits) for i in range(10)])


def random_email():
    return "".join(
        [random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(3, 20))]) + "@gmail.com"


testdata = [Contact(fname="", lname="", nickname="", home_phone="", email="")] + [
        Contact(fname=random_string("fname",10), lname=random_string("lname",10), nickname=random_string("nickname",10), home_phone=random_phone(), email=random_email())
        for i in range(n)
        ]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))