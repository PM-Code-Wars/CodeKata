Description:
Consider integer coordinates x, y in the Cartesian plan and three functions f, g, h defined by:

f: 1 <= x <= n, 1 <= y <= n --> f(x, y) = min(x, y)   - this is used to populate the cartesian plane, if x is less than y, then x value is used for a cell, otherwise y
g: 1 <= x <= n, 1 <= y <= n --> g(x, y) = max(x, y)   - opposite of g:	
h: 1 <= x <= n, 1 <= y <= n --> h(x, y) = x + y       - f+g


where n is a given integer (n >= 1, guaranteed) and x, y are integers.

In the table below you can see the value of the function f with n = 6.

---	0	1	2	3	4	5	6
6	-	1	2	3	4	5	6	
5	-	1	2	3	4	5	5	
4	-	1	2	3	4	4	4	
3	-	1	2	3	3	3	3	
2	-	1	2	2	2	2	2	
1	-	1	1	1	1	1	1	
0	-	-	-	-	-	-	-

The task is to calculate the sum of f(x), g(x) or h(x) for all integers x and y such that (1 <= x <= n, 1 <= y <= n).

The function sumin (sum of f) will take n as a parameter and return the sum of min(x, y) in the domain 1 <= x <= n, 1 <= y <= n. The function sumax (sum of g) will take n as a parameter and return the sum of max(x, y) in the same domain. The function sumsum (sum of h) will take n as a parameter and return the sum of x + y in the same domain.

Examples:

sumin(6) --> 91
sumin(45) --> 31395
sumin(999) --> 332833500
sumin(5000) --> 41679167500

sumax(6) --> 161
sumax(45) --> 61755
sumax(999) --> 665167500
sumax(5000) --> 83345832500

sumsum(6) --> 252
sumsum(45) --> 93150
sumsum(999) --> 332833500
sumsum(5000) --> 125025000000
Hint:

Try to avoid nested loops - this is very important, as CodeWars will reject your solution if its run time is too long.
Note that h = f + g
