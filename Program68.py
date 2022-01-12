
def SumEven(iNo):
	idigit,iSum=0,0

	while(iNo!=0):
		idigit=iNo%10
		if((idigit%2)==0):
			iSum=iSum+idigit
		iNo=int(iNo/10)

	return iSum

def main():
	iValue,iRet=0,0;

	print("Enter Number")
	iValue=int(input())

	iRet=SumEven(iValue)
	print("Sum of even digits are :",iRet)

if __name__=="__main__":
	main()