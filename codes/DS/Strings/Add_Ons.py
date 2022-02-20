class String:
    # CONSTRUCTOR
    def __init__(self, Padding=40, CharHori="-", CharVert="|"):
        Padding = Padding
        CharHori, CharVert = CharHori, CharVert


    # MESSAGE DISPLAY
    def Message(self, MessageType, *Messages):
        HLine = " " + self.CharHori * (max(self.Padding, max([len(str(Str)) for Str in Messages])) + len(MessageType) + 5)
        
        print(HLine)
        for i in range(len(Messages)):
            print(self.CharVert, f" {MessageType}  %-{self.Padding}s"%Messages[i], self.CharVert)
            print(HLine)





import string

class strConsts:
    digits       = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
    alphabetCaps = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',)
    alphabetSmls = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)
    punctuations = ('!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '\\', '|', '/', ':', ';', '<', '>', ',', '.', '?', '/', "'", '"', '`', '~', '(', ')', '[', ']', '{', '}',)
    whitespaces  = tuple(string.whitespace) # Eq to (' ', '\t', '\n', '\r', '\x0b', '\x0c')

# PRETTY PRINTING

# RIGHT, LEFT, CENTRE JUSTIFY









def Split(text:str, splitters:list[str], keepSplitters:bool = False, stripElements:bool = False) -> list[str]:
    '''Split
       =====

       splits given text/string by given splitters of any length

       Parameters
       ----------

       1. text : str :: The string on which splitting action has to be performed
       2. splitters : list[str] :: List of splitters (splitters can be of length > 1)
       3. keepSplitters : bool :: If True, splitters are also included in the resulting list of elements
       4. stripElements : bool :: If True, elements included in the result list are first stripped

       Returns
       -------
       List of resulting strings after split action
    '''

    try:
        text += splitters[0]                                            # Append a splitter at the end
        maxLen, spltrs = 0, {}                                          # maxLen among Splitters, spltrs dictionary

        for spltr in splitters:
            ls = len(spltr)
            if ls > maxLen: maxLen = ls
            spltrs[spltr] = ls                                          # Mapping splitter to its length

        elements, eleStart, i = [], 0, 0
        while i < len(text):
            for s in range(maxLen):
                if spltrs.get(text[i:i+s+1], 0):               # If current sliced string is a splitter
                    if text[eleStart:i]: elements.append(text[eleStart:i])  # If elem has len>0 append
                    if keepSplitters: elements.append(spltr)            # If splitters demanded, include them too
                    i = eleStart = i+s+1
                    break
            else: i+=1
        
        return elements

    except: return 'Error!'





def Split_Older(String: str, Splitters, KeepSplitters = False, StripElements = False):
    '''Can split text given by splitters of lenght 1'''
    #try:
    String = String + Splitters[0]
    SplitPos = [-1] + [pos for pos, ele in enumerate(String) if ele in Splitters] + [len(String)-1]

    List = []
    for i in range(len(SplitPos)-1):
        if SplitPos[i]+1 != SplitPos[i+1]:
            Ele = String[SplitPos[i]+1 : SplitPos[i+1]]
            List.append(Ele.strip() if StripElements is True else Ele)

        if KeepSplitters is True and i<len(SplitPos)-2: List.append(String[SplitPos[i+1]])

    return List[:-1 if KeepSplitters is not True else -2]
    
    #except: return -1





def makePairs(code: str, bracket_list = ['[', '{', '(', '<']) -> dict:
    """
    Pair Maker
    =========
        Finds and creates corresponding pairs of all types of brackets given in the 'bracket_list' present in the 'code'.

        Parameters
        ----------
        1. Code : str - given string of code
        2. Bracket List : list - all types of brackets whose pair has to be searched and mapped

        Returns
        -------
        A dictionary that maps an opening bracket position to corresponding closing bracket position

        Example
        -------
        >>> bracePairs = makePairs(code)\n
        >>> for open, close in bracePairs.items():\n
        >>>    print(code[open : close+1])
    """
    
    naivePairs = { '{':'}', '[':']', '(':')', '<':'>' }
    pairs:dict = {}                                                         # maps '{' position to corresponding '}' position
    openBraceStack = []                                                     # will store the consecutive brace openings
    for pos, char in enumerate(code):
        if char in naivePairs.keys(): openBraceStack.append(pos)            # if char is '{', push it into the 'openBraceStack'
        elif char in naivePairs.values(): pairs[openBraceStack.pop()] = pos # if char is '}', pop the last '{' from 'openBraceStack' and store this pair into 'pairs'
    
    return pairs