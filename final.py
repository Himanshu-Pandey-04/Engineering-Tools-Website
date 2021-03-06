from filecmp import dircmp
from inspect import signature, getmembers, isfunction
import importlib.util as iu
import sys, os, re


path = r'C:\Users\hp\AppData\Local\Programs\Python\Python39\Lib\site-packages\codes'

funcLib = {}

encloser = '''<div class="toolbar">
    <div id="tool-nav">
        <i class="bx bx-menu" id="tool-btn"> Tools</i>
    </div>
    <ul class="nav-list">
        $children$
    </ul>
</div>'''
dir_div = '''
<li>
    <span class="option lvl-$lvlNo$" onclick="DropDownToggle('$name$')" title="$name$">$name$</span>
    <ul id="list-$name$">
        $children$
    </ul>
</li>'''
# dir_div = '''<ul class="menu" id="list-$name$">$children$</ul>'''
func_leaf = '''<a href="#" class="option lvl-$lvlNo$ funcs" onclick="OpenTool('$funcName$')" title="$name$">
    $name$
</a>'''

pyDT_To_HTML = {
    float: 'number',
    int: 'number',
    str: 'text',
    range: 'range',
    list: 'range',
    tuple: 'range',
    set: 'range',
}


ignoreEntities = {
    'files' : [
        '.*__init__.*',
        '.*manager.*',
        '.*\.ipynb',
        '.*\.pyc'
    ],
    
    'dirs' : [
        '.*__pycache__.*',
    ],
}


name_conversions = {
    'cn': 'Computer Networks',
    'ldco': 'Logic Design and Computer Organization',
    'hamming_distance': 'Hamming Distance (HD)',
    'mhd_ed_ec': 'Error Control and Detection',
    'BST': 'Binary Search Trees (BST)'
}


def Name_Formatter(name : str):
    name = name.strip()
    if not name: return ''
    if name.startswith('_'): name = name[1:]
    if name.endswith('_'): name = name[:-1]
    name = name_conversions.get(name.lower(), name)
    chunks = name.translate(str.maketrans(dict.fromkeys(['_', '.'], ' '))).split()
    for i in range(len(chunks)):
        chunks[i] = str.upper(chunks[i][0]) + chunks[i][1:]
    return ' '.join(chunks)




def get_funcs(file : str, path : str):
    spec = iu.spec_from_file_location(file, path)
    foo = iu.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return getmembers(foo, isfunction)




def get_hierarchy(parent = path):
    if os.path.isfile(parent): return None
    hierar = {}

    for item in os.listdir(parent):
        ignore = False
        for igDir in ignoreEntities['dirs']:
            if re.search(igDir, item):
                ignore = True
                break
        if ignore: continue

        fullPath = parent + '\\' + item
        if os.path.isfile(fullPath):
            for igrfile in ignoreEntities['files']:
                if re.search(igrfile, item): break
            else:
                hierar[item] = []
                for name_func in get_funcs(item, fullPath):
                    if name_func[0][:3] == 'Igr': continue
                    hierar[item].append(name_func[0])
                    func = name_func[1]
                    Sig = signature(func)
                    funcLib[func.__name__] = {
                        'docS' : func.__doc__, 'returns' :  { 'r1' : Sig.return_annotation }, 'call' :  func,
                        'params' :  { name : Type.annotation for name, Type in Sig.parameters.items() },
                    }
        else: hierar[item] = get_hierarchy(fullPath)
    return hierar



def get_html(parent = path, lvl = 0):
    if os.path.isfile(parent): return None
    dirChildren = []

    for item in os.listdir(parent):
        ignore = False
        for igDir in ignoreEntities['dirs']:
            if re.search(igDir, item):
                ignore = True
                break
        if ignore: continue

        fullPath = parent + '\\' + item
        if os.path.isfile(fullPath):
            for igrFile in ignoreEntities['files']:
                if re.search(igrFile, item): break
            else:
                funcs = []
                for name_func in get_funcs(item, fullPath):
                    if name_func[0][:3] == 'Igr': continue
                    funcs.append(func_leaf.replace('$name$', Name_Formatter(name_func[0]).replace('$funcName$', name_func[0])).replace('$lvlNo$', str(lvl+2)))
                dirChildren.append(dir_div.replace('$children$', ''.join(funcs)).replace('$lvlNo$', str(lvl+1)).replace('$name$', Name_Formatter(os.path.splitext(item)[0])))
        else: dirChildren.append(get_html(fullPath, lvl+1))
    
    if parent[parent.rindex('\\')+1:] == 'codes': return encloser.replace('$children$', ''.join(dirChildren))
    return dir_div.replace('$children$', ''.join(dirChildren)).replace('$name$', Name_Formatter(parent[parent.rindex('\\')+1:])).replace('$lvlNo$', str(lvl))





def hierar_n_lib(parent = path):
    """Hierarchy and Function Library Generator
        =======================================
        1. Generates Folder -> Sub-folder -> File -> Function Hierarchy
        2. Generates Dictionary containing Function name mapped to function description and call
        
        Parameters
        ----------
        1. parent - Path to directory containing files and folders of neccessary functions

        Returns
        -------
        1. hierar : dict -> Directory Hierarchy from root folder to function names
        2. funcLib : dict -> Function-name mapped to function description and call

        Example
        -------
        >>> import final
        >>> hierarchy, funcLib = final.hierar_n_lib()
        """
    return get_hierarchy(parent), funcLib



def print_indent(items, indent = 0, indent_increment = 8):
    if items is None: return
    for item in items:
        print(' '*indent + item)
        if isinstance(items, dict) and isinstance(items[item], dict):
            print_indent(items[item], indent+indent_increment, indent_increment)


import pyperclip as pc
if __name__ == '__main__':
    # # Testing

    gh = get_html()
    print(gh)
    pc.copy(gh)

    # ### Directory Hierarchy Check
    # hierarchy = hierar_n_lib(path)
    # print_indent(hierarchy)

    # ### Function Library Testing
    # print(funcLib)
    # print(funcLib['Co_Prime']['call'](23,45))
    # print(funcLib['Co_Prime']['call'](23,46))

    """
    <div className='lvl_1'>
        <div className='lvl_2'>
        </div>
    </div>
    """