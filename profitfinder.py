'''
hello world
'''
   
def percentcalc(inv):
    thismonth=inv*0.08
    print("This month profit: {}".format(thismonth))
    return thismonth

def monthlyprofbonus(prc):
    proftbon=prc*0.07
    print("Profit bonus: {}".format(proftbon))
    return proftbon
    
def addamount(inv):
    perc=percentcalc(inv)
    mpb=monthlyprofbonus(perc)
    addedamount=inv+perc+mpb+50000
    return addedamount
 
print("Hello World")
inv=int(input("Enter amount: "))
bonus=inv*0.1
inv=inv+bonus
i=int(input("Enter amount of months: "))
for a in range(i):
    print("\n \nMonth {} : {}".format(a+1,inv))
    inv=addamount(inv)
