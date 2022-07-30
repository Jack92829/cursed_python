# def outer():
#     x = 5
#     def inner():
#         nonlocal x
#         x = 4
#         print(f"Inner: {x}")
    
#     inner()
#     print(f"Outer: {x}")

# outer()

# from __future__ import annotations

# def _(func):
#     stuff = func.__annotations__["return"].strip("None - {").strip("}").replace(", ", "\n")

#     def wrapper(*args, **kwargs):
#         exec(stuff)

#     return wrapper


# @_
# def function() -> None-{
#     print("test"),
#     print("Hello world")
# }:...

# function()

# from PIL import Image, ImageDraw

# import random, math, colorsys

# def random_color():
#     # I want a bright, vivid color, so max V and S and only randomize HUE.
#     h = random.random()
#     s = 1
#     v = 1
#     float_rbg = colorsys.hsv_to_rgb(h, s, v)
#     # Return as integer RGB.
#     return (
#         int(float_rbg[0] * 255),
#         int(float_rbg[1] * 255),
#         int(float_rbg[2] * 255),
#     ) 

# def generate_art():
#     print('Generate Art')
#     image_size_px = 2000
#     image_bg_color = (255,255,255)
#     image = Image.new(
#         "RGB",
#         size=(image_size_px, image_size_px),
#         color = image_bg_color
#     )
#     draw = ImageDraw.Draw(image)
#     points = []
#     starting_pos = (0,image_size_px*.50),(image_size_px,image_size_px*.50)
#     x = 0
#     y = image_size_px*.50
#     for _ in range(0, math.ceil(10)):
#         x += 200
#         y += (100-random.randint(0, image_size_px*0.4))
#         if y >= image_size_px*0.4: 
#             y -=300
#         elif y <= image_size_px*0.4:
#             y += 300
#         newpoints = (x, y)
#         points.append(newpoints)
#         y -= (100-random.randint(0, image_size_px*0.4))
#         x += 200
#         newpoints = (x, y)
#         points.append(newpoints)
#         line_xy= (points)
#         print(line_xy)
#     smoothness_factor = 300
# #     for point in line_xy:
# #          print(point)
# #          draw.ellipse((point[0], point[1], point[0]+50, point[1]+50), fill=random_color())
#     for point1, point2 in zip(line_xy[:-1], line_xy[1:]):

#         print(point1, point2)
#         x_diff = point2[0] - point1[0]
#         y_diff = point2[1] - point1[1]
#         print(x_diff, y_diff)

#         x_increment = x_diff / smoothness_factor
#         y_increment = y_diff / smoothness_factor
        
#         print(x_increment, y_increment)
#         print("\n\n")
#         x_pos = point1[0]
#         y_pos = point1[1]

#         print(x_increment)
#         print(y_increment)
#         for _ in range(smoothness_factor):
#             draw.ellipse((x_pos, y_pos, x_pos+50,y_pos+50), fill=random_color())
#             x_pos += x_increment
#             y_pos += y_increment

#     image.save('test_image.png')
# if __name__ == "__main__":
#     generate_art()

# import time,sys
# indend = 0
# inendincreasing = True
# try:
#     while True:
#             print('  ' * indend, end='')
#             print('**********')
#             time.sleep(0.1)

#             if inendincreasing:
#                 indend = indend + 1
#                 if indend == 20:
#                     inendincreasing = False
#             else: 
#                 indend = indend - 1
#                 if indend == 0:
#                     inendincreasing = True
# except KeyboardInterrupt:
#     sys.exit()

# class Thing:
#     def __str__(self):
#         raise NotImplementedError("Nope, you don't get to print")
    
#     def __repr__(self):
#         print("Hello")

# a = Thing()

# print(a)

# l = [[1, 3, 7],
#      [8, 5, 5],
#      [7, 5, 1],
#      [7, 0, 2]]

# transposed_l = [list(item) for item in zip(*l)]

# print(transposed_l)
# print([*zip(*l)])



# def func(a, b):
#     return a + b

