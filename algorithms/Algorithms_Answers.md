Add your answers to the Algorithms exercises here.

**Exercise I**:

a)  a = 0                       # O(1)
    while (a < n * n * n)       # O(n^3???)
      a = a + n * n

a)  a = 0                       # O(1)
    while (a < n * n)           # O(n^2???)
      a = a + n

a)  a = 0                       # O(1)
    while (a < n)               # O(n)
      a = a + 1                 # O(1)

O(n)

n*n*n
-----  = n 
 n*n


b)  sum = 0                                    # O(1)
    for (i = 0; i < n; i++)                    # O(n)
      for (j = i + 1; j < n; j++)              # O(1/2n) ==> O(n)
        for (k = j + 1; k < n; k++)            # O(n)
          for (l = k + 1; l < 10 + k; l++)     # O(1)
            sum++                              # O(1)

O(1) + O(n) * O(n) * O(n) * O(1) * O(1)
O(1) * O(n^3)
O(n^3)

i: 0
  j: 1 to n
i: 1
  j: 2 to n
i: 2
  j: 3 to n

for (l = k + 1; l < 10 + k; l++)
k     loop runs
---   -----------------------------
0     1 to 9,      for a total of 9
10    11 to 19,    for a total of 9
100   101 to 109,  for a total of 9


c)  bunnyEars = function(bunnies) {
      if (bunnies == 0) return 0
      return 2 + bunnyEars(bunnies-1)
    }

bunnyEars(n)


**Exercise II**:

Start in the middle floor. If the egg does not break go up one floor each time until it breaks. If the egg breaks go down one floor and check at which floor does the egg starts breaking.