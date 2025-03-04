#Example of simple one level inheritance
class ParentClass:
    def __init__(self,param1,param2,param3):
        self.param1=param1
        self.param2=param2
        self.param3=param3
    
    def func1(self):
        print(f"This is func1 of the parent class {self.param1}{self.param2}{self.param3} ")

class Child1(ParentClass):
        def __init__(self,param1,param2,param3,child_param1):
            super().__init__(param1,param2,param3)
            self.child_param1=child_param1
        
        def childfunc1(self):
            print(f"This is childfunc1 of the inheritedchild class {self.child_param1} ")

parent_obj1=ParentClass('p1','p2','p3')
parent_obj1.func1()
child_obj1=Child1('p1','p2','p3','c1')
child_obj1.childfunc1()
