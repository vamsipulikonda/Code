
#include <stdio.h>
#include<string.h>
int checkvow(char );

int main()
{
    int i,j=0;
    char vow[20],name[20];
    scanf("%s",name);
    for(i=0;name[i]!='\0';i++)
    {
        if(checkvow(name[i])==0)
        {
            vow[j]=name[i];
            j++;
            
        }
     
    }
       name[j]='\0';
       strcpy(name,vow);
       printf("%s",vow);
       
    return 0;
}
int checkvow(char ch)
{
    if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'){
        return 1;
    }
    else
    {
        return 0;
    }
}

