
def Reverse(iNo):
	idigit,iRev=0,0

	while(iNo!=0):
		idigit=iNo%10
		iRev=(iRev*10)+idigit
		iNo=int(iNo/10)

	return iRev
	
def main():
	iValue,iRet=0,0

	print("Enter Number")
	iValue=int(input())

	iRet=Reverse(iValue)
	print("Reverse number is :",iRet)

if __name__=="__main__":
	main()