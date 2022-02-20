'''AVL Tree
Newton's forward difference
Knapsack
'''

### 

'''
1, 2, 9's, etc Compliment Forms
Sign and Magnitude Form
'''




''' ANSI/IEEE S standard 754 - 1985
1. Single Precision Floating Point Binary Nos
2. Double   --------||--------
3. Extended --------||--------
'''




'''
Figure of Merit (SPP) = Propagation delay Time * Power Dissipation
'''


'''
SOP, POS Forms
Expression Reduction -- Algebraic Method / (Truth Table / K-Map)
'''





############   ############   ############   
############    BINARY ADDERS, SUBTRACTORS
############   ############   ############   







#region    ###############     BINARY ARITHMETIC    ###############
    
    
def Igr_Format(Numbers_List : list) -> str:
    """Returns All Numbers with Uniform Length"""
    
    if isinstance(Numbers_List, str): Numbers_List = Numbers_List.split()
  
    Numbers_List = list(map(str, Numbers_List))

    MaxLen = max(map(len, Numbers_List))
    return ['0'*(MaxLen-len(number)) + number for number in Numbers_List]

    

def Binary_Adder (Numbers_List: list, Base_System : int = 10) -> str:
    """PERFORMS ADDITION ON A LIST OF NUMBERS IN BASE SYSTEM Base_System"""
    
    Result, Carry = "", 0
    Numbers = Igr_Format(Numbers_List)
    MaxLen, Len = len(Numbers[0]), len(Numbers)  
    
    for col in range(MaxLen-1, -1, -1):
        colSum = Carry
        for row in range(Len): colSum += int(Numbers[row][col])
        Result, Carry = str(colSum%Base_System) + Result, colSum//Base_System
    
    while Carry != 0:
        Result = str(Carry%Base_System) + Result
        Carry = Carry//Base_System

    return Result





# Brute force
def Binary_Subtractor(Minuend : str, Subtrahend : str, Borrow : int = 0) -> str:
    Minuend, Subtrahend = Igr_Format([Minuend, Subtrahend])
    
    Result = ''
    for i in range(len(Minuend)-1, -1, -1):
        Curr_Minuend, Curr_Subtrahend = int(Minuend[i]), int(Subtrahend[i])

        if Borrow == 1:
            if Curr_Minuend == 1: Borrow = Curr_Minuend = 0
            else: Curr_Minuend = 1

        Result = str(Curr_Minuend ^ Curr_Subtrahend) + Result
        Borrow |= (0 if Curr_Minuend==1 else 1) * Curr_Subtrahend

    return str(int(Result))




# Using 2s Compliment for negative numbers
def Binary_Subtractor_2(Minuend : str, Subtrahend : str) -> str:
    Minuend, Subtrahend = Igr_Format([Minuend, Subtrahend])
    return str(int(Binary_Adder([Minuend, _2sCOMPLIMENT(Subtrahend)], 2)))





def Binary_Division(Dividend : str, Divisor : str) -> tuple:
    Quotient, Remainder, lDiv = '', '0', len(Divisor)

    while len(Dividend)>0:
        Remainder = '' if int(Remainder) == 0 else Remainder[Remainder.find('1'):]
        DivLen = lDiv - len(Remainder)
        if Remainder + Dividend[: DivLen] < Divisor: DivLen += 1

        Minuend = Remainder + Dividend[: DivLen]
        if int(Minuend) < int(Divisor): return Minuend, Quotient

        Dividend, Quotient = Dividend[DivLen :], Quotient + '1'
        Remainder = Binary_Subtractor(Minuend, Divisor)

        if int(Remainder) == 0 and (len(Dividend) == 0 or int(Dividend) == 0): return Remainder, Quotient + Dividend

    return Remainder, Quotient

#print(Binary_Adder(['110', '111', '110', '111']))

#endregion









#region               ##############     Number System <-> CODE CONVERTER    ##############
# `Inter NS Conversion` + `Inter Codes Conversion` + `NS <-> Code Conversion`


import imp
import math as m
import textwrap as tw



def Igr_ChrToVal(N): return N - (48 if N in range(48, 58) else 55 if N in range(65, 91) else 61)
def Igr_ValToChr(N): return chr(N + (48 if N in range(10) else 55 if N in range(10, 37) else 61))


