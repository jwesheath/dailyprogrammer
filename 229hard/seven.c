#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int rev(int num)
{
    int rev = 0;
    while(num > 0)
    {
        rev *= 10;
        rev += num % 10;
        num /= 10;
    }

    return rev;
}

int main(int argc, char* argv[]) 
{
    int e = atoi(argv[1]);
    unsigned long long int result = 0;

    for(int i = 0; i < pow(10, e); i += 7)
    {
        if(rev(i) % 7 == 0)
        {
            result += i;
        }
    }

    printf("%llu\n", result);

    return 0;
}