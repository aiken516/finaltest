def piNum(num):
    pi = 0.0;
    for i in range(1, num+1):
        pi += float(((-1)**(i+1)))/float(((2*i)-1)) * 4
    return pi


print("i\tm(i)")
for j in range(1, 902):
    print("{0:d}\t{1:.4f}".format(j, piNum(j)))
    