# val = 5
# l = [1, 8, 7, 4, 6]

# print(list(map(func, 10, l)))

# from sys import getsizeof

# integer = 45645465555

# print(getsizeof(integer))
# print(getsizeof(True))

# print(getsizeof((True,)))

# a = True
# print(getsizeof((a, a, a)))





# name = age = bday = "something"

# info = {
#   (name, age): ("Ruby", 28),
#   bday: "August 25, 1993",
# }

# print(info)




# from __future__ import annotations

# @lambda _:_()
# class __annotations__:
#     def __setitem__(self, name, value):
#         globals()[value] = globals()[name]

# class Number:
#     def __init__(self, value):
#         self.value = value

#     def __pos__(self):
#         self.value += 0.5
#         return self
    
#     def __str__(self):
#         return str(int(self.value))

# class console:
#     def log(*args, **kwargs): 
#         print(*args, **kwargs)

# let: i = Number(5);

# ++i;
# console.log(i);




# from __future__ import annotations

# @lambda _:_()
# class __annotations__:
#     def __setitem__(self, k, v):
#         if k == "For":
#             self.condition = v.split(",")[1].strip()
#             self.var = v.split(",")[0].strip("(")
#             globals()[self.var] = 0

#         elif k == "_":
#             code = v.strip("{").strip("}").strip().split(", ")
#             code_string = "\n".join(stuff.strip("'") for stuff in code)

#             while eval(self.condition):
#                 exec(code_string)
#                 globals()[self.var] += 1

# For:(x, x < 4, ++x);_:{
#     print("Hello world"),
#     print(x)
# }


# class Something:
#     def __format__(value, format_spec):
#         print(value)
#         print(format_spec)

#         return ""

# a = Something()

# f"{a:hh,nlyENIEH<[]}"





# @lambda _:_()
# class let_the_world_burn:
#     def __format__(_, format_spec):
#         header=format_spec.split("(")[1].split(")")[0].split(";");header[0]=header[0].split("let ")[1];body="\n".join(x.strip() for x in format_spec.split("[")[1].strip().split("]")[0].strip().split("\n"));globals()[header[0]]=0
#         while eval(header[1]):exec(body);globals()[header[0]] += 1
#         return ""
# f"""{let_the_world_burn:


# for (let i; i < 4; i++)[
#     print(i)
#     print("Hello world")
# ]


# }"""



# class While:
#     ___=lambda self: ((exec(self.__), globals().update(locals()), 
#           type(self)(self.___, self.__)) 
# if eval(self.___) else ...)
#     def __init__(self, __, ___):self.___ = __; self.__ = ___;((_ := globals()['__builtins__'].setattr), (
#           x := getattr(self.__class__, 
#      (_(self.__class__, (t := "__del__"), lambda ________: (...,...)), 
#        t)[1]), _(x, "__code__", While.___.__code__)))

    
# x = 3
# While("x < 50", "x += 3")
# print(x)


# a: int = 5
# b: float = 5.0
# c: complex = 5j
# d: bool = True
# e: str = "lol"
# f: list[int] = [5, 6]
# g: tuple[str] = ("hello", "world")
# j: dict[str, int] = {"hi": 5}
# k: set[int] = {1, 2, 3}
# x: list[any] = [a, b, c, d, e, f, g, j, k]
# y: list[tuple[any]] = [(type(i).__name__, i) for i in x]
# for t in y:
#     print(f"type: {t[0]:-<8} -> {t[1]}")


# class Dog:
#     def __init__(self, breed, colour):
#         self.breed = breed
#         self.colour = colour

#     @classmethod
#     def golden_retriever(cls):
#         return cls("Golden retriever", "yellowish I guess")

# my_dog = Dog.golden_retriever()

# print(my_dog.breed)


# def func():
#     var = 10
#     def inner():
#         nonlocal var
#         var = var + 5

#     inner()
#     print(var)

# func()





# _,=-- 5     ,





# while (i := globals().setdefault("i", 0)) < 5: print(i); i += 1






