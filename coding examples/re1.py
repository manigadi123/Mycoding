import re
emailaddress=raw_input("enter your mail address")
pat2="(Yw+)@(Yw+Y.)+(com)"
r2=re.match(pat2,emailaddress)
print r2.group(1)
