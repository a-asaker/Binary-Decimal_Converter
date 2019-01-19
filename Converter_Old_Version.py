#!/usr/bin/env python3
# Coded By : A_Asaker
#Use The New Version ,, This One Is An Old And Not Completed [:)
import os
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
	num=input("\n Enter The Decimal Number : ").strip()
	print("")
	if num.find("-")==-1:
		return IsDec(num)
	elif num.find("-")==0:
		return "-"+IsDec(num[1:])
	else:
		return " Not A Valid Decimal Number ! "


def IsDec(num):
	if str(num).count('.')<=1:
		bol=0
		for char in num:
			if char not in ('0','1','2','3','4','5','6','7','8','9','.'):
				bol=0
				break
			else:
				bol=1
		while bol==0:
			num=input("\n Please Enter A Positive Decimal Number : ").strip()
			for char in num:
				if char not in ('0','1','2','3','4','5','6','7','8','9','.'):
					bol=0
					break
				else:
					bol=1
		return DecToBin(num)
	else:
		return " Not A Valid Decimal Number ! "

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
	num=input("\n Enter The Binary Number : ").strip()
	print("")
	if num.find("-")==-1:
		return IsBin(num)
	elif num.find("-")==0:
		return "-"+str(IsBin(num[1:]))
	else :
		return " Not A Valid Binary Number ! "

def IsBin(num):
	if str(num).count('.')<=1:
		bol=0
		for z in num:
			if z not in('0','1','.'):
				bol=0
				break
			else:
				bol=1
		while bol==0:
			num=input("\n Please Enter A Binary Number : ").strip()
			for z in num:
				if z not in('0','1','.'):
					bol=0
					break
				else:
					bol=1
		return BinToDec(num)
	else:
			return  " Not A Valid Binary Number ! "

def DecToOct():
	dec_num=input("\n Enter The Decimal Number : ").strip()
	if (dec_num.isnumeric()):
		return str(oct(int(dec_num)))[2:]

def OctToDec():
	dec_num=input("\n Enter The Octal Number : ").strip()
	if (dec_num.isnumeric()):
		return str(int(dec_num,8))

def DecToHex():
	dec_num=input("\n Enter The Decimal Number : ").strip()
	is_float=0
	if (dec_num.isnumeric() or dec_num.find(".")):
		try :
			int(dec_num)
			is_float=0
		except ValueError:
			is_float=1
	if (is_float==0):
		return str(hex(int(dec_num)))
	elif(is_float==1):
		return str(float.hex(float(dec_num)))

def HexToDec():
	dec_num=input("\n Enter The Hexa-decimal Number : ").strip()
	if (dec_num[0:2].lower()=="0x"):
		try :
			return str(int(dec_num,16))
		except ValueError:
			return str(float.fromhex(dec_num))

str_res='''   ---------------------------\n ==> | {} |\n   ---------------------------
______________________________________________________________________________
______________________________________________________________________________
'''

def main():
	print('''
 ┌────────────────────┐
 │  ＯＰＴＩＯＮＳ  ：│
 └────────────────────┘
		''')
	print(" (1) Decimal To Binary")
	print(" (2) Binary To Decimal")
	print(" (3) Decimal To Octal [Natural Numbers Only]")
	print(" (4) Octal To Decimal [Natural Numbers Only]")
	print(" (5) Decimal To Hexa-decimal")
	print(" (6) Hexa-decimal To Decimal")
	print(" (7) Clear The Terminal [c]")
	print(" (0) Exit [q]","\n")
	x=input(" #===================# >( 1 || 2 || 3 || 4 || 5 || 0 ): ").strip()
	if x == '1':
		print(str_res.format(IsMinusDec()))
	elif x == '2':
		print(str_res.format(IsMinusBin()))
	elif x=='3':
		print(str_res.format(DecToOct()))
	elif x=='4':
		print(str_res.format(OctToDec()))
	elif x=='5':
		print(str_res.format(DecToHex()))
	elif x=='6':
		print(str_res.format(HexToDec()))
	elif str(x)=="7" or str(x).lower()=='c':
		os.system("clear")
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
