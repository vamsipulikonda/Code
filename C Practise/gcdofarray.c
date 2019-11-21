#include<stdio.h>
int max(int a, int b){
	if(a>b){
		return a;
	}
	return b;
}
int calcGCD(int a, int b){
	int g;
	int m=max(a, b);
	for(int i=1;i<m;++i){
		if((a%i==0)&&(b%i==0)){
			g=i;
		}
	}
	return g;
}
int main(){
	int k,a[10],n=3,sum=0;
	scanf("%d\n", &k);
	for(int i=0;i<n;i++){
		scanf("%d ", &a[i]);
	}
	for(int j=0;j<n;j++){
		sum+=calcGCD(k, a[j]);
	}
	printf("%d", sum);
  return 0;
}