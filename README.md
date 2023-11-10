import random
lower_case = "abcdefghijklmnopqrstuvwxz"
upper_case = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sysmbol = "[]{}#()*;._-"
ans = lower_case + upper_case + num + sysmbol

length = 9
password = "".join(random.sample(ans,length))
print(" Generated password ", password)
