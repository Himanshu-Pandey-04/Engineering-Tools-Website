

def DTC(Value, DT):           # DATA TYPE CONVERTER
    DTs = [int, float, list, tuple, dict]
    try: return DT(Value)
    except: return "error"
      



# METHOD : METHOD TO MAP ANOTHER METHOD TO A LIST OF INPUTS
#@decorator.decorator
def MathDecor(Function, *args, **kwargs):
    """APPLY A METHOD ON A SET/LIST/TUPLE OF ENTRIES"""
    
    import functools   #, decorator
    
    @functools.wraps(Function)
    def Wrapper(*args, **kwargs):
        #if isinstance(args, (list, tuple)):
        return Function(*args, **kwargs)
    return Wrapper





# METHOD 1 :
@MathDecor
def Sieve(Number : int):# -> list:
    """SIEVE OF ERASTOSTHENES :- Computes Sieve of Eratosthenes"""

    List, Number = [i for i in range(2,Number+1)], int(round(float(Number)))

    if Number<2: return [Number]
    
    for i in range(2,Number+1):
      for j in range(i*2, Number+1, i):
        if j in List: List.remove(j)
        
    return List




# METHOD 2 :
@MathDecor
def Prime_Factors(Number : int):
    """PRIME FACTORS :- Computes List of Prime Factors"""
    return [i for i in Sieve(int(Number)) if Number%i==0]





# METHOD 3 :
@MathDecor
def Prime_Check(Number : int):
    """PRIME CHECK :- Checks if a Number is Prime / Composite / Neither Prime nor Composite"""
    Number = int(float(Number))
    if Number<2: return -1                                                                                # Return -1 if Number is 1,0 or negative
   
    for i in range(Number**0.5+1):
        if Number%i==0: return 0      # Return 0 if Number is Composite
   
    return 1                          # Return 1 if Number is Prime





# METHOD 4 :
@MathDecor
def Co_Prime(Number_1 : int, Number_2 : int):
    """CO-PRIME :- Checks Whether Given Pair of Numbers are Co-Prime"""
    Number_1, Number_2 = int(float(Number_1)), int(float(Number_2))
    if Number_1==1 or Number_2==1: return True
    
    return True if len(set(Prime_Factors(Number_1)).intersection(set(Prime_Factors(Number_2))))==0 else False





# METHOD 5 :
@MathDecor
def Signum(Number : int):
    """SIGNUM :- Checks Sign of Number   Range = { -1, 0, 1 }"""
    return 1 if Number>0 else 0 if Number==0 else -1





# METHOD 6 :
@MathDecor
def Chinese_Remainder_Theorem(Divisor_Array : list, Remainder_Array : list):
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





# METHOD 7 :
@MathDecor
def Euler_Totient_Function(Number : int):
    """EULER TOTIENT FUNCTION :- Computes ETF for given Number"""
    Counter = 0
    for i in range(1, Number):
        if Co_Prime(i, Number): Counter += 1
    return Counter




# METHOD 8 :
@MathDecor
def Inverse_Euler_Totient_Function(Number : int):
    """INVERSE EULER TOTIENT FUNCTION :- Computes IETF for given Number"""
    Number = 1
    while True:
        if Euler_Totient_Function(Number) == Number: return Number
        Number += 1





# METHOD 9 :
@MathDecor
def Determinant(Mat : list):
    """JUST ONE LINE DETERMINANT CALCULATOR :- Calculates Determinant of given Matrix"""
    return Mat[0][0] if len(Mat)==1 else sum([Mat[ignoR][0] * (-1)**ignoR * Determinant(np.concatenate((Mat[:ignoR,1:],Mat[ignoR+1:,1:]))) for ignoR in range(len(Mat))])
    



# METHOD 10 :
MatN = { 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6,4,6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1,9,1] }
@MathDecor
def Last_Digit_Determiner(Base : int, Exponent : int):
    """PRINTS LAST DIGIT OF EXPONENTIAL RESULT :- Determines Last Digit of Result (Base ^ Exp)"""
    return 1 if Exponent==0 else MatN[(Base%10)][(Exponent%4)-1] if Base%10 not in [0,1,5,6] else Base%10
    # return MatN[Base-2][(Exponent%4)-1]




# METHOD 11 :
@MathDecor
def Josephus_Problem(Step : int, Sequence : list):
    """JOSEPHUS PROBLEM :- Theoretical problem related to a certain counting-out game"""
    i = Step-1
    while True:
        Len = len(Sequence)
        if Len <= 1: return Sequence[0]    
        if i >= Len: i -= Len

        del Sequence[i%Len]
        i += Step-1




# METHOD 12 :
@MathDecor
def Permutations(Elements : list, Positions=-1, Allow_Repetitions = False):
    """PERMUTATIONS :- Returns List of All Possible Permutations of Input Data"""
    if Positions == 0: return [[]*len(Elements)]
    if Positions == -1: Positions = len(Elements)

    return set((i,)+j for i in Elements for j in set(map(tuple, Permutations(Elements, Positions-1, Allow_Repetitions))) if (True if Allow_Repetitions is True else i not in j))





# METHOD 13 :
@MathDecor
def Combinations(Elements : list, Positions=-1):
    """COMBINATIONS :- Returns List of All Possible Combinations of Input Data"""
    return list(map(list, set(map(frozenset, Permutations(Elements, Positions)))))





