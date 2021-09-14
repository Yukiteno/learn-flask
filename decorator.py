from functools import wraps

def a_decorator(a_func):
  @wraps(a_func)
  def wrapTheFunction():
    print('before excute a_func()')

    a_func()

    print('after excute a_func()')

  return wrapTheFunction

def need_decoration():
  print('I needs some decoration')

need_decoration()

need_decoration = a_decorator(need_decoration)
need_decoration()

print('---------')

@a_decorator
def need_decoration_too():
  print('I needs some decoration too')

need_decoration_too()

print('---------')

print(a_decorator.__name__)
print(need_decoration.__name__)
print(need_decoration_too.__name__)