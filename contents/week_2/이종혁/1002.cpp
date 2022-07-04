// boj 1002 터렛
// sliver 3

#include<stdio.h>
#include<math.h>



int main(void)
{
	int x, y, x1, y1, x2, y2,r,r1, r2,n;
	double d;
	int diff1, diff2;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
	{
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
		diff1 = (x2 - x1);
		diff2 = (y2 - y1);
		d = sqrt(diff1 * diff1 + diff2 * diff2);
		r = abs(r2 - r1);
		
		if (d == r1 + r2)
		{
			printf("1\n");
		}
		else if (d>r && d < r1 + r2 )
		{
			printf("2\n");
		}
		else if (d > r1 + r2)
		{
			printf("0\n");
		}
		else if (x1 == x2 && y1 == y2 && r1 != r2)
		{
			printf("0\n");
		}
		else if (x1 == x2 && y1 == y2 && r1 == r2)
		{
			printf("-1\n");
		}
		else if (d != 0 && d==r)
		{
			printf("1\n");
		}
		else
		{
			printf("0\n");
		}
		
	}

}