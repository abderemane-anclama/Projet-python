import re

file = open ("data.txt", "r")
sms = file.read()
var0 = "[a-zA-Z]+"
var1 = re.findall(var0, sms)

print(len(var1))