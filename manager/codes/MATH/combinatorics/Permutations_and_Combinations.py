class Perms_Combs:
    Final_List = []

    def Combinations(self, Sub_List, n):
        L = len(Sub_List)
        
        if L<=1:
            Perms_Combs.Final_List.append(Sub_List)
            return Sub_List
        
        else:
            #List = Perms_Combs.Combinations(Perms_Combs.Final_List, Sub_List[1:], n)
            #for ele in List: ele.insert(0, Sub_List[0])
    
            #Perms_Combs.Final_List.append(List)
            '''return List if n!=len(List) else '''
            Perms_Combs.Final_List
        


    def Print_List(self): print(Perms_Combs.Final_List)



def Permutations(Elements : list, Positions=-1, Allow_Repetitions = False):
    """PERMUTATIONS :- Returns List of All Possible Permutations of Input Data"""
    if Positions == 0: return [[]*len(Elements)]
    if Positions == -1: Positions = len(Elements)

    return set((i,)+j for i in Elements for j in set(map(tuple, Permutations(Elements, Positions-1, Allow_Repetitions))) if (True if Allow_Repetitions is True else i not in j))



def Combinations(Elements : list, Positions=-1):
    """COMBINATIONS :- Returns List of All Possible Combinations of Input Data"""
    return list(map(list, set(map(frozenset, Permutations(Elements, Positions)))))


if __name__ == '__main__':
    PC = Perms_Combs()
    print(PC.Combinations([1,2,3], 3))
    PC.Print_List()
    print(Permutations([1,2], 3))
    print(Combinations([1,2,3], 3))