# class Test:
#     def __init__(self):
#         self.counter = 0
#         self.done = False

#     @property
#     def step(self):
#         ...
    
#     @step.setter
#     def step(self, yep):
#         if yep == self.limit:
#             self.done = True
    
#     def __call__(self, limit):
#         self.limit = limit
#         return self

#     def __iter__(self):
#         print("hi")
#         return self

#     def __next__(self):
#         if self.done:
#             raise StopIteration

#         self.counter += 1
#         return self.counter
        

# count = Test()

# for count.step in count(10):
#     print("test")






# @lambda _:_()
# class _:
#     def __format__(_, format_spec):
#         name = format_spec.strip().split("++")[0];globals()[name] += 1;return ""

# x = 0
# f'''{_:


# x++


# }'''

# print(x)






# import inspect

# class Thing:
#     def __init__(self, value):
#         self.value = value
#         self.flag = False
    
#     def __neg__(self):
#         ok = inspect.getframeinfo(inspect.currentframe().f_back).code_context[0].strip()

#         if ok.count("-") == 1:
#             return Thing(-self.value)
#         elif ok.count("-") == 2:
#             if not self.flag:
#                 self.flag = True
#                 return self
#             else:
#                 self.flag = False
#                 self.value -= 1
#                 return self
#         else:
#             print("No clue")

#     def __str__(self):
#         return str(self.value)


# a = Thing(10)

# print(-a)
# print(--a)
# print(a)




# _,=-- 5     ,


# var ,=-- 5     ,

# print(var)



# def test():
#     yield f"Hello {yield}"


# c = test()
# print(next(c))
# print(c.send("World"))


# def testing():

#     yield 5
    
#     yield f'{yield}'

# a = testing()
# print(next(a))
# print(a.send("testing"))








# class _(metaclass=(type("__", (type,), {"__init__": lambda cls, name, bases, dct: print(f"""a{setattr(cls, '__del__', lambda self: print(f"Hello World! {type(self)()}"[0:11]))}{cls()}"""[0].replace('a', ''), end="")}))):...








# import ctypes;ctypes.c_char.from_address(id("Hello World!") + 48 + 2).value = "z".encode()

# print("Hello World!")






# from dis import dis 

# dis(
# """
# for _ in range(5):
#     print("test")
# """
# )






# import ctypes;ctypes.c_int.from_address(id(4) + int.__basicsize__).value = 3




# print(2 + 2)






# from __future__ import annotations

# @lambda _:_()
# class __annotations__:
#     def __setitem__(self, name, item):
#         if name == "print":
#             to_print = (stuff.strip() for stuff in item.strip("(").strip(")").split(","))
#             print(*to_print)

# print:(Hello, World)








# import asyncio

# async def func1():
#     print("hi")
#     print("What?")
#     await asyncio.sleep(1)
#     print("Hello again")

# def func2():
#     loop = asyncio.get_event_loop()
#     loop.create_task(func1())
#     print("Hey there")

# async def main():
#     func2()
#     await asyncio.sleep(1)  # free up the even loop for func1 to finish up


# asyncio.run(main())







# l = [1, 2, 10, 11, 3, 5]

# match l:
#     case [1, x, 10, *_]:
#         print(x)





# import ctypes

# for i,ii in zip(range(len("Hello World!")),"Bye World!  "):ctypes.c_char.from_address(id("Hello World!")+48+i).value=ii.encode()




# print("Hello World!")

# @lambda _:_()
# class insert:
#     def __format__(self, _):
#         return globals()[_.split()[-1]]


# var = "World!"

# print(f"hello {insert:variable with name var}")




# import tempfile;import sys;a=sys.stdout;sys.stdout=(yep:=tempfile.TemporaryFile("r+"));import __hello__;yep.seek(0);[setattr(__import__("ctypes").c_char.from_address(id("Adios world")+48+i),"value",ii.encode())for i,ii in zip(range(len("Adios world")),yep.read())];sys.stdout=a