def Print_List(Message = 'Choice'):
    try:
        for i in range(len(List)): print(str(i)+'. '+List[i])
        return int(input(Message+" : "))
    except: return -1



'''
Code Converters
First 5 by Universal Code Converter with Decimal Point -
Binary, Octal, Decimal, Duodecimal, Hexadecimal, Gray, BCD, Excess-3
'''


def Binary_To_Gray(Number : str, BTG : bool = True) -> str:
    if not isinstance(Number, str): Number = str(Number)
    if len(Number) < 2: return Number

    Result = Number[0]
    for i in range(1, len(Number)): Result += str(int(Number[i-1] if BTG is True else Result[-1]) ^ int(Number[i]))
    return Result
  

# X to Decimal NS
def X_To_Decimal(nfc : str, From : int, nDec : int = 0) -> int:
    for i in range(len(nfc)):
        nDec += From**(len(nfc)-1-i) * Igr_ChrToVal(ord(nfc[i]))
    return nDec

# Decimal to X NS   
def Decimal_To_X(nDec : int, to : int, conv : str = "") -> str:
    while(nDec != 0):
        conv = Igr_ValToChr(int(nDec%to)) + conv
        nDec//=to
    return conv


def BCD_To_Decimal(nfc : str, EachDigitLen : int = 4) -> str:
    nDec = ""
    for ele in tw.wrap(nfc, EachDigitLen): nDec += str(X_To_Decimal(ele, 2))
    return nDec

def Decimal_To_BCD(nfc : str, EachDigitLen : int = 4) -> str:
    bcd = ""
    for ele in str(nfc): bcd += str(Decimal_To_X(int(ele), 2)).zfill(EachDigitLen)
    return bcd


def BCD_To_Ex3(nfc : str, EachDigitLen : int = 4) -> str:
    Ex3 = ""
    for ele in tw.wrap(nfc, EachDigitLen): Ex3 += str(Binary_Adder(ele, "011")).zfill(EachDigitLen)
    return Ex3






#List = ["Base "+str(i) for i in range(2, 37)] + ["BCD", "EX-3", "Gray"]
List = [str(i) for i in [2, 8, 10, 16]] + ["BCD", "EX-3", "Gray"]

    

def NS_Code_Converter(nfc : str = None, From : str = None, To : str = None) -> str:
    if nfc == From == To == None:
        From, To = List[Print_List('From')], List[Print_List('To')]
        nfc = input('Number for Conversion = ')
    Result = 0
    
    #Base To Base
    if From in List[:-3] and To in List[:-3]:
        Result = Decimal_To_X(X_To_Decimal(nfc, int(From)), int(To))
    
    #Other Base To BCD
    elif From in List[:-3] and To == List[-3]:
        EDL = int(input('Each Digit Length : '))
        Result = Decimal_To_BCD(X_To_Decimal(nfc, int(From)), EDL)
   
    # BCD To Other Base
    elif From == List[-3] and To in List[:-3]:
        EDL = int(input('Each Digit Length : '))
        Result = Decimal_To_BCD(X_To_Decimal(nfc, int(From)), EDL)

    #Binary To Gray, Gray To Binary
    elif From == List[0] and To == List[-1] or From == List[-1] and To == List[0]:
        Result = Binary_To_Gray(nfc, True if From==List[0] else False)
    
    #BCD To Ex-3
    elif From == List[-3] and To == List[-2]:
        Result = BCD_To_Ex3(nfc.replace(' ', ''))
    
    return Result
        
#endregion
        






############   ############   ############   
############    SUPPORTER METHODS
############   ############   ############   





import codes.MATH.combinatorics.Permutations_and_Combinations as PC
import codes.DS.Strings.Add_Ons as ao






'''
 Truth Table
 If User gives values of variables then give function result
 Or give truth table for all possible combinations


// PROPOSITIONAL CALCULUS CALCULATOR //


'''



#######  ALL DUNDER / MAGIC METHODS
#### Operation = { '^': object.__and__, 'v': object.__or__, '~': object.__invert__, '<->': object.DOUBLE_IMPLIES, '->': object.IMPLIES }


#region    ###############     BINARY COMPLIMENTS    ###############


def _1sCOMPLIMENT(Number : str) -> str: return ''.join(["1" if Ele=="0" else "0" for Ele in list(str(Number))])


