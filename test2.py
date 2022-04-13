import string

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase

print(lowercase_letters[1])

a = "cat"
#a[1] = "b"
b = "avdd"
c = "i"

print(a.find("a"))

print(a.replace(b, c))

f = b[:]
f = f.replace("a", "b")
print(f)
print(b)

v, w, x = ("a", "b", "C")
print(v)

print(ord("a"))
print(ord("Z"))
#print()
print(0 % 26)
for i in range(0, 128):
    print(chr(i))
