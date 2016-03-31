#jeżeli
a = 3
if a > 2:
    #op1
    #op2
    b = 55
    c = 22
    print(a, b)

if a > 2:
    #op1
    #op2
    b = 55
    c = 22
else:
    d = 11
    print("DD")

if a < 2:
    #op1
    #op2
    b = 55
    c = 22
elif a == 3:
    print("elif")
else:
    d = 11
    print("DD")

#dopóki
a = 0
while a < 3:
    a = a + 1
    print(a)

a = 0
while a < 3:
    a = a + 1
    print(a)
else:
    print("else")

#dla (for)
for a in (range(1,11)):
    print(a)

for a in (range(11)):
    print(a)
else:
    print("hoo")

  # brake
for a in (range(11)):
    if a > 4:
        break
    print(a)
else:
    print("hoo")

# continue
for a in (range(11)):
    if a > 4:
        continue
    print(a)
else:
    print("hoo")

