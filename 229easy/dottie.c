#include <stdio.h>
#include <math.h>

int fact(int x) 
{
	if (x == 1) return x; 
	else return x * fact(x - 1);
}

double absolute(double x)
{
	return x * ( (x < 0) * -1 + (x > 0) );
}

double cosTaylor(double x)
{
	double result = 1;
	double term;
	int i = 2;	
	int step = 1;

	while(1)
	{
		if (step % 2 == 0)
		{
			term = pow(x, i) / fact(i);
		}
		else
		{
			term = pow(x, i) / fact(i) * -1;
		}

		if (absolute(term) < 0.0001)
		{
			break;
		}

		result += term;
		i += 2;
		step += 1;
	}

	return result;

}

int main(void) 
{
	double num = cosTaylor(2);
	printf("%f\n", num);
}
