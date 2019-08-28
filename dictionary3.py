s={1:10, 2:20}
d={3:30, 4:40}
e={5:50,6:60}
f = {}
for i in (s,d,e):f.update(i)
print(f)
