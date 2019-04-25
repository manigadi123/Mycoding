def throws():
    return 5/0
try:
    throws()
except ZeroDivisonError:
    print "divison by zero"
except Exception,err:
    print "caught an exception"

finally:
    print "Finally block is used for cleanup"
