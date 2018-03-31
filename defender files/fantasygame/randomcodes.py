n = 0
while n <= 33:
	months = "JanFebMarAprMayJunJulAugSepOctNovDec"
	n = 3 * (int(input("enter a month number: "))-1)
	print (n)
	print(months[n:n+3])
	
	
	
1)
tuple
list
array
library


x={}

x["Melee"] = 4
x["Range"] = 6
x["Magic"] = 10
x["Special"] = 22


print(x)
#print(x["Melee"])
#print(x["Magic"])

for att in x:
	print(att + " = " + str(x[att]))
	
if "Special" in x:
	print("Special attack = " + str(x["Special"]))
else:
	print("This Character has no special attacks")
	


