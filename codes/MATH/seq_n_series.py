def APs_smallest_common_ele(a : int, b : int, c : int, d : int) -> int:
    """
        Smallest Common Element
        =======================
        Finds smallest common element of the Arithmetic Progressions (APs) whose initial terms and common differences are given
        AP 1: a + (n-1)*b
        AP 2: b + (m-1)*d
        
        Parameters
        ----------
        a : int -> initial term of first AP
        b : int -> common difference of first AP
        c : int -> initial term of second AP
        d : int -> common difference of second AP

        Returns
        -------
        int : first common term (first intersection) of 2 APs which satisfies (a+(n-1)*b = c+(m-1)*d) if exists, else -1
    """

    if a == c: return a
    if a > c: a,b,c,d = c,d,a,b

    for y in range(b):
        if not ((c - a) % b + y*d) % b: return c+y*d
    return -1