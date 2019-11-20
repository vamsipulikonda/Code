#include<stdio.h>
int main()
{
     int a,b,m,n,rem_m,rem_n,sum,count,judge=0;
    scanf("%d%d",&m,&n);
    
       
        count=0;
        while(m!=0 && n!=0)
        {
            rem_m=m%10;
            rem_n=n%10;
            if(judge==1)
            {
                rem_m++;
            }
            
            sum = rem_m+rem_n;
            
            if(sum>=10)
            {
                count++;
                judge++;
              
            }
            m=m/10;
            n=n/10;
        }
        if(count==0)
        {
            printf("No carry operation.\n");
        }
        else
        {
            printf("%d carry operations.\n",count);
        }
    
    return 0;
}