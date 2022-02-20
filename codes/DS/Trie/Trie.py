
def Reach(Dict, Key_List):
    try:
        for Key in Key_List: Dict = Dict[Key]
        return Dict
    except Exception: return 'Not Found!'

def Split(String: str, Splitters, KeepSplitters = False, StripElements = False):
        String += Splitters[0]
        SplitPos = [-1] + [pos for pos, ele in enumerate(String) if ele in Splitters] + [len(String)-1]
        List = []
        for i in range(len(SplitPos)-1):
            if SplitPos[i]+1 != SplitPos[i+1]:
                Ele = String[SplitPos[i]+1 : SplitPos[i+1]]
                List.append(Ele.strip() if StripElements is True else Ele)
            if KeepSplitters is True and i<len(SplitPos)-2: List.append(String[SplitPos[i+1]])
        return List[:-1 if KeepSplitters is not True else -2]




from time import sleep

def s(t=1): sleep(t)




class Node:
    pass


class Spacial_Node(Node):
    pass






class Dense_Node(Node):
  
    def __init__(self, Data = None):
        self.Data = Data 
        self.Links = []
    
    

    #Commented   
        # def Search(Node, Query, Pos=0, IFNP = False):
        #     """IFNP : Insert_If_Not_Present :- User can set this field to True if Insertion should be performed when Data not present in Trie"""
        #     print(Node.Data)
        #     i, lQ, lN = Pos, len(Query), len(Node.Data)
        #     while(i < min(lQ, lN) and Node.Data[i]==Query[i]): i+=1                               # Get the Position till which Node.Data and Query are Identical

        #     if i==lN==lQ: return "1", f"Full Match"                                               # If Query is Equal to Node.Data (Perfect Match)
            
        #     if i==lN:                                                                             # If Node.Data is a Substring of Query then Check children or insert new link
        #         if Node.Links != []:                                                              # If Node has Children
        #             for link in range(len(Node.Links)):                                           # Iterate through Children
        #                 if Node.Links[link].Data[Pos] == Query[Pos]:                              # If Node's Current Child's Data is synchronizing with Query Data upto 'Pos' Places
        #                     Result = Dense_Node.Search(Node.Links[link], Query, Pos+1, IFNP)      # Then Level Up and Conquer this Child's Children
        
        #                     if IFNP and Result[0] in tuple("34"):                                 # If Insertion Allowed (IFNP=True) and Demanded(Result type 3 or 4)
        #                         if Result[0] == "3":                                              # If Query is in between Node and Node.Links[link].Data
        #                             New_Node = Dense_Node(Query)                                  # Create New Node with Query as its Data
        #                             New_Node.Links.extend([Node.Links[link]])                     # Make Current child of Node as child of New Node
                                
        #                         if Result[0] == "4":                                              # If Query is inline with Node.Links[link].Data
        #                             New_Node = Dense_Node(Query[: int(Result[1])])                # Create a common Node for both of them
        #                             New_Node.Links.extend([Node.Links[link], Dense_Node(Query)])  # Insert these inline Nodes as children of the common Node

        #                         Node.Links[link] = New_Node                                       # Replace Older Node with New Node in Node's Links Link
        #                         return "1", f"Full Match {Query}"

        #                     else: return Result                                                   # Else Do not Insert and return Message recieved

        #         if IFNP:                                                                          # If IFNP==True, Insert Data
        #             Node.Links.append(Dense_Node(Query))                                      
        #             return "1", f"Full Match {Query}"                                             # Hence Query will Match with Newly Inserted Data
        #         else: return f"Not Found!"                                                        # If IFNP==False, Do not Insert and Message : Not Found


        #     elif i==lQ: return "3", f"Insert {Query} before {Node.Data}"                          # If Query is a Substring of Node.Data

        #     else: return "4", i, f"{i} characters matched between {Query[:i]} and {Node.Data}"    # 4 Depicts type of Message, i is no of chars matched, String is the actual message
            

    
    def Traverse(Node, indent=0):
        print(' '*indent + Node.Data)
        s(0.3)
        for link in Node.Links:
            Dense_Node.Traverse(link, indent+4)
    


    def Searcher(Node, Query, Hierarchy=""):
        """Searches Query-Data in the Trie"""

        if Node.Data == Query: return 1, Hierarchy

        for link in Node.Links:
            if link.Data == Query: return 1, Hierarchy + link.Data + " -> "
            Result = Dense_Node.Searcher(link, Query, Hierarchy + link.Data + " -> ")
            if Result[0] == 1: return Result
        
        return -1, "Not Found"



    def Insert(Node, Query, Pos=0):
        """Inserts Data in Trie, and Handles 4 Different Scenarios 1. Inserted Successfully - Returns Unique Message for Each Type"""

        i, lQ, lN = Pos, len(Query), len(Node.Data)
        while(i < min(lQ, lN) and Node.Data[i]==Query[i]): i+=1                               # Get the Position till which Node.Data and Query are Identical

        if i==lN==lQ: return "2", f"{Query} Already Exists"                                   # If Query is Equal to Node.Data (Perfect Match)
        
        if i==lN:                                                                             # If Node.Data is a Substring of Query then Check children or insert new link
            if Node.Links != []:                                                              # If Node has Children
                for link in range(len(Node.Links)):                                           # Iterate through Children
                    if Node.Links[link].Data[Pos] == Query[Pos]:                              # If Node's Current Child's Data is synchronizing with Query Data upto 'Pos' Places
                        R = Dense_Node.Insert(Node.Links[link], Query, Pos+1)                 # Then Level Up and Conquer this Child's Children

                        if R[0] in ("3", "4"):
                            New_Node = Dense_Node(Query[: int(R[1])] if R[0]=="4" else Query) # Create a common Node for both of them
                            
                            if R[0] == "3":                                                   # If Query is in between Node and Node.Links[link].Data
                                New_Node.Links.extend([Node.Links[link]])                     # Make Current child of Node as child of New Node  
                            if R[0] == "4":                                                   # If Query is inline with Node.Links[link].Data
                                New_Node.Links.extend([Node.Links[link], Dense_Node(Query)])  # Insert these inline Nodes as children of the common Node
                            
                            Node.Links[link] = New_Node                                       # Replace Older Node with New Node in Node's Links Link
                            return "1", f"{Query} Insertion Successful"   
                              
                        else: return R                                                        # Else Do not Insert and return Message recieved   
      
            Node.Links.append(Dense_Node(Query))                                          
            return "1", f"{Query} Insertion Successful"                                       # Hence Query will Match with Newly Inserted Data
      
      
        elif i==lQ: return "3", f"Insert {Query} before {Node.Data}"                          # If Query is a Substring of Node.Data
      
        else: return "4", i, f"{i} characters matched between {Query[:i]} and {Node.Data}"    # 4 Depicts type of Message, i is no of chars matched, String is the actual message







if __name__ == '__main__':
    # Create a Trie and Initialize Root
    Root = Dense_Node("")

    # Insert Data
    Data = ["a", "an", "at", "ande", "tea", "team", "cease", "heal", "been", "car", "ca", "bean", "healing", "he", "ban",
    "floccinaucinihilipilification", "fry", "flock", "freak", "freaky", "been"]
    for data in Data:  print(Dense_Node.Insert(Root, data))

    # Search Data
    Find = "flock"
    print(f"Searching {Find} : ", Dense_Node.Searcher(Root, Find))

    # Traverse And Print Trie Structure
    Dense_Node.Traverse(Root)






