for a in range(1,500):
    for b in range(a,500):
        for c in range(b,500):
            if (pow(a,2)+pow(b,2) == pow(c,2)) and (a+b+c==1000):
                print(a,b,c)
                print(a*b*c)
