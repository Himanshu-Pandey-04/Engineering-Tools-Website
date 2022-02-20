import re

def Clean(sentence: str):
    Punctuations_Dict = list(''''"!?#@()[]{}+-=_$*/\&|~%^,.:;''')
    import re
    sentence = sentence.lower()

    for char in ['’', '-', "'"]: sentence = sentence.replace(char, '')                                        # REMOVES
    for char, rep in {'é':'e', 'à':'a', '(s)':'s', '(t)':'t'}.items(): sentence = sentence.replace(char, rep)                      # REPLACEMENTS
    sentence = re.sub(r"\([^()]*\)", '', sentence)                                                            # REDUCTIONS

    sentence = sentence.replace(" ' ", "'")
    Shorts = { "won't": "would not", "can't": "cannot", "shouldn't": "should not", "gonna": "going to", "wanna" : "want to"} #    "n't", ' not'
    for Short, Full in Shorts.items(): sentence = sentence.replace(Short, Full)
        
    for punc in Punctuations_Dict: sentence = sentence.replace(punc, f' {punc} ') #    list('''?!;:'"*/()+-&_#@{}\=°^%[]|~×÷^,.''')
    sentence = sentence.replace(" ' ", "'")

    return sentence



def Clean_Resume(resumeText):
    Removals = ['http\S+\s*', 'RT|cc', '#\S+', '@\S+', '\s+']
    
    for r in Removals: resumeText = re.sub(r, ' ', resumeText)
    resumeText = re.sub('[%s]'%re.escape("""!"#$%&'_=-+()[];:,./?^*@{}|\~"""), ' ', resumeText)
    resumeText = re.sub(r'[^x00-x7f]', r' ', resumeText)
    
    return resumeText                                                           # REDUCTIONS





class Data_Cleaner:
    Punc_List = ("'", '"', '!', '?', '#', '@', '(', ')', '[', ']', '{', '}', '+', '-', '*', '/', '\\', '&', '|', '~', '%', '^', ',', '.', ':')

    def __init__(self): pass
    

    def Clean(Data : str, Numbers = False, Cap_Alphas = False, Small_Alphas = False,
        Punctuations = True, HashTags = True, Mentions = True, Urls = True, Emails = True,
        Multi_Space = True, New_Lines = False):
        
        """
        Data :: String Cleaner
        ======================
        Set Attributes to True which should be Cleaned
        
        The function recognizes characters as Punctuations if present in Data_Cleaner.Punc_List
        """
        
        from itertools import chain
        import re
        
        if Emails    == True: Data = re.sub('[A-Za-z0-9]*@[a-z]*\.[a-z]*', '', Data)
        if Urls      == True: Data = re.sub('/[A-Za-z]+', '', Data)
        if Mentions  == True: Data = re.sub('@[A-Za-z 0-9]*', '', Data)
        if HashTags  == True: Data = re.sub('#[A-Za-z0-9]*', '', Data)
        
        Ord_Chars = dict(zip(
          [range(48, 58), range(65, 91), range(97, 123), map(lambda x: ord(x), Data_Cleaner.Punc_List)],
          [Numbers, Cap_Alphas, Small_Alphas, Punctuations]))
          
        Valid = list(chain(*map(lambda kv: range(0) if kv[1] else kv[0], Ord_Chars.items())))

        Result = ''.join([char for char in Data if ord(char) in Valid or char in [' ', '\n']])
        if Multi_Space == True: Result = ' '.join(Result.split()) if New_Lines else re.sub(' +', ' ', Result) 

        return Result




if __name__ == '__main__':
    print(tuple(''''"!?#@()[]{}+-*/\&|~%^,.:'''))
    print(Data_Cleaner.Clean('''!"#$%&'_=-+(How are you)[Hey];:,./?^*@{I'm Jarvis}|\~''', True, Punctuations=True))