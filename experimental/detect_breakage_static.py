import ast
import importlib
import os

def get_package_info(pkgname):
    """returns a dict containing info about modules, classes, functions"""
    spec = importlib.util.find_spec(pkgname)
    locations = [l for l in spec.submodule_search_locations]
    root_dir = locations[0]
    info = _get_package_info(root_dir)
    return info

def _get_package_info(root_dir):
    info = {}
    info['modules'] = {}
    subpackages = []
    for name in os.listdir(root_dir):
        if name.startswith('_'):
            continue
        elif name.endswith('.py'):
            path = os.path.join(root_dir, name)
            with open(path) as f:
                node = ast.parse(f.read(), path)
            modname = name[:-3]
            info['modules'][modname] = get_module_info(node)
        elif not name.startswith('.'):
            subpackages.append(name)

    info['subpackages'] = {}
    for name in subpackages:
        path = os.path.join(root_dir, name)
        info['subpackages'][name] = _get_package_info(path)

    return info

def get_module_info(node):
    """returns a dict containing info on classes and functions"""
    classes = [n for n in node.body if isinstance(n, ast.ClassDef)]
    functions = [n for n in node.body if isinstance(n, ast.FunctionDef)]

    res = {}
    res['classes'] = get_class_info(classes)
    res['functions'] = get_function_info(functions)

    return res

def get_class_info(classes):
    """returns a dict containing info on args, subclasses and functions"""
    res = {}
    for node in classes:
        if node.name.startswith('_'):
            continue

        init_func = None
        subclasses, functions = [], []
        for n in node.body:
            if hasattr(n, 'name') and n.name == '__init__':
                init_func = n
            if isinstance(n, ast.ClassDef):
                subclasses.append(n)
            elif isinstance(n, ast.FunctionDef):
                functions.append(n)

        args = []
        if init_func is not None:
            args = get_args(init_func.args)

        res[node.name] = {}
        res[node.name]['args'] = args
        res[node.name]['subclasses'] = get_class_info(subclasses)
        res[node.name]['functions'] = get_function_info(functions)

    return res

def get_function_info(functions):
    """returns a dict mapping function name to function args"""
    res = {}
    for node in functions:
        if node.name.startswith('_'):
            continue
        res[node.name] = {}
        res[node.name]['args'] = get_args(node.args)
    return res

def get_args(node):
    args = []
    for arg in node.args:
        if isinstance(arg, ast.arg):
            args.append(arg.arg)
        elif isinstance(arg, ast.Name):
            args.append(arg.id)
        # Testing - will delete later
        else:
            from pdb import set_trace; set_trace()
    return args

# Testing - will delete later
if __name__ == '__main__':
    pkgname = 'compatibility_lib'
    # pkgname = 'google.cloud.bigquery'
    res = get_package_info(pkgname)

    import json
    print(json.dumps(res, indent=4, sort_keys=True))
