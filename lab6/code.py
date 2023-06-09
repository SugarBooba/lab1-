first_numb = 30
second_numb = 30

AC = bin(first_numb)[2:]
DR = bin(second_numb)[2:]

AC = "0"*(16-len(AC))+AC
DR = "0"*(16-len(DR))+DR

print("AC = ", AC, "DR = ", DR)
BR = "0"
# binary_first_numb = "0"+binary_first_numb[:-1]
# print(binary_first_numb)
c = 0

def asr(numb, c):
    c = numb[-1]
    return "0"+numb[:-1], c

def asl(numb, c):
    c = numb[0]
    return numb[1:]+"0", c
while True:
    AC, c = asr(AC, c)

    if c != "0":
        # BR+= DR
        BR = bin(int(BR, 2)+int(DR, 2))[2:]

    DR,c = asl(DR, c)
    if int(AC, 2) == 0:
        break
print(int(BR, 2), BR)
    
    
# print(int("55", 16))
print(hex(int("55",16)*int("2",16))[2:])
# print(hex(85*2))