# print("Adios world")


# class Event:
#     def __init__(self, function):
#         self.trigger = function
#         self.hooked_functions = []
    
#     def hook(self, hook):
#         self.hooked_functions.append(hook)


# @Event
# def water_falling_rapidly():
#     ...

# @water_falling_rapidly.hook
# def activate_led():
#     ...

# @water_falling_rapidly.hook
# def sound_buzzer():
#     ...

# @water_falling_rapidly.hook
# def console_warning():
#     ...





# from math import sqrt

# a = input("Enter side a: ")
# b = input("Enter side b: ")
# c = input("Enter side c: ")

# if not a:
#     print(f"Side a = {sqrt(float(c) ** 2 - float(b) ** 2)}")
# elif not b:
#     print(f"Side b = {sqrt(float(c) ** 2 - float(a) ** 2)}")
# else:
#     print(f"Side c = {sqrt(float(a) ** 2 + float(b) ** 2)}")


# annual_income = float(input("Enter annual income: "))

# if annual_income <= 18_200:
#     print("$0")
#     print("0%")
# elif annual_income <= 45_000:
#     print(f"${annual_income - 18_200}")
#     print(f"{((annual_income - 18_200) * 0.19) / annual_income * 100}%")
# elif annual_income <= 120_000:
#     print(f"${annual_income - 45_000}")
#     print(f"{(5_092 + (annual_income - 45_000) * 0.325) / annual_income * 100}%")
# elif annual_income <= 180_000:
#     print(f"${annual_income - 120_000}")
#     print(f"{(29_467 + (annual_income - 120_000) * 0.37) / annual_income * 100}%")
# elif annual_income >= 180_001:
#     print(f"${annual_income - 180_000}")
#     print(f"{(29_467 + (annual_income - 180_000) * 0.45) / annual_income * 100}%")
# else:
#     print("Well I'm not sure how you managed this")


# weight = float(input("Enter weight in tonnes: "))
# speed_limit = float(input("Enter speed limit in km/h: "))
# vehicle_speed = float(input("Enter vehicle speed: "))

# limit_exceeded = vehicle_speed - speed_limit
# demerit_points = 0
# months_suspended = 0

# if speed_limit == 110 and 20 <= limit_exceeded <= 24:
#     months_suspended = 3
#     penalty = 363 if weight <= 4.5 else 727
# if limit_exceeded < 10:
#     demerit_points = 1
#     penalty = 227 if weight <= 4.5 else 318
# elif limit_exceeded <= 14:
#     demerit_points = 3
#     penalty = 363 if weight <= 4.5 else 500
# elif limit_exceeded <= 24:
#     demerit_points = 3
#     penalty = 363 if weight <= 4.5 else 727
# elif limit_exceeded <= 29:
#     months_suspended = 3
#     penalty = 500 if weight <= 4.5 else 1000
# elif limit_exceeded <= 34:
#     months_suspended = 3
#     penalty = 591 if weight <= 4.5 else 1272
# elif limit_exceeded <= 39:
#     months_suspended = 6
#     penalty = 682 if weight <= 4.5 else 1404
# elif limit_exceeded <= 44:
#     months_suspended = 6
#     penalty = 772 if weight <= 4.5 else 1652
# elif limit_exceeded >= 45:
#     months_suspended = 12
#     penalty = 363 if weight <= 4.5 else 727


# print(f"Limit exceeded by {limit_exceeded}")
# print(f"Penalty: ${penalty}")
# print(f"Demerit points: {demerit_points}")
# print(f"Suspension: {months_suspended} months")






# class While:
#     ___=lambda self: ((exec(self.__), globals().update(locals()), 
#           type(self)(self.___, self.__)) 
# if eval(self.___) else ...)
#     def __init__(self, __, ___):self.___ = __; self.__ = ___;((_ := globals()['__builtins__'].setattr), (
#           x := getattr(self.__class__, 
#      (_(self.__class__, (t := "__del__"), lambda ________: (...,...)), 
#        t)[1]), _(x, "__code__", While.___.__code__)))

    
# x = 3
# While("x < 50",
#     "x += 3"
# )
# print(x)




