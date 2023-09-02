# nhap ham can tinh
import math
def f(x):
    return math.exp(x) - 2

def bisection(x0,x1,e):
    step = 1
    print('\n\n*** bisection method ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nRequired Root is : %0.8f' % x2)



x0 = float(0)
x1 = float(2)
e = float(0.01)

if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else: # nhap a,b, h
    bisection(x0,x1,e)

