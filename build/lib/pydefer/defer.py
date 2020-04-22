from contextlib import ExitStack
from functools import wraps, partial

def defer(func,*func_args,DEBUG=False,file=False):
    '''
    Defers a function until after the wrapped function has been executed.

    `func` - takes in a function's name (their `__name__`)

    `*args` - the arguments that would be passed into the func
    '''
    def dec(f):
        @wraps(f)
        def wrapped_func(*args, **kws):
            if DEBUG:
                print('__________ENTERING EXIT CALLBACK STACK__________\n')
                with ExitStack() as stack:
                    stack.callback(partial(func,*func_args))

                    stack.callback(partial(print,'__________DEFERRED FUNCTION RESULTS__________\n'))
                    stack.callback(partial(print,'__________RETURNING TO EXIT CALLBACK STACK__________\n'))
                    print('__________WRAPPED FUNCTION RESULTS__________\n\n')
                    return f(*args, **kws)
            else:
                with ExitStack() as stack:
                    stack.callback(partial(func,*func_args))
                    return f(*args, **kws)

        return wrapped_func
    return dec
    
@defer(open('test3.txt','a').close)
def test3():
    f = open('test3.txt','w')
    f.write('test3')

@defer(print,'butt',DEBUG='DEBUG')
def test2():
    print('test2')

@defer(print,'working',2345,2345,234,1)
def test():
    print(5)
    print(4)
    print(3)
    print(2)
    print(1)

if __name__ == '__main__':
    # test()
    # test2()
    test3()
    # print('end test')
