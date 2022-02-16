import numpy as np
import codes.MATH.manager as mngr

    

# METHOD 1 :
@mngr.MathDecor
def Congruent_Modulo(List : list, N : int) -> dict:
    """CONGRUENT_MODULO :- Groups 'List' elements giving identical modulus value w.r.t. 'Number'"""
    ModDict = {}
    for i,Ele in enumerate([i%N for i in List]): ModDict[Ele] = ModDict.get(Ele, []) + [List[i]]

    return ModDict



# METHOD 2 :
@mngr.MathDecor
def Sieve(Number : int) -> list:
    """SIEVE OF ERASTOSTHENES :- Computes Sieve of Eratosthenes"""

    primes = dict.fromkeys([2] + [i for i in range(3, Number+1, 2)], 1)
    Number = int(round(float(Number)))
    if Number<2: return []
    if (Number == 2): return [2]
    
    for i in range(2, Number+1):
      for j in range(i*2, Number+1, i):
        if primes.get(j, 0): primes[j] = 0
        
    return list(filter(lambda key: primes[key], primes.keys()))




# METHOD 3 :
@mngr.MathDecor
def Prime_Factors(Number : int) -> list:
    """PRIME FACTORS :- Computes List of Prime Factors"""
    return [i for i in Sieve(int(Number)) if Number%i==0]





# METHOD 4 :
@mngr.MathDecor
def Prime_Check(Number : int) -> int:
    """PRIME CHECK :- Checks if a Number is Prime / Composite / Neither Prime nor Composite"""
    Number = int(float(Number))
    if Number<2: return -1              # Return -1 if Number is 1, 0 or negative
    if Number %  2 == 0: return int(Number==2)
    if Number % 10 == 5: return int(Number==5)
    
    sqrt = Number**0.5
    if(sqrt == int(sqrt)): return 0

    for i in range(3, int(sqrt+1), 2):
        if Number%i==0: return 0,i      # Return 0 if Number is Composite
    return 1                            # Return 1 if Number is Prime





# METHOD 5 :
@mngr.MathDecor
def Co_Prime(Number_1 : int, Number_2 : int) -> bool:
    """CO-PRIME :- Checks Whether Given Pair of Numbers are Co-Prime"""
    Number_1, Number_2 = int(float(Number_1)), int(float(Number_2))
    if Number_1==1 or Number_2==1: return True
    
    return True if len(set(Prime_Factors(Number_1)).intersection(set(Prime_Factors(Number_2))))==0 else False





# METHOD 6 :
@mngr.MathDecor
def Signum(Number : int) -> int:
    """SIGNUM :- Checks Sign of Number in Range = { -1, 0, 1 }"""
    return 1 if Number>0 else 0 if Number==0 else -1





# METHOD 7 :
@mngr.MathDecor
def Chinese_Remainder_Theorem(Divisor_Array : list, Remainder_Array : list) -> int:
    """CHINESE REMAINDER THEOREM :- Implements CRT on Given Divisor and Remainder Arrays"""
    
    a, LNA = max(Remainder_Array), len(Divisor_Array)

    while True:      # Iterates 'a' from Max of Remainders to until we get 'a' satisfying all entries
        Counter = 0
        for i in range(LNA):
            if a % Divisor_Array[i] != Remainder_Array[i]: break
            Counter+=1
        if Counter == LNA: break
        a+=1
        
    return a 





# METHOD 8 :
@mngr.MathDecor
def Euler_Totient_Function(Number : int) -> int:
    """EULER TOTIENT FUNCTION :- Computes ETF for given Number"""
    Counter = 0
    for i in range(1, Number):
        if Co_Prime(i, Number): Counter += 1
    return Counter




# METHOD 9 :
@mngr.MathDecor
def Inverse_Euler_Totient_Function(Number : int) -> int:
    """INVERSE EULER TOTIENT FUNCTION :- Computes IETF for given Number"""
    Number = 1
    while True:
        if Euler_Totient_Function(Number) == Number: return Number
        Number += 1





# METHOD 10 :
@mngr.MathDecor
def Determinant(Mat : list) -> int:
    """JUST ONE LINE DETERMINANT CALCULATOR :- Calculates Determinant of given Matrix"""
    return Mat[0][0] if len(Mat)==1 else sum([Mat[ignoR][0] * (-1)**ignoR * Determinant(np.concatenate((Mat[:ignoR,1:],Mat[ignoR+1:,1:]))) for ignoR in range(len(Mat))])
    



# METHOD 11 :
MatN = { 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6,4,6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1,9,1] }
@mngr.MathDecor
def Last_Digit_Determiner(Base : int, Exponent : int) -> int:
    """PRINTS LAST DIGIT OF EXPONENTIAL RESULT :- Determines Last Digit of Result (Base ^ Exp)"""
    return 1 if Exponent==0 else MatN[(Base%10)][(Exponent%4)-1] if Base%10 not in [0,1,5,6] else Base%10
    # return MatN[Base-2][(Exponent%4)-1]




# METHOD 12 :
@mngr.MathDecor
def Josephus_Problem(Step : int, Sequence : list) -> int:
    """JOSEPHUS PROBLEM :- Theoretical problem related to a certain counting-out game"""
    i = Step-1
    while True:
        Len = len(Sequence)
        if Len <= 1: return Sequence[0]    
        if i >= Len: i -= Len

        del Sequence[i%Len]
        i += Step-1



import codes.MATH.combinatorics.Permutations_and_Combinations as PC #import Permutations, Combinations
# # METHOD 13 :
# @mngr.MathDecor
# def Permutations(Elements : list, Positions : int = -1, Allow_Repetitions : bool = False) -> set:
#     """PERMUTATIONS :- Returns List of All Possible Permutations of Input Data"""
#     if Positions == 0: return [[]*len(Elements)]
#     if Positions == -1: Positions = len(Elements)

#     return set((i,)+j for i in Elements for j in set(map(tuple, Permutations(Elements, Positions-1, Allow_Repetitions))) if (True if Allow_Repetitions is True else i not in j))





# # METHOD 14 :
# @mngr.MathDecor
# def Combinations(Elements : list, Positions : int = -1) -> list:
#     """COMBINATIONS :- Returns List of All Possible Combinations of Input Data"""
#     return list(map(list, set(map(frozenset, Permutations(Elements, Positions)))))





# METHOD 15 :
FibLib = {0:0}

@mngr.MathDecor
def Fibonacci(n : int) -> int:
    """FIBONACCI :- Provides fibonacci result upto 998
    n -> depicts element position in the fibonacci sequence
    """
    if n<2: return n
    if FibLib.get(n-1) is None: FibLib[n-1] = Fibonacci(n-1)
    return FibLib[n-1] + FibLib[n-2]




# METHOD 16 :
@mngr.MathDecor
def ModAll(List : list, Number : int) -> list:
    """MODALL :- Performs modulus(%) operation on given elements in 'List' w.r.t. 'Number'"""
    return [i%Number for i in List]
