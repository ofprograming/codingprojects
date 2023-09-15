#include <stdio.h>
int count = 0 ;
int nnum = 0 ; 
int C = 1;
int numfind(int);
int oppnum(int);
void main()
{

int num  ;
printf("pls enter a num"); 
scanf("%d", num);
int temp=num;
numfind(temp);
oppnum(num);

}

int numfind(int num){
num=num/10;
count++;
if (num == 0 ){return 1; }
else{numfind(num); 
}}


int oppnum(int num){
int nnum = num%10 ;
num = num/10 ;
while (C =! 0){printf("%d", nnum);C--;} 
if(count==0 ){return 1;}
else{
    count--;
    C = count ;
    oppnum(num);}
}

