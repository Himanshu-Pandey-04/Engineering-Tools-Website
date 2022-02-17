#!/usr/bin/env python
# coding: utf-8

# In[5]:


from inspect import signature, getmembers, isfunction
import importlib.util as iu
import sys, os, re
# from typing import DefaultDict

def GetDict():
    functions = {}
    codeFiles = []
    codes = r'.\codes'


    # In[6]:


    ignoreEntities = {
        'files' : [
            '.*__init__.*',
            '.*manager.*'
        ],
        
        'dirs' : [
            '.*__pycache__.*',
        ],
    }


    # In[7]:


    for (root, _, files) in os.walk(codes):
        ignore = False
        for dir in ignoreEntities['dirs']:
            if re.search(dir, root):
                ignore = True
        
        if ignore: continue

        for item in files:
            for file in ignoreEntities['files']:
                if re.search(file, item): break
            else: codeFiles.append((item, os.path.join(root, item),))


    # In[8]:


    for file_path in codeFiles:
        spec = iu.spec_from_file_location(*file_path)
        foo = iu.module_from_spec(spec)
        spec.loader.exec_module(foo)
        for func in getmembers(foo, isfunction):
            functions[func[0]] = func[1]
            # functions[func[0]] = functions.get(func[0], set()).union({func[1]})


    # In[9]:


    for name,func in functions.items():
        print(name, func)
        print('\n\n')
        # if func[0] == 'Co_Prime':
            # print(func[0], func[1](3, 14))


    # In[10]:


    functions


    # In[11]:


    func_Lib = functions.values()
    func_Lib


    # In[20]:


    from inspect import signature




    Dict = {
        'function_name': {
            'docS': 'tooltip',
            'params': {
                'p1': ['int', 'tooltip'],
                'p2': ['str', 'tooltip']
            },
        
            'returns': {
                'r1': ['list', 'tooltip']
            },
        
            'tags': ['tag1', 'tag2']
        }
    }


    Dict = {}


    pyDT_To_HTML = {
        float: 'number',
        int: 'number',
        str: 'text',
        range: 'range',
        list: 'range',
        tuple: 'range',
        set: 'range',
    }

    for func in func_Lib:
        Sig = signature(func)
        Dict[func.__name__] = {}
        Dict[func.__name__]['docS'] = func.__doc__
        Dict[func.__name__]['params'] = { name : Type.annotation for name, Type in Sig.parameters.items() }
        Dict[func.__name__]['returns'] = { 'r1' : Sig.return_annotation }
        Dict[func.__name__]['call'] = func

    return Dict

if __name__=="__main__":
    print(GetDict())

