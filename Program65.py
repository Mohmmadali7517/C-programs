
def CountDigit(iNo):
	iCnt=0

	while(iNo!=0):
		iCnt=iCnt+1
		iNo=int(iNo/10)

	return iCnt

def main():
	iValue,iRet=0,0

	print("Enter Number")
	iValue=int(input())

	iRet=CountDigit(iValue)
	print("number of digits are :",iRet)

if __name__=="__main__":
	main()