def _2sCOMPLIMENT(Number : str) -> str:
    #return str(bin(int(_1sCOMPLIMENT()))+1)[2:]
    parts = Number.rindex("1")
    return _1sCOMPLIMENT(Number[:parts]) + Number[parts:]


Func_Caller = { "1": _1sCOMPLIMENT, "2":_2sCOMPLIMENT }


def COMPLIMENTS() -> None:  
    print("\n\n   ♤♡ COMPLIMENT CALCULATOR ◇♧")

    Number = input("Enter Binary Number : ")

    print("1.  1's  COMPLIMENT","2.  2's  COMPLIMENT","9.  9's  COMPLIMENT","10. 10's COMPLIMENT", sep='\n')

    Func_Caller = { "1": _1sCOMPLIMENT, "2": _2sCOMPLIMENT }

    try: return [Func_Caller[i](Number) for i in input("CHOICE (Select Multiple by Space Separation, Eg. 1, 2): ").split(' ')]
    except: print("INVALID INPUT")

#endregion




import inspect

class Exp_Evaluator:
    
    '''
    def Calculator(self, Exp, Mode = "MATHEMATICAL"):
       
        DI, Imp, xOR = '=', '>', '@' #'<->', '->'  # DOUBLE IMPLIES, IMPLIES
        ODS, ORS = [], []
        
        if Mode.upper() == "BOOLEAN":
            Operation = { '^': Exp_Evaluator.AND, 'v': Exp_Evaluator.OR, '~': Exp_Evaluator.NEGATION, DI: Exp_Evaluator.DOUBLE_IMPLIES, Imp : Exp_Evaluator.IMPLIES }
            
            Binary_Operators  =  ['^', 'v', Imp, DI]
            Unary_Operators   =  ['~']
            All_Operators     =  ['^', 'v', Imp, DI, '~']
            
            Precedence = {'~': 4, '^': 3, 'v': 2, Imp: 1, DI: 1}


        if Mode.upper() == "MATHEMATICAL":
            Operation = { '+': lambda x,y: x+y, '-': lambda x,y: x-y, '*': lambda x,y: x*y, '//': lambda x,y: x//y, '/': lambda x,y: x/y, '%': lambda x,y: x%y, '^': lambda x,y: x**y, abs: lambda x: x.__abs__(), int: lambda x: x.__int__(), 'ln': m.log, 'log': lambda x: m.log(x, 10), '!': m.factorial, 'sin': m.sin, 'cos': m.cos, 'tan': m.tan}

            Binary_Operators   =  ['^', '÷', '/', '%', '*', '×', '+', '-']
            Unary_Operators    =  ['√', '!', '~', 'log', 'ln', 'sin', 'cos', 'tan', 'cot', 'cosec', 'sec', 'asin', 'acos', 'atan']
            Boolean_Operators  =  ['<', '>', '|', '&']
            All_Operators      =  ['^', '÷', '/', '%', '*', '×', '+', '-', '√', '!', '~', '<', '>', '|', '&']

            Trig_Precedence = 8
            Precedence = {'&': 1, '|': 1, '>': 2, '<': 2, '~': 6, '!': 6, '√': 5, '-': 3, '+': 3, '×': 4, '*': 4, '%': 4, '/': 4, '÷': 4, '^': 5, 'log': 6, '!': 7, 'sin': 8, 'cos': 8, 'tan': 8, 'cot': 8, 'cosec': 8, 'sec': 8, 'asin': 8, 'acos': 8, 'atan': 8 }
        '''
        
    def Calculator(self, Exp, Mode = "MATHEMATICAL"):
       
        DI, Imp, xOR = '=', '>', '@' #'<->', '->'  # DOUBLE IMPLIES, IMPLIES
        ODS, ORS = [], []
        
        if Mode.upper() == "BOOLEAN":
            Operation = { '^': Exp_Evaluator.AND, 'v': Exp_Evaluator.OR, '~': Exp_Evaluator.NEGATION, DI: Exp_Evaluator.DOUBLE_IMPLIES, Imp : Exp_Evaluator.IMPLIES }

            Binary_Operators  =  ['^', 'v', Imp, DI]
            Unary_Operators   =  ['~']
            All_Operators     =  ['^', 'v', Imp, DI, '~']
            
            Precedence = {'~': 4, '^': 3, 'v': 2, Imp: 1, DI: 1}


        if Mode.upper() == "MATHEMATICAL":
            Operation = { '+': lambda x,y: x+y, '-': lambda x,y: x-y, '*': lambda x,y: x*y, '//': lambda x,y: x//y, '/': lambda x,y: x/y, '%': lambda x,y: x%y, '^': lambda x,y: x**y, abs: lambda x: x.__abs__(), int: lambda x: x.__int__(), 'ln': m.log, 'log': lambda x: m.log(x, 10), '!': m.factorial, 'sin': m.sin, 'cos': m.cos, 'tan': m.tan}

            Binary_Operators   =  ['^', '/', '%', '*', '+', '-']
            Unary_Operators    =  ['!', '~', 'log', 'ln', 'sin', 'cos', 'tan', 'cot', 'cosec', 'sec', 'asin', 'acos', 'atan']
            Boolean_Operators  =  ['<', '>', '|', '&']
            All_Operators      =  ['^', '/', '%', '*', '+', '-', '!', '~', '<', '>', '|', '&']

            Trig_Precedence = 8
            Precedence = {'&': 1, '|': 1, '>': 2, '<': 2, '-': 3, '+': 3, '*': 4, '%': 4, '/': 4, '^': 5, 'log': 6, '~': 6, '!': 7, 
                          'sin': 8, 'cos': 8, 'tan': 8, 'cot': 8, 'cosec': 8, 'sec': 8, 'asin': 8, 'acos': 8, 'atan': 8 }
            
            OpDict = {1: ['&', '|'], 2: ['>', '<'], 6: ['~', 'log'], 3: ['-', '+'], 4: ['*', '%', '/'], 5: ['^'], 7: ['!'], 8: ['sin', 'cos', 'tan', 'cot', 'cosec', 'sec', 'asin', 'acos', 'atan']}




        def Evaluate():
            if any([len(ORS), len(ODS)]) is False: return
            ODS.append(Operation.get(ORS[-1])(*[ODS.pop(-1) for i in range(len(str(inspect.signature(Operation[ORS.pop(-1)])).split(',')))][::-1]))



        Exp = Exp.translate(Exp.maketrans('×÷', '*/'))
        Exp = ao.Split(Exp, list(Precedence.keys())+['(', ')'], True, True)
        

        for ele in Exp:
            if ele in list(Precedence.keys()) + ['(', ')']:
                if ele == '(' or len(ORS) == 0: ORS.append(ele)

                elif ele == ')':
                    while ORS[-1] != '(': Evaluate()
                    ORS.pop(-1)                

                else:
                    while len(ORS)>0 and ORS[-1] != '(' and Precedence[ele] <= Precedence[ORS[-1]]: Evaluate()
                    ORS.append(ele)

            else: ODS.append(float(ele))

        while len(ORS)>0: Evaluate()
        return ODS.pop()



        
    def NEGATION(A):           return 1 if int(A) is 0 else 0
    
    def AND(A, B):             return 1 if int(A) * int(B) == 1 else 0
    
    def OR(A, B):              return 1 if A+B>1 else A+B
    
    def IMPLIES(A, B):         return 0 if(int(A) is 1 and int(B) is 0) else 1
    
    def DOUBLE_IMPLIES(A, B):  return 1 if int(A) == int(B) else 0









'''
Expression Solver and Comparator
Draw Truth Tables and compare Expressions and tell if they're same or not
'''
def Propositional_Truth_Table(Exp : str = "((pvqvy)^~q)>r=t=s") -> None:
    #print(All_Operators)

    Variables = sorted(list(set([i for i in Exp if i.isalpha() and i!='v'])))
    Outcomes = sorted(list(PC.Permutations([0, 1], len(Variables), True)))

    for i in Variables: print(i, end=' '*5)
    print(Exp, end='\n\n')
    

    for i in range(len(Outcomes)):
        Expr = Exp
        for j in range(len(Outcomes[i])):
            print(Outcomes[i][j], end=' '*5)
            Expr = Expr.replace(Variables[j], str(Outcomes[i][j]))
        
        print(int(Exp_Evaluator().Calculator(Expr, "BOOLEAN")))#, end=' '*5)




if __name__ == '__main__':
    print(Igr_Format([10, '1060', 1000]))



#### Facility of Retaining Default Argument- like enter . to retain default argument for current parameter

