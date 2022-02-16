import random as r



class Randomizer :
  
  def Random_Element(Sequence, start=0, end=-1) :                                                             # For Picking Random element from a sequence
      #try:
      if end==-1: end = len(Sequence)
      end = min(end, len(Sequence)-1)
      if start>end or end<0 or start>=len(Sequence): return -1                                                # If Inputs don't follow logic
 
      if isinstance(Sequence, dict): return Sequence[list(Sequence.keys())[r.randint(start, end)]]        # If instance of dict, pick random key from list of dict.keys(), then return value mapped to that key
     
      if isinstance(Sequence, (list, tuple, set)): return Sequence[r.randint(start, end)]                 # If instance of a general sequence, return random indexed value
    
      #except: return -2
  
  
  
  
  def Random_Range(start, end):
    try:
      if (type(start) != type(end)) or end<start : return -1                                              # If start and end are of different data types or end<start
    
      if isinstance(start, float): return r.uniform(start, end)                                           # Random Decimal No. between start and end
        
      if isinstance(start, int): return r.randint(start, end)                                             # Random Integer between start and end
   
    except: return -2




  def BiasedEvents(Sequence, NoOfDraws):                                                                  # Method Takes Input of Biased Probability of unique elements and number of outcomes/draws
    if any([isinstance(i, float) for i in Sequence]):                                                     # If any element is floating point number
  
      decimal = [str(float(i)).split(".")[1] for i in Sequence]                                           # Obtains and stores decimal parts of all elements in list 'decimal'
  
      if any(list(map(int,decimal))) != False:                                                            # If any element has a decimal part
        FinalDeciPlaces = min(max([len(str(i)) for i in decimal]),4)                                      # Compute maximum length of decimal part, and take minimum of that with 4
        return FinalDeciPlaces
  
  
  
  
  
  def Shuffler(Sequence) :                                                             # For Picking Random element from a sequence
    try:
      OldList, NewList = [i for i in Sequence], []
      for Len in range(len(OldList)-1, -1, -1):
        NewList.append(OldList.pop(r.randint(0, Len)))
      
      return type(Sequence)(NewList)
      
    except: return -2




  # Shuffle Individual Sequences and Group(zip)
  def Shuffle_Zip(length = -1, Sequence1 = ["Coco", "Nova"], Sequence2 = ["Nina", "Hande", "Candice"], *args):
    import math as m
    All = [Sequence1, Sequence2] + list(args)
    length = max(map(len, All)) if length==-1 else length

    final = []
    for ele in All:
        Args = ele*(length//len(ele)) + ele[:length%len(ele)]
        final.append(Randomizer.Shuffler(Args))
    return list(zip(*final))



  # Generate random Dates
  def Random_Dates(Freq = 10, dayR = (1, 31), monthR = (1, 12), yearR = (2000, 2021), Format = "YYYY-MM-DD"):
    try: from random import randint as r
    except: raise Exception("Random_Dates need Random module to operate - action: pip install random")
    
    try:
      
        Format, Result = Format.lower(), []
        for i in range(Freq):
            Max_Days_Mod = [32, 29, 32, 31, 32, 31, 32, 32, 31, 32, 31, 32]

            y, m, d = list(map(lambda xy: str(r(*xy[0])).zfill(xy[1]), [(yearR, 4), (monthR, 2), (dayR, 2)]))

            delimiter = '-' if Format.find('/')==-1 else '/'
            Dict = {Format.find('y'):y, Format.find('m'):m, Format.find('d'):d}

            Result.append(delimiter.join([Dict[i] for i in sorted(Dict)]))
        return Result
    
    except: raise Exception

            
if __name__ == '__main__':
    R = Randomizer
    
    print(R.Shuffler([[66], 789, (7), ["2", 4.077], ("3", 999.999)]))
    
    print(R.Random_Element(list(range(6))))
    print(R.Random_Range(3, 6))






