#include<stdio.h>

void DisplayFactors(int);

int main()
{
    int iNo = 0;
    
    printf("Enter number\n");
    scanf("%d",&iNo);
    
    DisplayFactors(iNo);
    
    return 0;
}

void DisplayFactors(int iValue)
{
    int iCnt = 0;   // Loop Counter
    if(iValue < 0)
    {
        iValue = -iValue;
    }
    //          1             2                 3
    for(iCnt = 1; iCnt <= (iValue/2); iCnt++)        // O(N/2)
    {
            if((iValue % iCnt) == 0)    // ICnt is a factor
            {
                printf("%d\n",iCnt);
            }
    }
}

