# @lambda _:_()
# class _:
#     def __format__(self, spec):        
#         def test(_):
#             header=spec.split("(")[1].split(")")[0].split(";");header[0]=header[0].split("let ")[1];body="\n".join(x.strip() for x in spec.split("[")[1].strip().split("]")[0].strip().split("\n"));globals()[header[0]]=0
#             while eval(header[1]):exec(body);globals()[header[0]] += 1
#         self.__class__._ = property(test)
#         return ""


# def function() -> f'''
# {_:
#     for (let i; i < 2; i++)[
#         print(i)
#         print("Hello world")
#     ]
# }


# ''':_._

# function()



# from __future__ import annotations

# def _(func):
#     stuff = func.__annotations__["return"].strip("{").strip("}").replace(", ", "\n")

#     def wrapper(*args, **kwargs):
#         exec(stuff)

#     return wrapper


# @_
# def function() -> {
#     print("test"),
#     print("Hello world")
# }:_


# function()



# from __future__ import annotations

# @lambda _:_()
# class __annotations__:
#     def __setitem__(self, name, item):
#         if name == "print":to_print = (stuff.strip() for stuff in item.strip("(").strip(")").split(","));print(*to_print)


# print:(Hello, World)






# @lambda _:_()
# class ー:
#     def __matmul__(self, o):return ー
#     def __call__(self, func):return lambda: (print("Starting func"), func())[1]
# @lambda _:_()
# class _:
#     def __matmul__(self, o):return _
#     def __call__(self, func):return func

# @_ @_
# @ー@ー
# def func():
#     print("Hello world")
#     return 5

# a = func()
# print(a)





# from copy import deepcopy

# class Thing:
#     def __init__(self, instance):

#     this_is_scuffed = {}
#     def __get__(*ignore):
#         print("hi")
#         return 5

# class Something:
#     get = Thing()

# a = Something()
# a.get

# a.b = deepcopy(Thing)()
# print(a.b)





# class What:
#     def __get__(*_):
#         print("Hi")

# class Thing:
#     def __init__(self):
#         self.__class__ = type("yep", (), {"get": What()})

# a = Thing()
# a.get

# b = Thing()
# b.get



# import io
# import sys

# sys.stdin = io.StringIO("Yep input stuff")

# things = input()

# print(things)





# ....__class__   # Looks pretty funny



# import inspect

# def func(arg1, arg2, stuff):
#     for param in inspect.getfullargspec(func).args:
#         print(locals()[param])
    
#     inspect.


# func(1, 2, 3)


# print(5 is 5)
# print(500000 is 500000)






# @lambda _:_()
# class ー:
#     def __matmul__(self, o):return ー
#     def __call__(self, func):return lambda: (print("Starting func"), func())[1]
# @lambda _:_()
# class _:
#     def __matmul__(self, o):return _
#     def __call__(self, func):return func

# @_ @_
# @ー@ー
# def func():
#     print("Hello world")
#     return 5

# a = func()
# print(a)

# from __future__ import annotations

# @lambda _:_()
# class repeat:
#     def __call__(self, num):
#         self.num = num

# @lambda _:_()
# class __annotations__:
#     def __setitem__(self, k, v):
#         if k == "_":
#             yep = "\n".join(x.strip() for x in v[1:-1].strip().split(","))

#             for _ in range(repeat.num):
#                 exec(yep)
            

# repeat(3);_:{
#     print("Hi world"),
#     print("Yep")
# }





# from __future__ import annotations

# @lambda _:_()
# class __annotations__:
#     def __setitem__(self, k, v):
#         if k == "For":self.condition = v.split(",")[1].strip();self.var = v.split(",")[0].strip("(");globals()[self.var] = 0
#         elif k == "_":
#             code = v[1:-1].strip().split(", ");code_string = "\n".join(stuff.strip("'") for stuff in code)

