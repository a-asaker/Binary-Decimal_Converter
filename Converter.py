#!/usr/bin/env python3

# Coded By :: A_Asaker

from os import system
from sys import platform

def ToDecRat(num,base):
	conv_num=0
	n=0
	for x in num:
		n=n+1
		if base==16:
			if x=="a":
				x=10
			if x=="b":
				x=11
			if x=="c":
				x=12
			if x=="d":
				x=13
			if x=="e":
				x=14
			if x=="f":
				x=15
		conv_num=conv_num+(int(x)*(base**(-n)))
	num=str(conv_num)
	return num[num.find('.')+1:]

def ToDecNat(num,base):
	if base==16:
		return str(int(num,16))
	else:	
		conv_num=0
		n=len(num)
		for x in num:
			n=n-1
			conv_num=conv_num+(int(x)*(base**(n)))
		return conv_num

def FrmDecNat(num,base):
	if base==2:
		return bin(int(num))[2:]
	if base==8:
		return oct(int(num))[2:]
	if base==16:
		return hex(int(num))[2:]
	else:
		return "Error!"

def FrmDecRat(num,base):
	conv_num=""
	num=float(num)
	if num != 0.0 :
		for i in range(18):
			num = float(num)*base
			conv,num=str(num).split(".")
			if base==16:
				if conv=="10":
					conv="a"
				if conv=="11":
					conv="b"
				if conv=="12":
					conv="c"
				if conv=="13":
					conv="d"
				if conv=="14":
					conv="e"
				if conv=="15":
					conv="f"
			conv_num+=conv
			num="."+num
		return conv_num
	else: 
		return 0

def FrmDec(base):
	num=input("\n Enter The Decimal Number : ").strip()
	if num.find(".")==-1:
		return FrmDecNat(num,base)
	elif num.find(".")==0:
		num_nat=0
		num_rat=num[num.find("."):]
		Dec=str(num_nat)+"."+str(FrmDecRat(num_rat,base))
		return Dec
	else:
		num_nat=num[:num.find(".")]
		num_rat=num[num.find("."):]
		Dec=str(FrmDecNat(num_nat,base))+"."+str(FrmDecRat(num_rat,base))
		return Dec

def ToDec(base):
	num=""
	if base==2:
		num=input("\n Enter The Binary Number : ").strip()
	elif base==8:
		num=input("\n Enter The Octal Number : ").strip()
	elif base==16:
		num=input("\n Enter The Hexa-Decimal Number : ").strip()
	else:
		return "Error!"
	rat=num.find(".")
	if rat==-1:
		return ToDecNat(num,base)
	else:
		return(str(ToDecNat(num[:rat],base))+"."+str(ToDecRat(num[rat+1:],base)))

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
	print(" (3) Decimal To Octal")
	print(" (4) Octal To Decimal")
	print(" (5) Decimal To Hexa-decimal")
	print(" (6) Hexa-decimal To Decimal")
	print(" (7) Clear The Terminal [c]")
	print(" (0) Exit [q]","\n")
	x=input(" #=========# >( 1 || 2 || 3 || 4 || 5 || 6 || 7 || 0 ): ").strip()
	if x == '1':
		print(str_res.format(FrmDec(2)))
	elif x == '2':
		print(str_res.format(ToDec(2)))
	elif x=='3':
		print(str_res.format(FrmDec(8)))
	elif x=='4':
		print(str_res.format(ToDec(8)))
	elif x=='5':
		print(str_res.format(FrmDec(16)))
	elif x=='6':
		print(str_res.format(ToDec(16)))
	elif str(x)=="7" or str(x).lower()=='c':
		if platform.lower()=="windows":
			system("cls")
		else :
			system("clear")
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
