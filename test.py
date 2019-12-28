import unittest
from asm1 import simple_assembler

code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a
'''

program = ['mov a 5', 'inc a', 'dec a', 'dec a', 'jnz a -1', 'inc a']

class MyTestCase1(unittest.TestCase):

    def test_p(self):
        self.assertEqual(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})


class MyTestCase2(unittest.TestCase):

    def test_p1(self):
        self.assertEqual(simple_assembler(program), {'a': 1})


if __name__ == '__main__':
    unittest.main()
    
