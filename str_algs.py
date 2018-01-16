stroka="hello, world"
def perevorot(stroka):
    stroka2=""
    j=-1
    for i in stroka:
        j+=1
    for i in stroka:
        stroka2+=stroka[j]
        j-=1
    return stroka2
#я знаю, что такое len()

def perevorot2(stroka):
    stroka=stroka[::-1]
    return stroka

print(perevorot(stroka))
print(perevorot2(stroka))
#print(stroka[::-1])