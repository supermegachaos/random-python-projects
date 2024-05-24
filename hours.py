xh = input("Enter Hours:")
xr = input("Enter Rate:")
xp= float(xh) * float (xr)
xo= float(xh)-40
def computePay():
    if xo >= 0:
        xp = (40 * float(xr)) + (xo * float(xr) * 1.5)
        print( "Overtime: " + str(xo) + " Hours")
        print("")
        print("Overtime rate " + str(float(xr)) + " dollars")
        print("")
        print("pay:",xp)
    else:
        print ("pay:",xp)


computePay()
