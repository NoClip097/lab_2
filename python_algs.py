ivan = {
"name" : "ivan" ,
"age" : 34 ,
"children" : [{
"name" : "vasja" ,
"age" : 12 ,
}, {
"name" : "petja" ,
"age" : 10 ,
}],
}
darja = {
"name" : "darja" ,
"age" : 41 ,
"children" : [{
"name" : "kirill" ,
"age" : 21 ,
}, {
"name" : "pavel" ,
"age" : 15 ,
}],
}
emps = [ivan, darja]

def aged_children(emps,lim):
    for e in emps:
        for key,c in e.items():
            if key=='children':
                for ch in c:
                    for k,a in ch.items():
                        if k=='age':
                            #print(a)
                            if a>=lim:
                                print(e["name"])


aged_children(emps,18)
