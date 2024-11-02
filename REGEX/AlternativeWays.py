


import re

p=re.compile("m\w\w")
m=p.match("dad mam man map run gun mad")
                                        or
m=re.match("m\w\w","dad mam man map run gun mad")
print("==================================")

p=re.compile("m\w\w")
m=p.search("dad mam man map run gun mad")
                                 or
m=re.search("m\w\w","dad mam man map run gun mad")
print("====================================")

p=re.compile("m\w\w")
lst=p.findall("dad mam man map run gun mad")
                                    or
lst=re.findall("m\w\w","dad mam man map run gun mad")


















