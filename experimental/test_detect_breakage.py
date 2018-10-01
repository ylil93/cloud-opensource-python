import ast
import unittest

from detect_breakage_static import get_package_info, get_module_info


class TestSimplePackages(unittest.TestCase):
    def setUp(self):
        self.expected_function_res = {
            'modules': {
                'simple_function': {
                    'classes': {},
                    'functions': {
                        'hello': {
                            'args': []
                        }
                    }
                },
            },
            'subpackages': {}
        }


    def test_simple_function(self):
        location = '/usr/local/google/home/pekopeko/Google/cloud-opensource-python/experimental/test/simple_function'
        info = get_package_info(location)
        self.assertEqual(self.expected_function_res, info)

    def test_simple_class(self):
        location = '/usr/local/google/home/pekopeko/Google/cloud-opensource-python/experimental/test/simple_class'
        info = get_package_info(location)

    def test_simple_types(self):
        pass


class TestInheritance(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple_inheritance(self):
        res = {
            'args': [],
            'functions': {
                'foo': {
                    'args': []
                },
                'moo': {
                    'args': []
                }
            },
            'subclasses': {}
        }
        location = '/usr/local/google/home/pekopeko/Google/cloud-opensource-python/experimental/test/simple_inheritance'
        info = get_package_info(location)

        self.assertEqual(res, info['modules']['simple_inheritance']['classes']['Foo'])
        self.assertEqual(res, info['modules']['simple_inheritance']['classes']['Bar'])

    def test_multiple_inheritance(self):
        code = (
            'class Bar(object):\n'
            '    def foo(a):\n'
            '        pass\n'
            'class Baz(object):\n'
            '    def foo(b):\n'
            '        pass\n'
            'class Foo(Bar, Baz):\n'
            '    pass\n')

        node = ast.parse(code)
        res = get_module_info(node)
        from pdb import set_trace; set_trace()
        self.assertEqual(['a'], res['classes']['Foo']['functions']['foo']['args'])

class TestBackwardsCompatibility(unittest.TestCase):
    def setUp(self):
        pass

    def test_base_class_removal(self):
        pass

if __name__ == '__main__':
    unittest.main()
