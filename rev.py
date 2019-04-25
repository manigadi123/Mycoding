def reverse_number(n): #10
    r = 0              #r=0
    while n > 0: #10>0:
        r *= 10   # 0*10=0
        r += n % 10 #0+=10%10 ===>0+=0
        n /= 10 #10/10=1
    return r

print(reverse_number(123))
