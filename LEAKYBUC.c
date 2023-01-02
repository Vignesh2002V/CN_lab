#include<stdio.h>
#include<conio.h>
void main()
{
  int bucketsize,packets,oprate,buffer,n;
  printf("Enter the bucket size\n");
  scanf("%d",&bucketsize);

  printf("Enter the output rate\n");
  scanf("%d",&oprate);
  buffer=0;
  n=0;
  while(n<5)
  {
    printf("Enter the input stream of packets\n");
    scanf("%d",&packets);
    buffer=buffer+packets;
    if(buffer>=bucketsize)
    {
     printf("%d",buffer);
     printf("Bucket Full\n");
     break;
    }
    else
    {
     buffer=buffer-oprate;
     printf("%d\n",buffer);
     n=n+1;
    }
    getch();

  }

}