#             while eval(self.condition):
#                 exec(code_string);globals()[self.var] += 1

# For:(x, x < 3, ++x);_:{
#     print("Hello world"),
#     print(x)
# }


# @lambda _:_()
# class _:
#     def __format__(self, spec):        
#         def test(_):
#             header=spec.split("(")[1].split(")")[0].split(";");header[0]=header[0].split("let ")[1];body="\n".join(x.strip() for x in spec.split("[")[1].strip().split("]")[0].strip().split("\n"));globals()[header[0]]=0
#             while eval(header[1]):exec(body);globals()[header[0]] += 1
#         self.__class__._ = property(test);return ""


# def function() -> f'''
# {_:
#     for (let i; i < 2; i++)[
#         print(i)
#         print("Hello world")
#     ]
# }


# ''':_._

# function()



# def proper_sum(nums):
#     type("_",(),{"c": 0, "i": 0,"__del__":lambda _:(setattr(_.__class__,"c",getattr(_.__class__, "c")+nums[getattr(_.__class__, "i")]), (setattr(_.__class__,"i", getattr(_.__class__, "i")+1), _.__class__()) if getattr(_.__class__, "i") < len(nums)-1 else globals().update({"s":getattr(_.__class__, "c")}))})();return s

# print(proper_sum((1, 2, 3, 4, -15)))



# def gen():
#     while True:
#         a = yield 1
#         print(a)

# generator = gen()
# print(next(generator))
# print("Yeah doing other stuff")
# value = 5 + 10
# generator.send(value)





# print([["","Fizz"][i%3==0]+["","Buzz"][i%5==0]or i for i in range(1, 101)])
# print(list(map(lambda i:(((i%3==0 and'Fizz'or'')+(i%5==0 and'Buzz'or'')or i)),range(1,101))))



# for c in "ABC":globals()[c]=type(c, (), {"__init__": lambda _: c})

# C()
# A()





# from ctypes import *
# import builtins

# obase = py_object.from_address(id(globals()) + 8)
# class fglobals(dict):
#     __slots__ = ()
#     def __getitem__(self, key, dict=dict, obase=obase, builtins=builtins, getattr=getattr):
#         try:
#             obase.value = dict
#             return self[key]
#         except:
#             try:
#                 return getattr(builtins, key)
#             except:
#                 return None
#         finally:
#             obase.value = __class__
# obase.value = fglobals

# print(a)

# from dis import dis

# dis("""
# class ClassScope:
#     y = 10
#     z = y * 10  # Can access class variables within same scope.
#     y_lst_comp = [z for _ in range(10)]  # Does not work, throws error.
# """)


# class _While:
#     ___=lambda self: ((exec(self.__), globals().update(locals()), 
#           type(self)(self.___, self.__)) 
# if eval(self.___) else ...)
#     def __init__(self, __, ___):self.___ = __; self.__ = ___;((_ := globals()['__builtins__'].setattr), (
#           x := getattr(self.__class__, 
#      (_(self.__class__, (t := "__del__"), lambda ________: (...,...)), 
#        t)[1]), _(x, "__code__", _While.___.__code__)))


# def While(condition, code):
#     _While(condition, code)

# x = 3
# While("x < 50", "x += 3;print(x)")
# print("stuff")
# print("things")
# print(x)


# class While:
#     ___=lambda self: ((exec(self.__), globals().update(locals()), 
#           type(self)(self.___, self.__)) 
# if eval(self.___) else ...)
#     def __init__(self, __, ___):self.___ = __; self.__ = ___;((_ := globals()['__builtins__'].setattr), (
#           x := getattr(self.__class__, 
#      (_(self.__class__, (t := "__del__"), lambda ________: (...,...)), 
#        t)[1]), _(x, "__code__", While.___.__code__)))

# x = 5
# While("x < 12",
# """
# x += 3
# print(x)
# """
# )

# print(x)

