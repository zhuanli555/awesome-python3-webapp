class student(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    def print_name(self):
        print('%s' % self.__name)

    def print_age(self):
        print('%d' % self.__age)
ogb = student('zhuanli',12)
if hasattr(ogb,'print_age'):
    print('true')