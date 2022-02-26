from inspect import signature, getmembers, isfunction
import importlib.util as iu
import sys, os, re


path = r'.\codes'

funcLib = {}

encloser = ''' <section class="sidebar col-3"></section>'''
dir_div = '''
<div class="dropdowns">
    <button class="btn Subjects" id="btn-$name$" onclick="DropDownToggle('$name$')">$name$</button>
    <ul class="menu" id="list-$name$">
        $children$
    </ul>
</div>'''
# dir_div = '''<ul class="menu" id="list-$name$">$children$</ul>'''
func_leaf = '''<li class="item"><a href="#">$name$</a></li>'''

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



def get_html(parent = path):
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
                    funcs.append(func_leaf.replace('$name$', name_func[0]))
                dirChildren.append(dir_div.replace('$children$', ''.join(funcs)).replace('$name$', os.path.splitext(item)[0]))
        else: dirChildren.append(get_html(fullPath))
    return dir_div.replace('$children$', ''.join(dirChildren)).replace('$name$', parent[parent.rindex('\\')+1:])





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



if __name__ == '__main__':
    # # Testing

    # print(get_html())
    get_html()

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