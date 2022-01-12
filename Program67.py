
def CountEven(iNo):
	iCnt,idigit=0,0

	if(iNo==0):
		return 1

	while(iNo!=0):
		idigit=iNo%10
		if((idigit%2)==0):
			iCnt=iCnt+1
		iNo=int(iNo/10)

	return iCnt;

def main():
	iValue,iRet=0,0

	print("Enter Number")
	iValue=int(input())

	iRet=CountEven(iValue)

	print("Number of even digits are :",iRet)

if __name__=="__main__":
	main()
