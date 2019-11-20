
#include <stdio.h>
#include<string.h>


int main()
{
    int i,j;
    char a[100],b[100];
    gets(a);
    gets(b);
    int s1=strlen(a);
    int s2=strlen(b);
    if(s1!=s2)
    {
        printf("Not anagram");
        return 0;
    }
    for(i=0;i<s1;i++)
    {
    for( j=i+1;j<s1;j++)
    {
        if (a[i]<a[j])
        {
            int temp;
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
        if (b[i]<b[j])
        {
            int temp;
            temp=b[i];
            b[i]=b[j];
            b[j]=temp;
        }
    }
    }
    for(i=0;i<s1;i++)
    {
        if(a[i]!=b[i])
        {
            printf("not anagram");
            return 0;
        }
    }
    printf("it is anagram");

    return 0;
}