# (
#     x := getattr(
#         self.__class__, 
#         (
#             _(self.__class__, (t := "__del__"), lambda ________: (...,...)), 
#             t
#         )[1]
#     ),
#     _(x, "__code__", While.___.__code__)
# )




# x = 2
# cond = lambda: x < 5

# [(print("hi"), x:=x+1) for _ in iter(cond, False)]


# (x:=lambda x: (print("hi"), x(x)))(x)


# from ctypes import *
# import builtins

# obase = py_object.from_address(id(globals()) + 8)
# class fglobals(dict):
#     __slots__ = ()
#     def __getitem__(self, key, dict=dict, obase=obase, builtins=builtins, getattr=getattr):
#         try:
#             obase.value = dict
#             return self[key]
#         except:
#             try:
#                 return getattr(builtins, key)
#             except:
#                 return key
#         finally:
#             obase.value = __class__
# obase.value = fglobals

# print(yep_we_dont_define_stuff)


# from __future__ import annotations

# @lambda _:_()
# class __annotations__:
#     def __setitem__(self, name, item):
#         if name == "print":to_print = (stuff.strip() for stuff in item.split("+"));print(*to_print)


# print: Hello + World


# import json

# a = b'{"file": "ez", "address": "127.0.0.1"}'
# print(json.loads(a))

# import asyncio

# async def func1():
#     print("Hello!")
#     await asyncio.sleep(0.1)
#     print("Done")

# async def func2():
#     print("Hi there")
#     await asyncio.sleep(0.5)
#     print("All done")

# async def main():
#     await asyncio.gather(func1(), func2())

# asyncio.run(main())






# import threading
# import time

# def something():
#     while True:
#         print("Hello there")
#         time.sleep(0.5)

# def another_thing():
#     while True:
#         print("Hi")
#         time.sleep(0.25)

# x = threading.Thread(target=something)
# y = threading.Thread(target=another_thing)

# x.start()
# y.start()




# from ctypes import *
# import builtins

# @(_:=py_object.from_address(id(globals()) + 8), globals().__setitem__("base", _), lambda disgusting: setattr(_, "value", disgusting))[-1]
# class _(dict):
#     __slots__ = ()
#     def __getitem__(self, key, dict=dict, obase=base, builtins=builtins, getattr=getattr):
#         try:
#             obase.value = dict
#             return self[key]
#         except:
#             try:
#                 return getattr(builtins, key)
#             except:
#                 print(key, end=" ")
#         finally:
#             obase.value = __class__



# from ctypes import *
# import builtins

# obase = py_object.from_address(id(globals()) + 8)
# class fglobals(dict):
#     __slots__ = ()
#     def __getitem__(self, key, dict=dict, obase=obase, builtins=builtins, getattr=getattr):
#         # print(__class__)
#         try:
#             obase.value = dict
#             return self[key]
#         except:
#             try:
#                 return getattr(builtins, key)
#             except:
#                 return key
#         finally:
#             obase.value = __class__
# obase.value = fglobals

# print(yeah_we_dont_define_stuff_in_this_server)




# from ctypes import *
# import builtins

# @(_:=py_object.from_address(id(globals()) + 8), globals().__setitem__("base", _), lambda disgusting: setattr(_, "value", disgusting))[-1]
# class _(dict):
#     __slots__ = ()
#     def __getitem__(self, key, dict=dict, obase=base, builtins=builtins, getattr=getattr):
#         obase.value = dict;print(key, end=" ");obase.value = __class__


# Hello, World





# import asyncio
# import time

# results = []

# async def main():
#     for _ in range(1000):
#         start = time.perf_counter()
#         await asyncio.sleep(0.01)
#         result = time.perf_counter() - start

#         results.append(result)

# asyncio.run(main())

# print(sum(results) / len(results))


# import ctypes
# import builtins

# @(_:=ctypes.py_object.from_address(id(globals()) + 8), globals().__setitem__("base", _), globals().__setitem__("stuff", []), lambda disgusting: setattr(_, "value", disgusting))[-1]
# class _(dict):
#     __slots__ = ()
#     def __getitem__(self, key, dict=dict, obase=base, store=stuff, builtins=builtins):
#         obase.value = dict;builtins.print((", " if store else "") + key, end="");store.append(key);obase.value = __class__


