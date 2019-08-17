#include<conio.h>
#include<stdio.h>
int main()
{
int i,n,rem[100];	
scanf("%d",&n);
i=0;
while(n>0)
{
	rem[i]=n%2;
	n=n/2;
	i++;
}
for(i=0;i<n;i++)
{
	printf("%d",rem[i]);
}	
return 0;	
}

	

