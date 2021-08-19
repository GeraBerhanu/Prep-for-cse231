def do_twice(f,x):
    f(x)
    f(x)

do_twice(print, ('spam'))

def print_spam():
    print('spam')


def print_twice(x):
    print(x)
    print(x)

do_twice(print_twice, ('spam'))

def do_four(f,x):
    do_twice(f,x)
    do_twice(f,x)

do_four(print, ('spam'))

def make_grid():
    print('+ - - - - + - - - - +',)
    print('|         |         |'  ) 
    print('|         |         |'  ) 
    print('|         |         |'  ) 
    print('|         |         |'  ) 
    print('+ - - - - + - - - - +',)
    print('|         |         |'  ) 
    print('|         |         |'  ) 
    print('|         |         |'  ) 
    print('|         |         |', ) 
    print('+ - - - - + - - - - +',)



def make_ts():
    print('+ - - - - + - - - - +',)



def make_i():
    do_four(print, '|         |         |')

def make_grid2():
    make_ts()
    make_i()
    make_ts()
    make_i()
    make_ts()

make_grid2()

