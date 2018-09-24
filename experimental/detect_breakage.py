import enum
import importlib
import inspect
import pkgutil

ARGLESS_CLASSES = [
    enum.Enum,
    enum.IntEnum,
    enum.IntFlag,
    enum.Flag,
]

def get_package_info(pkgname):
    """returns a dict containing info about modules, classes, functions"""
    pkg = importlib.import_module(pkgname)
    return _get_package_info(pkg)

def _get_package_info(pkg):
    """returns a dict containing info about modules, classes, functions"""
    _modules = pkgutil.walk_packages(pkg.__path__)
    modules = []
    subpackages = []
    for (_, name, ispkg) in _modules:
        if not name.startswith('_'):
            import_str = '%s.%s' % (pkg.__name__, name)
            # try:
            #     obj = importlib.import_module(import_str)
            #     if ispkg:
            #         subpackages.append(obj)
            #     else:
            #         # _module = pkg.__loader__.load_module(name)
            #         modules.append(obj)
            # except:
            #     print('skipped %s, %s' % (import_str, ispkg))

            # new from py3.5
            fullname = '%s.%s' % (pkg.__name__, name)
            spec = importlib.util.find_spec(fullname)
            if spec is not None:
                obj = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(obj)
                if ispkg:
                    subpackages.append(obj)
                else:
                    modules.append(obj)
            else:
                print("not found/skipped %s (ispkg: %s)" % (fullname, ispkg))


    res = {}
    res['modules'] = get_module_info(modules)
    res['subpackages'] = {}
    for subpkg in subpackages:
        res['subpackages'][subpkg.__name__] = _get_package_info(subpkg)
    return res

def get_module_info(modules):
    """returns a dict containing info on classes and functions"""
    res = {}
    for module in modules:
        modname = module.__name__
        res[modname] = {}

        classes = inspect.getmembers(module, inspect.isclass)
        classes = [c for c in classes if c[1].__module__ == modname]
        functions = inspect.getmembers(module, inspect.isfunction)
        functions = [f for f in functions if f[1].__module__ == modname]

        res[modname]['classes'] = get_class_info(classes)
        res[modname]['functions'] = get_function_info(functions)
    return res

def get_class_info(classes):
    """returns a dict containing info on args, subclasses and functions"""
    res = {}
    for name, value in classes:
        if not name.startswith('_'):
            res[name] = {}
            res[name]['args'] = get_class_args(value)

            modname = value.__module__
            subclasses = inspect.getmembers(value, inspect.isclass)
            subclasses = [s for s in subclasses if s[1].__module__ == modname]
            res[name]['subclasses'] = get_class_info(subclasses)

            functions = inspect.getmembers(value, inspect.isfunction)
            functions = [f for f in functions if f[1].__module__ == modname]
            res[name]['functions'] = get_function_info(functions)
    return res

def get_class_args(value):
    special_class = False
    for argless_class in ARGLESS_CLASSES:
        if issubclass(value, argless_class):
            special_class = True
            break

    args = []
    if not special_class:
        try:
            args = inspect.getfullargspec(value).args
        except TypeError:
            pass

    return args

def get_function_info(functions):
    """returns a dict mapping function name to function args"""
    res = {}
    for name, value in functions:
        if not name.startswith('_'):
            res[name] = {}
            args = inspect.getfullargspec(value).args
            res[name]['args'] = args
    return res


# Testing - will delete later
if __name__ == '__main__':
    pkgname = 'compatibility_lib'
    res = get_package_info(pkgname)

    import json
    print(json.dumps(res, indent=4, sort_keys=True))

