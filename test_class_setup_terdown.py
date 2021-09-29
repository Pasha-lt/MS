class TestClass:
    @classmethod
    def setup_class(cls):
        print(f'\n{"*" * 30}\n Setup class \n{"*" * 30}')
    
    @classmethod
    def teardown_class(cls):
        print(f'\n{"*" * 30}\n teardown class\n{"*" * 30}')

    def setup_method(self, method):
        print(f'\n{"*" * 30}\n Setup method, {method} \n{"*" * 30}')

    def teardown_method(self, method):
        print(f'\n{"*" * 30}\n teardown method, {method} \n{"*" * 30}')

    def test_tcst_1(self):
        print(f'\n{"*" * 30}\n tcst_1 \n{"*" * 30}')

    def test_tcst_2(self):
        print(f'\n{"*" * 30}\n tcst_2\n{"*" * 30}')

'''
Когда мы делаем вешаем декоратор класметода на сетуп тердаун то он отработает в начале и конце всех
тестов, а не как в случае с методом после каждого.

test_class_setup_terdown.py
******************************
 Setup class
******************************
******************************
 Setup method, <bound method TestClass.test_tcst_1 of <test_class_setup_terdown.TestClass object at 0x7f9b1ebb7c18>>
******************************
******************************
 tcst_1
******************************
******************************
 teardown method, <bound method TestClass.test_tcst_1 of <test_class_setup_terdown.TestClass object at 0x7f9b1ebb7c18>>
******************************
******************************
 Setup method, <bound method TestClass.test_tcst_2 of <test_class_setup_terdown.TestClass object at 0x7f9b1ebb7ac8>>
******************************
******************************
 tcst_2
******************************
******************************
 teardown method, <bound method TestClass.test_tcst_2 of <test_class_setup_terdown.TestClass object at 0x7f9b1ebb7ac8>>
******************************
******************************
 teardown class
******************************
'''