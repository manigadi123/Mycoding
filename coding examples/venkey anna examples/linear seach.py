l=list(input("enter a list"))
item=int(input("Enter the number to ne search"))
count=0
for i in range(0,len(l)-1):
	if (int(l[i])==item):
		print("item found at the location:",str(i+1))
		count=1
		break
	   
