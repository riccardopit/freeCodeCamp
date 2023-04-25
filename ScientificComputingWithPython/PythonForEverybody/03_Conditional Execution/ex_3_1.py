hours = input("Enter hours: ")
h = float(hours)    #hours
rate = input("Enter rate: ")
r = float(rate)    #rate
ot_k = 1.5  #overtime rate factor

if h > 40:
    ot_r = r * ot_k #overtime rate
    ot_pay = (h - 40) * ot_r    #overtime pay
    pay = 40 * r + ot_pay   #pay
else:
    pay = h * r #pay

print(pay)