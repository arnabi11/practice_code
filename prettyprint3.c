#include <stdio.h>



int main()

{

    int i, j, N;



    printf("Enter N: ");

    scanf("%d", &N);



    for(i=1; i<=N; i++)

    {

        for(j=i; j<=(i*i); j += i)

        {

            printf("%-3d", j);

        }



        printf("\n");

    }



    return 0;

}
