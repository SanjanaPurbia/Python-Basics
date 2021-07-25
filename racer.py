# to calc prize benefits of a racer
RD=int(input("Enter racing distance covered:"))

if RD>=1000:
    rate=2.5
    sup_prize=1250
    print("-----keep supliment of 5 KG")
elif RD>=700:
    rate=2.0
    sup_prize=800
    print("-----keep supliment of 4 KG")
elif RD>=400:
    rate=1.5
    sup_prize=450
    print("-----keep supliment of 3 KG")
else:
    rate=1.0
    sup_prize=200
    print("-----keep supliment of 2 KG")
cash=RD*rate
print("cash prize: %0.2f Rs with health benefit of %d Rs"\
      %(cash,sup_prize))