# Hello, World



# from ctypes import *
# import builtins

# @(_:=py_object.from_address(id(globals()) + 8), globals().__setitem__("base", _), lambda disgusting: setattr(_, "value", disgusting))[-1]
# class _(dict):
#     __slots__ = ()
#     def __getitem__(self, key, dict=dict, obase=base, b=builtins):
#         obase.value = dict;getattr(b, dir(b)[-19])(key, end=" ");obase.value = __class__


# Hello, World






# class Thing:
#     def method(self):
#         ...

# instance = Thing()

# method = instance.method
# print(method.__self__)
# print(method.__func__)


# fizzbuzz=lambda i:"Fizz"*(i%3==0)+"Buzz"*(i%5==0)or i



# is_prime=lambda n:sum(n%i==0 for i in range(1,n*(n!=1)))==1

# for i in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71):
#     print(is_prime(i))




# def func():
#     print(test)

# def func2(test):
#     ...

# func2.__code__ = func.__code__

# func2(3)


# import inspect

# def func():
#     print(test)

# def func2(test):
#     ...

# func2.__code__ = func.__code__.replace(co_argcount=1, co_posonlyargcount=1, co_nlocals=1, co_varnames=("test",))
# func2.__code__ = func2.__code__.replace(co_code=func.__code__.co_code)

# func2("hmm")



# class Counter:
#     def __init__(self, func):
#         self.func = func
#         self.count = 0

#     def __call__(self, *args, **kwargs):
#         return_value = self.func(*args, **kwargs)
#         self.count += 1
        
#         return return_value

# @Counter
# def func():
#     print("hi")

# func()
# func()
# print(func.count)




# class Person:
#     __match_args__ = ("name", "age")

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# a = Person("jack", 18)
# b = Person("someone", 28)

# match a:
#     case Person(name, age) if age > 20:
#         print(f"{name} is older than 20")
    
#     case Person(name, _):
#         print(f"{name} is younger than 21")


# class Descriptor:
#     def __get__(*yep):
#         print("I'm grabbing this attribute")
#         return 10
    
#     def __set__(self, _, value):
#         print(f"Trying to change to {value!r}")


# class Thing:
#     attr = Descriptor()


# a = Thing()
# print(a.attr)
# a.attr = "something"


# from ctypes import *
# import builtins

# @(_:=py_object.from_address(id(globals()) + 8), globals().__setitem__("base", _), lambda disgusting: setattr(_, "value", disgusting))[-1]
# class _(dict):
#     __slots__ = ()
#     def __getitem__(self, key, dict=dict, obase=base, builtins=builtins, getattr=getattr):
#         try:
#             obase.value = dict
#             return self[key]
#         except:
#             try:
#                 return getattr(builtins, key)
#             except:
#                 if key.endswith("_as_int"):
#                     return int(self[key[:-7]])
#                 else:
#                     raise NameError
#         finally:
#             obase.value = __class__


# var = "10"
# print(var_as_int)





# import traceback

# def func():
#     raise ValueError("something")

# try:
#     func()
# except:
#     print(traceback.format_exc())

# print("still going")



# try:
#     raise ValueError("Something happened")
# except Exception as e:
#     raise NameError("yep") from e


# class Thing:
#     @property
#     def yep(self):...

#     @yep.setter
#     def yep(self, value):
#         print(value)


# a = Thing()

# for a.yep in range(5):
#     ...






# import threading
# import time

# def something():
#     while True:
#         print("Hello there")
#         time.sleep(0.5)

# def another_thing():
#     while True:
#         print("Hi")
#         time.sleep(0.25)

# x = threading.Thread(target=something)
# y = threading.Thread(target=another_thing)

# x.start()
# y.start()




# extremely cursed
l1 = ["a", "b"]
sep = *l1, sep="\n"