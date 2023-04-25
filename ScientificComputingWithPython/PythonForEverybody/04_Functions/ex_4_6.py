def computepay(H,R):
    ot_k = 1.5  #overtime rate factor
    if H > 40:
        ot_r = R * ot_k #overtime rate
        ot_pay = (H - 40) * ot_r    #overtime pay
        pay = 40 * R + ot_pay   #pay
    else:
        pay = h * r #pay
    return pay

hours = input("Enter hours: ")
h = float(hours)    #hours
rate = input("Enter rate: ")
r = float(rate)    #rate
p = computepay(h,r) #pay
print("Pay",p)