#!/usr/bin/env python3

def DecToBinNat(num):
	return bin(int(num))[2:]

def DecToBinRat(num):
	num=float(num)
	conv_num=""
	if num != 0.0 :
		while num!=1:
			num = num*2
			if num > 1 :
				num =num-1
				conv_num=str(conv_num)+"1"
			elif num==1:
				conv_num=str(conv_num)+"1"
				break
			else:
				conv_num=str(conv_num)+"0"
		return conv_num
	else: 
		return 0

def DecToBin(num):
	if num.find(".")==-1:
		return DecToBinNat(num)
	elif num.find(".")==0:
		num_nat=0
		num_rat=num[num.find("."):]
		Dec=str(num_nat)+"."+str(DecToBinRat(num_rat))
		return Dec
	else:
		num_nat=num[:num.find(".")]
		num_rat=num[num.find("."):]
		Dec=str(DecToBinNat(num_nat))+"."+str(DecToBinRat(num_rat))
		return Dec


def IsMinusDec():
	num=input("\n Enter The Decimal Number : ")
	print("")
	if num.find("-")==-1:
		return IsDec(num)
	elif num.find("-")==0:
		return "-"+IsDec(num[1:])
	else:
		return " Not A Valid Decimal Number ! "


def IsDec(num):
	bol=0
	for char in num:
		if char not in ('0','1','2','3','4','5','6','7','8','9','.'):
			bol=0
			break
		else:
			bol=1
	while bol==0:
		num=input("\n Please Enter A Positive Decimal Number : ")
		for char in num:
			if char not in ('0','1','2','3','4','5','6','7','8','9','.'):
				bol=0
				break
			else:
				bol=1
	return DecToBin(num)


def BinToDecNat(num):
	return int(num,2)


def BinToDecRat(num):
	conv_num=0
	n=0
	for x in num:
		n=n+1
		conv_num=conv_num+(int(x)*(2**(-n)))
	num=str(conv_num)
	return num[num.find('.')+1:]

def BinToDec(num):
	if num.find(".")==-1:
		return BinToDecNat(num)
	elif num.find(".")==0:
		num_nat=0
		num_rat=num[num.find(".")+1:]
		Dec=str(num_nat)+"."+str(BinToDecRat(num_rat))
		return Dec
	else:
		num_nat=num[:num.find(".")]
		num_rat=num[num.find(".")+1:]
		Dec=str(BinToDecNat(num_nat))+"."+str(BinToDecRat(num_rat))
		return Dec

def IsMinusBin():
	num=input("\n Enter The Binary Number : ")
	print("")
	if num.find("-")==-1:
		return IsBin(num)
	elif num.find("-")==0:
		return "-"+str(IsBin(num[1:]))
	else :
		return " Not A Valid Binary Number ! "

def IsBin(num):
	bol=0
	for z in num:
		if z not in('0','1','.'):
			bol=0
			break
		else:
			bol=1
	while bol==0:
		num=input("\n Please Enter A Binary Number : ")
		for z in num:
			if z not in('0','1','.'):
				bol=0
				break
			else:
				bol=1
	return BinToDec(num)

def main():
	print('''
 ┌────────────────────┐
 │  ＯＰＴＩＯＮＳ  ：│
 └────────────────────┘
		''')
	print(" (1) Decimal To Binary","\n")
	print(" (2) Binary To Decimal","\n")
	print(" (0) Exit","\n")
	x=input(" #===================# >( 1 || 2 || 0 ): ")
	if x == '1':
		print("   ---------------------------\n "," ==> | ",IsMinusDec()," |\n   ---------------------------")
		print('______________________________________________________________________________')
		print('______________________________________________________________________________')
	elif x == '2':
		print("   ---------------------------\n "," ==> | ",IsMinusBin()," |\n   ---------------------------")
		print('______________________________________________________________________________')
		print('______________________________________________________________________________')
	elif str(x)=='0' or x.lower()=="q":
		print('''
				┌──────────────────────────────────────┐
				│Ｃｏｄｅｄ  Ｂｙ  ：  Ａ＿Ａｓａｋｅｒ│
				└──────────────────────────────────────┘

			''')
		exit()
	else:
		print("\n Go Play Far Away ! \n")
		exit()


while 1:
	main()


''' converts from binary to deci
----------------------------------------
	Another Method (1):(Mine)
	conv_num=0
	n=len(num)
	for x in num:
		n=n-1
		conv_num=conv_num+(int(x)*(2**(n)))
	print(conv_num,"\n")
-----------------------------------------
	Another Method (2):
	num = input()
	conv_num = 0
	for x in num:
	     conv_num = conv_num*2 + int(x)
	print(conv_num)
	'''