# METHOD 14 :
FibLib = {0:0}
@MathDecor
def Fibonacci(n):
    """FIBONACCI :- Provides fibonacci result
    n -> depicts element position in the fibonacci sequence
    """
    if n<2: return n
    if FibLib.get(n-1) is None: FibLib[n-1] = Fibonacci(n-1)
    return FibLib[n-1] + FibLib[n-2]




# METHOD 15 :
@MathDecor
def ModAll(List, Number):
    """MODALL :- Performs modulus(%) operation on given elements in 'List' w.r.t. 'Number'"""
    return [i%Number for i in List]

# print(ModAll([783, -217, 464, -108, 367], 11))



# METHOD 16 :
@MathDecor
def Congruent_Modulo(List, N):
    """CONGRUENT_MODULO :- Groups 'List' elements giving identical modulus value w.r.t. 'Number'"""
    ModDict = {}
    for i,Ele in enumerate([i%N for i in List]):  ModDict[Ele] = ModDict.get(Ele, []) + [List[i]]

    return ModDict


# print(ModAll([783, -217, 464, -108, 367], 11))






# import StrCollection, MathCollection


# P = StrCollection.Collections()
Func_Lib = { "1" : Sieve, "2": Prime_Factors, "3": Prime_Check, "4": Co_Prime, "5": Signum, "6": Chinese_Remainder_Theorem, "7": Euler_Totient_Function, "8": Inverse_Euler_Totient_Function, "9": Determinant, "10": Last_Digit_Determiner, "11": Josephus_Problem, "12": Permutations, "13": Combinations, "14": Fibonacci, "15": ModAll }

def Get_Funcs_Dict(): return Func_Lib


###########     MENU     ###########
def Function_Menu(Func_Library = Func_Lib):
    import sys, traceback, time #,numpy as np
    import inspect

    Func_Lib = Func_Library
    
    def Message(Header, Str): print(Header + Str)


    try:
        while True:
        
            time.sleep(2)
            print("\n\n %20s" %"MENU \n")
            print(f"    0. Exit")
        
            for FuncNumber, Func in Func_Lib.items():
                print(f"\n    %-2s. %-70s :   %-40s"%(FuncNumber, str(Func.__name__).replace('_',' ') + str(inspect.signature(Func)).replace('_', ' '), Func.__doc__))

            Types = { "int": int, "float": float, "str": str, "dict": dict, "list": list, "tuple": tuple, "set": set, "range": range }
            
            Choice = input("\n\n  CHOICE : ").strip()
            
            if Choice == '0': sys.exit(0)
            
            Func = Func_Lib[Choice]
            SigList = str(inspect.signature(Func))[1:-1].split(',')
           
            if SigList != ['']:       
                Inputs = []
                for Arg in SigList:
                    Colon = Arg.find(':')
                    Type, Param = Arg[Colon+1:].strip(), (Arg[: Colon] if Colon != -1 else Arg).replace('_', ' ').strip()

                    if Colon == -1: Inputs.append(input(Param + ':'))
                    elif Type in ["int", "float"]: Inputs.append(Types[Type](float(input(Param + ': '))))
                    elif Type == "str": Inputs.append(Types[Type](input(Param + ': ').strip()))
                    else: Inputs.append(Types[Type](input(Param + ': ').strip().split()))
                
                   # if Inputs[-1] == '.' and Arg.find('=')!=-1: Inputs[-1] = Arg[Ar]

                Output = str(Func(*Inputs))
                
            else: Output = str(Func())
            
            if Output != "None": Message("\n  OUTPUT : ", Output)
           
    except : traceback.print_exc()#P.Message("WARNING : ", "Sorry! Something Went Wrong")

'''

def Function_Menu(c):
    import sys, traceback #,numpy as np
    from inspect import signature
    
    def Message(Header, Str): print(Header + Str)


    while True:
        try:
            Input1, Input2 = None, None       # Options
            InputList = []
      
            print("\n\n %20s" %"MENU \n")
            print(f"    0. Exit")
        
            for FuncNumber, Func in Func_Lib.items():
                print(f"\n    %-2s. %-70s :   %-40s"%(FuncNumber, str(Func.__name__).replace('_',' ') + str(signature(Func)).replace('_', ' '), Func.__doc__))


            Types = { "int": int, "float": float, "str": str, "dict": dict, "list": list, "tuple": tuple, "set": set, "range": range }
            
            Choice = input("\n\n  CHOICE : ").strip()
            if Choice is '0': sys.exit(0)
            
            Func = Func_Lib[Choice]

            SigList = str(signature(Func))[1:-1].split(',')

            Inputs = []
            for Arg in SigList:
                Colon = Arg.find(':')
                Type, Param = Arg[Colon+1:].strip(), (Arg[: Colon] if Colon != -1 else Arg).replace('_', ' ').strip()

                if Colon == -1: Inputs.append(input(Param + ':'))
                elif Type in ["int", "float"]: Inputs.append(Types[Type](float(input(Param + ': '))))
                else: Inputs.append(Types[Type](map(int, input(Param + ': ').strip().split())))

            Message("\n  OUTPUT : ", str(Func(*Inputs)))
           
        except : traceback.print_exe()#P.Message("WARNING : ", "Sorry! Something Went Wrong")

'''

if __name__ == '__main__' :
    Function_Menu(Func_Lib)


