def accumulated_value(R, i, n):
    '''Formula for the accumulated value S of an ordinary simple annuity.

    Parameters
    ----------
    R : periodic payment value of the annuity
    i : interval rate per coversion period
    n : number of interest conversion periods during the term of an annuity

    Returns
    -------
    S : accumulated value of the annuity
    '''
    return R * ((1 + i) ** n - 1) / i


def periodic_payment(V, i, n, kind):
    '''Formula for the monthly payment of a ordinary simple annuity required to reach some amount S or A.

    Parameters
    ----------
    V : accumulated (or discounted) value of the annuity
    i : interval rate per coversion period
    n : number of interest conversion periods during the term of an annuity
    kind : string which must be either 'accumulated' or 'discounted' and denotes whether the amount provided is either
           accumulated or discounted. If a different string is given, then None is returned.

    Returns
    -------
    R : periodic payment value of the annuity
    '''
    if (kind == 'accumulated'):
        return V * (i / ((1 + i) ** n - 1))
    elif (kind == 'discounted'):
        return V * (i / (1 - (1 + i) ** -n))
    else:
        return None


def discounted_value(R, i, n):
    '''Formula for the discounted value S of an ordinary simple annuity.

    Parameters
    ----------
    R : periodic payment value of the annuity
    i : interval rate per coversion period
    n : number of interest conversion periods during the term of an annuity

    Returns
    -------
    A : discounted value of the annuity
    '''
    return R * (1 - (1 + i) ** -n) / i

def bisection(f,a,b,N):
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> bisection(f,1,2,25)
    1.618033990263939
    >>> f = lambda x: (2*x - 1)*(x - 3)
    >>> bisection(f,0,1,10)
    0.5
    '''
    if f(a)*f(b) >= 0:
        print("Bisection method fails, a solution is not guaranteed. f(a): " + str(f(a))+", f(b): " + str(f(b)))
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2


def find_interest_rate(V, R, n, kind):
    if kind == 'accumulated':
        i = bisection(lambda x: (((1+x)**n-1)/x)/(V/R)-1, 0.01, 0.99, 50)
        recalculated_V = accumulated_value(R, i, n)
    elif kind == 'discounted':
        i = bisection(lambda x: ((1-(1+x)**-n)/x)/(V/R)-1, 0.01, 0.99, 50)
        recalculated_V = discounted_value(R, i, n)
    else:
        return None
    error = V - recalculated_V
    print("Bisection method calculated i of " +str(i) + ", equalling value of "
            + str(recalculated_V) + " with error of " + str(error))
    return i