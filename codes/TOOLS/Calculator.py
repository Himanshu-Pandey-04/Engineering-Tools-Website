import math as m
from codes.DS.Strings.Add_Ons import Split

#import Python.Data_Manip.Data_Manip

Binary_Operators = ['^', '÷', '/', '%', '*', '×', '+', '-']
Unary_Operators  = ['√', '!', '~', 'log', 'ln', 'sin', 'cos', 'tan', 'cot', 'cosec', 'sec', 'asin', 'acos', 'atan']
Boolean_Operators = ['<', '>', '|', '&']
All_Operators = ['^', '÷', '/', '%', '*', '×', '+', '-', '√', '!', '~', '<', '>', '|', '&']

ODS, ORS = [], []
Trig_Precedence = 8
Precedence = {'&': 1, '|': 1, '>': 2, '<': 2, '~': 6, '!': 6, '√': 5, '-': 3, '+': 3, '×': 4, '*': 4, '%': 4, '/': 4, '÷': 4, '^': 5, 'log': 6, '!': 7, 'sin': 8, 'cos': 8, 'tan': 8, 'cot': 8, 'cosec': 8, 'sec': 8, 'asin': 8, 'acos': 8, 'atan': 8 }





def Calculator(Exp, OperPrec = Precedence):
    Exp = Exp.translate(Exp.maketrans('×÷', '*/'))
    Exp = Split(Exp, list(OperPrec.keys())+['(', ')'], True, True)


    def Evaluate():
        if any([len(ORS), len(ODS)]) is False: return
        
        Second, First = ODS.pop(-1), ODS[-1]
        Operation = { '+': First.__add__, '-': First.__sub__, '*': First.__mul__, '//': First.__floordiv__, '/': First.__truediv__, '%': First.__mod__, '^': First.__pow__, abs: First.__abs__, int: First.__int__, 'ln': m.log, 'log': lambda x: m.log(x, 10), '!': m.factorial, 'sin': m.sin, 'cos': m.cos, 'tan': m.tan }
    
    
        if ORS[-1] in Binary_Operators:
            ODS.pop(-1)
            
        elif ORS[-1] in Unary_Operators: pass
        
        ODS.append(Operation.get(ORS.pop(-1))(Second))    


    # Will combine '-' sign and succeeding number to make single -ve number
    for i in range(len(Exp)-1):
        try:
            if Exp[i] in OperPrec.keys() and Exp[i+1] == '-':       # If '-' has some operator before it (then combine it with succeeding number)
                Exp[i+2] = '-'+Exp[i+2]
                del Exp[i+1]
            elif Exp[i] in OperPrec.keys() and Exp[i+1] == '(' and Exp[i+2] == '-': # If condition like '<some operator>(-', then remove parentheses and combine)
                Exp[i+3] = '-'+Exp[i+3]
                # del Exp[i+1:i+3]
                del Exp[i+2]
        except: continue

    
    for ele in Exp:
        if ele in list(OperPrec.keys()) + ['(', ')']:

            if ele == '(' or len(ORS) == 0: ORS.append(ele)

            elif ele == ')':
                while ORS[-1] != '(': Evaluate()
                ORS.pop(-1)                

            else:
                while len(ORS)>0 and ORS[-1] != '(' and OperPrec[ele] <= OperPrec[ORS[-1]]: Evaluate()
                ORS.append(ele)

        else: ODS.append(float(ele))

    while len(ORS)>0: Evaluate()
    return ODS.pop()





if __name__ == '__main__':
    Expression = input('Expression=') #"1+3-5*2^(9-6)%2+sin(3.14159)*5!/120"
    print(Expression, ' = ', Calculator(Expression))








#######  ALL DUNDER / MAGIC METHODS
#### Operation = { '+': object.__add__, '*': object.__mul__, '//': object.__floordiv__, '/': object.__truediv__, '%': object.__mod__, '**': object.__pow__, '<<': object.__lshift__, '>>': object.__rshift__, '&': object.__and__, '^': object.__xor__, '|': object.__or__, '+=': object.__iadd__, '-=': object.__isub__, '*=': object.__imul__, '/=': object.__idiv__, '//=': object.__ifloordiv__, '%=': object.__imod__, '**=': object.__ipow__, '<<=': object.__ilshift__, '>>=': object.__irshift__, '&=': object.__iand__, '^=': object.__ixor__, '|=': object.__ior__, 'abs()': object.__abs__, '~': object.__invert__, 'complex()': object.__complex__, 'int()': object.__int__, 'long()': object.__long__, 'float()': object.__float__, 'oct()': object.__oct__, 'hex()': object.__hex__, '<': object.__lt__, '<=': object.__le__, '==': object.__eq__, '!=': object.__ne__, '>=': object.__ge__, '>': object.__gt__ } # '+': object.__pos__, '-': object.__neg__,


