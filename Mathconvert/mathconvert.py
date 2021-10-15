#Documentation
def docs():
    print("Decimal To Binary => Mathconvert.d2b(Number)")
    print("Binary To Decimal => Mathconvert.b2d(Number)")
    print("Hex To Decimal    => Mathconvert.h2d(Number)")
    print("Decimal To Hex    => Mathconvert.d2h(Number)")
    print("Octal To Decimal  => Mathconvert.o2d(Number)")
    print("Decimal To Octal  => Mathconvert.d2o(Number)")
    print("Binary To Hex     => Mathconvert.b2h(Number)")
    print("Hex To Binary     => Mathconvert.h2b(Number)")
    print("Binary To Octal   => Mathconvert.b2o(Number)")
    print("Octal To Binary   => Mathconvert.o2b(Number)")
    print("Library By ayoub ech-chetyouy")
#Octal To Binary
def o2b(num):
    l = []
    nmbr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    o = str(num)
    rep1 = oct(int(o))
    for i in rep1.__str__():
        if i in nmbr:
            l.append(i)
    rp = ''
    for i in l:
        rp += i
    rep2 = bin(int(rp)).replace("0b", "")
    print(rep2)
#Decimal To Binary
def d2b(num):
    rep = 0
    ren = bin(int(num)).replace("0b", "")
    print(num)
#Binary To Decimal
def b2d(num):
    rep = 0
    rep = int(num, 2)
    print(rep)
#Hex To Decimal
def h2d(num):
    rep = 0
    rep = int(num, 16)
    print(rep)
#Decimal To Hex
def d2h(num):
    rep = 0
    rep = hex(int(num)).split('x')[-1]
    print(rep)
#Octale To Decimal
def o2d(num):
    rep = 0
    rep = oct(int(num))
    print(rep)
#Deimale To Octal
def d2o(num):
    rep = 0
    rep = int(num, 8)
    print(rep)
#Binary To Hex
def b2h(num):
    rep1 = int(num, 2)
    rep2 = hex(int(rep1)).split('x')[-1]
    print(rep2)
#Hex To Binary
def h2b(num):
    rep1 = int(num, 16)
    rep2 = bin(int(rep1)).replace("0b", "")
    print(rep2)
#Binary To Octal
def b2o(num):
    rep1 = int(num, 2)
    rep2 = oct(rep1)
    print(rep2)






