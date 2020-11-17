class A:
    def hello(self):
        print('hello')

def b():
    print('world')

a = A()
print(dir(A))
print(dir(a))
print(type(a.hello))
print(dir(a.hello))
# true
print(id(a.hello.__self__)==id(a))

print(id(a.hello)==id(a.hello.__func__))

print(type(b))
print(dir(b))