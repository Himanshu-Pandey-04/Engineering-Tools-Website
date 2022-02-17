def TimeIt(stmts, setups, numbers):
    from timeit import timeit as t
    
    Ls, LS, Ln = len(stmts), len(setups), len(numbers)
    return [t(stmt=stmts[i%Ls], setup=setups[i%LS], number= numbers[i%Ln]) for i in range(Ls)]



import manager.codes.LDCO.ldco as ldco
from textwrap import wrap
import math as m



#region    ###############     CRC    ###############


def CRC_Encoder(Data : str, Divisor : str) -> str:
    return Data + ldco.Binary_Division(Data + '0'*(len(Divisor)-1), Divisor)[0].zfill(len(Divisor)-1)



def CRC_Decoder(Data : str, Divisor : str) -> str:
    return "Accepted" if int(ldco.Binary_Division(Data, Divisor)[0]) == 0 else "Discarded"
 
#endregion






#region    ###############     CHECK SUM    ###############


def _1sComp_CheckSum_Generator(Data_List : list[str]) -> list[str]:
    Sum = ldco.NS_Code_Converter(str(sum(map(int, Data_List))), "10", "2")
    Size = int(m.log(max(Data_List), 2))
    while len(Sum)>Size: Sum = ldco.Binary_Adder(wrap(Sum.zfill(len(Sum)% Size), Size), 2)
    Sum = ldco._1sCOMPLIMENT(Sum.zfill(Size))
    
    return Data_List + [ldco.NS_Code_Converter(Sum, "2", "10")]





def _1sComp_CheckSum_Checker(Data_List : list[str]) -> list[str]:
    Sum = ldco.NS_Code_Converter(sum(map(int, Data_List)), 10, 2)
    
    Size = int(m.log(max(Data_List), 2))
    while len(str(Sum))>Size: Sum = ldco.Binary_Adder(wrap(Sum, Size), 2)
    
    Sum = ldco._1sCOMPLIMENT(str(Sum).zfill(Size))
    
    return "Accepted" if int(Sum) == 0 else "Discarded"

#endregion






#region    ###############     HAMMING CODE, ERROR DETECTION AND CORRECTION    ###############
import typing

def hamming_distance(word_1 : list[str], word_2 : list[str] = None) -> int:
    if not word_1: return
    if word_2 is None: word_2 = [0]*len(word_1)
    try:
        if not isinstance(word_1, typing.Iterable): word_1 = list(word_1)
        if not isinstance(word_2, typing.Iterable): word_2 = list(word_2)
    except: return "WARNING : inputs must be a list/tuple/set/str"

    if (l1 := len(word_1)) != (l2 := len(word_2)):
        if l1>l2: word_2 = [0]*(l1-l2) + word_2
        else: word_1 = [0]*(l2-l1) + word_1

    return sum([e1!=e2 for e1,e2 in zip(word_1, word_2)])



def MHD_ED_EC(word_1 : list[str], word_2 : list[str] = None) -> dict[str, int]:
    """Minimum hamming distance(MHD), Error detection(ED), Error correction(EC)
        ==========================================================
        Calculates
        ----------
        1. Minimum Hamming Distance (d_min) between given 2 code-words
        2. Number of errors that can be detected
        3. Number of errors that can be corrected
    """
    d_min = hamming_distance(word_1, word_2)
    return {
        'Minimum hamming distance' : d_min,
        'Number of errors that can be detected'  : max(0, d_min-1),
        'Number of errors that can be corrected' : max(0, (d_min-1)//2)
    }


#endgregion





if __name__ == '__main__':
    #print(dict(zip(['Remainder', 'Quotient'], Binary_Division('11010', '101'))))
    #print(CRC_Decoder('010101', '10101'))
    print(_1sComp_CheckSum_Generator([7, 11, 12, 0, 6]))
    print(_1sComp_CheckSum_Checker([7, 11, 12, 0, 6, 9]))