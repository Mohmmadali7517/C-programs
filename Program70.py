
def CheckPallindrome(iNo):
	idigit,iRev=0,0
	iTemp=iNo

	while(iNo!=0):
		idigit=iNo%10
		iRev=(iRev*10)+idigit
		iNo=int(iNo/10)

	if(iRev==iTemp):
		return True

def main():
	iValue=0
	bret=False

	print("Enter number")
	iValue=int(input())

	bret=CheckPallindrome(iValue)

	if(bret==True):
		print(iValue,"is pallindrome number")
	else:
		print(iValue,"is not a pallindrome number")


if __name__=="__main__":
	main()