class Myerror(object):
    '''my own excption class
Attributes:
msg -- explanation of the error
'''
    def __init__(self,msg):
        self.msg=msg

error=Myerror("something wrogh")
