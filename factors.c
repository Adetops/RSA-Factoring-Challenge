#include <stdio.h>
#include <stdlib.h>

int trial_div(long int n);

/**
 * Find the smallest divisor, if any, of a given number `n`
 * Returns: smallest divisor if found, 0 if n is prime
 */
int trial_div(long int n)
{
	long int f;

	if (n % 2 == 0)
	{
		printf("%lu=%lu*%i\n", n, n / 2, 2);
		return 0;
	}

	f = 3;
	while (f * f <= n)
	{
		if (n % f == 0)
		{
			printf("%lu=%lu*%lu\n", n, n / f, f);
			return (0);
		}
		else
		{
			f += 2;
		}
	}
	printf("%lu =%lu*%i\n", n, n, 1);
	return (0);
}

/**
 * main - main code
 * Return: Always 0
 */
int main(int argc, char **argv)
{
	(void) argc;
	FILE *file;
	char line[100];
	long int n, i = 0;

	file = fopen(argv[1], "r");

	if (file == NULL)
	{
		printf("Failed to open the file.\n");
		return 1;
	}

	while (fgets(line, sizeof(line), file) != NULL)
	{
		n = atoi(line);
		trial_div(n);
		i++;
	}
	fclose(file);

	return (0);
}
