'''
1. MENU OF FUNCTIONS PRINTER
2. DECORATOR
3. TABULAR REPRESENTATION
'''



#     ###########      ###########      ###########
      ###########  MENU OF FUNCTIONS PRINTER
      ###########      ###########      ###########

def Function_Menu(Func_Library: list):
    import sys, traceback #,numpy as np
    from inspect import signature
    
    def Message(Header, Str): print(Header + Str)

    Func_Lib = { str(i+1): Func_Library[i] for i in range(len(Func_Library)) }
    
    while True:
        try:
            print("\n\n %20s" %"MENU \n")
            print(f"    0. Exit")
        
            for FuncNumber, Func in Func_Lib.items():
                print(f"\n    %-2s. %-70s :   %-40s"%(FuncNumber, str(Func.__name__).replace('_',' ') + str(signature(Func)).replace('_', ' '), Func.__doc__))

            Types = { "int": int, "float": float, "str": str, "dict": dict, "list": list, "tuple": tuple, "set": set, "range": range }
            
            Choice = input("\n\n  CHOICE : ").strip()
            
            if Choice == '0': sys.exit(0)
            
            Func = Func_Lib[Choice]
            SigList = str(signature(Func))[1:-1].split(',')
           
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












#     ###########      ###########      ###########
      ###########  DECORATOR AND DATA TYPE CONVERTER
      ###########      ###########      ###########

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













#     ###########      ###########      ###########
      ###########  TABULAR REPRESENTATION
      ###########      ###########      ###########





from re import I
import numpy as np


def Table(Headers_1D:list, Rows_2D:list, Uniform_Col_Width:int = -1, Vert_Char:str = '|', Horiz_Char:str = '-'):
    All_Rows        =   [ Headers_1D ] + Rows_2D
    Column_Widths   =   [ max(map(lambda x: len(x)+2, Row)) for Row in np.array(All_Rows).T ] if Uniform_Col_Width == -1 else [ Uniform_Col_Width ] * len(All_Rows[0])
    Table_X         =   sum(Column_Widths) + len(Vert_Char)*(len(All_Rows[0]) + 1)

    print(' ' * len(Vert_Char) + Horiz_Char * Table_X)
    for Row in All_Rows: print(Vert_Char, Vert_Char.join([str(Row[i]).center(Column_Widths[i]) for i in range(len(Row))]), Vert_Char, '\n' + ' ' * len(Vert_Char) + Horiz_Char * Table_X)











#     ###########      ###########      ###########
      ###########  TABULAR REPRESENTATION
      ###########      ###########      ###########







# from codes.DS.Strings.Add_Ons import Split
# from codes.TOOLS.Calculator import Calculator
# from codes.DBMS.Tables import Table
import numpy as np



if __name__ == '__main__':
    Table(["Name", "Age", "Sex"], [["Himanshu Pandey", 20, "M"], ["Hande Erçel", 27, "F"], ["Nina Dobrev", 26, "F"]], 17)


    columns = { 'x': list(np.linspace(2, 5, 7)), 'f':[3,34,50,80,65,30,8]}

    List = np.array(list(columns.values()))


    T = Table(list(columns.keys()))
    T.Add_Rows(List.T)
    T.Exp_Evaluate({ 'u':'(x-3.5)/0.5', 'fu':'f*u', 'fu^2':'f*u^2', 'fu^3':'f*u^3', 'fu^4':'f*u^4' })

    #T.sort()
    T.Peek()

    '''
    List = np.array(
    [['Himanshu Pandey', 'Aanshu Pandey', 'Burak Deniz', 'Ozge Yagiz', 'Hande Erçel', 'Nina Dobrev', 'Bear Grylls', 'Albert Einstein', 'Lionel Messi']
    ,['20', '12', '27', '27', '26', '23', '45', '100', '37']
    ,['M', 'M', 'M', 'F', 'F', 'F', 'M', 'M', 'M']
    ,['£', '*', '@', '_', '&', '-', '+', '(', ')']
    ,['😂', '🤤', '🎉', '🍾', '❤', '🙏', '🍻', '🔥', '💤']
    ])


    T = Table(["Name", "Age", "Gender", "Sign", "Emoji"])
    T.Add_Rows(List.T)
    T.sort()
    T.Peek()
    T.Add_Rows(['Stefanie Knight', 26, 'F', '$', '🤙'])
    T.Peek()
    T.sort('Name')
    T.Peek()
    #print(T.Get_Col_Order())'''







