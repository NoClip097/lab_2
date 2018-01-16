massiv=[8,2,4,6]
def minimum(massiv):
    m=massiv[0]
    for i in massiv:
        if i<m:
            m=i
    return m

print(minimum(massiv))
print(min(massiv))

def srednee(massiv):
    s=n=0
    for i in massiv:
        s+=i
        n+=1
    return s/n

print(srednee(massiv))


