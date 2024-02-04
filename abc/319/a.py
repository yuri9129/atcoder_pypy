p = """tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481"""

lst = p.split("\n")
lst = [x.split() for x in lst]
users = {}
for a,b in lst:
    users[a] = int(b)

s = input()

print(users[s])

