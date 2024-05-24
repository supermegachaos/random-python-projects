def computePay():
    xh = input("Enter Hours:")
    xr = input("Enter Rate:")
    xp= float(xh) * float (xr)
    xo= float(xh)-40
    if xo >= 0:
        xp = (40 * float(xr)) + (xo * float(xr) * 1.5)
        print( "Overtime: " + str(xo) + " Hours")
        print()
        print("Overtime rate " + str(float(xr)*1.5) + " dollars")
        print()
        print("pay:",xp)
    else:
        print("Regualr hours " + str(float(xh)))
        print()
        print("Hourly rate " + str(float(xr)) + " Dollars")
        print()
        print ("pay:",xp)


computePay()
