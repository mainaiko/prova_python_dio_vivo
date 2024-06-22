# import re

# string = "Ola meu nome é Aiko Aiko"

# padrao = re.compile ("Aiko")

# # x = re.fullmatch(padrao, string)
# # x = re.search(padrao, string)
# x = re.findall(padrao, string)
# print (x)

import re

string = "222.222.222.22"
pattern = re.compile ("...\....\....\...")
x= re.fullmatch (pattern, string)

print (x)