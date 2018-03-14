cidrs=[
0,
128,
192,
224,
240,
248,
252,
254,
255,
383,
447,
479,
495,
503,
507,
509,
510 ,
638,
702,
734,
750,
758,
762,
764,
765 ,
892,
956,
 988,
1003,
1013,
1017,
1019,
1020]
InputOctet1 = input ("Enter the first octet: ")
InputOctet2 = input ("Enter the second octet: ")
InputOctet3 = input ("Enter the third octet: ")
InputOctet4 = input ("Enter the fourth octet: ")
#doinit = input ("enter your ip xxx,xxx,xxx,xxx/xx:")
InputCidr = input ("Enter the cidr: ")
def Print(first,second,third,fourth,cyder):
	print("your IP is "+first+"."+second +"."+ third + "."+ fourth + "/" +cyder)
Print(InputOctet1,InputOctet2,InputOctet3,InputOctet4,InputCidr)
binary1 = [0,0,0,0,0,0,0,0]
binary2 = [0,0,0,0,0,0,0,0]
binary3 = [0,0,0,0,0,0,0,0]
binary4 = [0,0,0,0,0,0,0,0]
ip = [0,0,0,0,0,0,0,0 ,   0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0 ,       0,0,0,0,0,0,0,0]
Cidr = [0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0]
CidrInv = [0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0,     0,0,0,0,0,0,0,0]
networkaddress = [0,0,0,0,0,0,0,0 ,   0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0 ,       0,0,0,0,0,0,0,0]
broadcast=[0,0,0,0,0,0,0,0 ,   0,0,0,0,0,0,0,0,      0,0,0,0,0,0,0,0 ,       0,0,0,0,0,0,0,0]
math = []



Octet1 =int(InputOctet1)
Octet2 =int(InputOctet2)
Octet3 =int(InputOctet3)
Octet4 =int(InputOctet4)
Cyder =int(InputCidr)
Cyder =cidrs[Cyder]
fullip=Octet1+Octet2+Octet3+Octet4

#def ipfind(first,output):
	#x=0
	#while x !=32:
	#	first.pop(x)
		#first.extend([binary1[x]])
		#x=x+1
def superbinary(source,output):
	add = 0
	x = 0
	iteration = 0
	while x != 8:
		if (source - (128+add) >=0):
			add = add + 128
			output.pop(iteration) 
			output.insert(iteration,1)
		
		if (source - (64+add) >=0):
			add = add + 64
			output.pop(iteration+1) 
			output.insert(iteration+1,1)
		
		if (source - (32+add) >=0):
			add = add + 32
			output.pop(iteration+2) 
			output.insert(iteration+2,1)
		
		if (source - (16+add) >=0):
			add = add + 16
			output.pop(iteration+3) 
			output.insert(iteration+3,1)
		
		if (source - (8+add) >=0):
			add= add + 8
			output.pop(iteration+4) 
			output.insert(iteration+4,1)
			
		if (source - (4+add) >=0):
			add= add + 4
			output.pop(iteration+5) 
			output.insert(iteration+5,1)
		
		if (source - (2+add) >=0):
			add = add + 2
			output.pop(iteration+6) 
			output.insert(iteration+6,1)

		if (source - (1+add) >=0):
			add= add + 1
			output.pop(iteration+7) 
			output.insert(iteration+7,1)
		x=x+1
		iteration = iteration+8
def binary(source,output,add):

	more = 0
	if (source - (128+more) >=0):
		more = more + 128
		output.pop(0+add) 
		output.insert(0+add,1)
		
	if (source - (64+more) >=0):
		more = more + 64
		output.pop(1+add) 
		output.insert(1+add,1)
		
	if (source - (32+more) >=0):
		more = more + 32
		output.pop(2+add) 
		output.insert(2+add,1) 
		
	if (source - (16+more) >=0):
		more = more + 16
		output.pop(3+add) 
		output.insert(3+add,1)
		
	if (source - (8+more) >=0):
		more = more + 8
		output.pop(4+add) 
		output.insert(4+add,1)
		
	if (source - (4+more) >=0):
		more = more + 4
		output.pop(5+add) 
		output.insert(5+add,1)
		
	if (source - (2+more) >=0):
		more = more + 2
		output.pop(6+add) 
		output.insert(6+add,1)

	if (source - (1+more) >=0):
		more = more + 1
		output.pop(7+add) 
		output.insert(7+add,1)
def invert(source,output):

	y=0
	while y !=32:
		if source[y]==0:
			output.pop(y)
			output.insert(y,1)
		if source[y]==1:
			output.pop(y)
			output.insert(y,0)
		y=y+1
def andgate(source,second,output):
	
	x=0
	y=0
	for x in range (0,32):
			if(source[x]+second[x]==2):
				output.pop(x)
				output.insert(x,1)
				x=x+1
				y=y+1
def orgate(source,second,output):
	x = 0
	y = 0
	for x in range (0,32):
		if(source[x]+second[x]==1):
			output.pop(x)
			output.insert(x,1)
			x=x+1
			y=y+1
def hosts(first,second,output):
	print(hello)
binary(Octet1,ip,0)
binary(Octet2,ip,8)
binary(Octet3,ip,16)
binary(Octet4,ip,24)
superbinary(Cyder,Cidr)
invert(Cidr,CidrInv)
andgate(ip,Cidr,networkaddress)
orgate(ip,CidrInv,broadcast)
#addbinary(ip,Cidr)
print ('ip is {}'.format(ip))
print('the network address is {}'.format(networkaddress))
print('the broadcast is {}'.format(broadcast))
#print (math)





