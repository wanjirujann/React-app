Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170118] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=10
>>> a
10
>>> school="akirachix"
>>> school
'akirachix'
>>> school.capitalize
<built-in method capitalize of str object at 0x7f903382aaf0>
>>> school.capitalize()
'Akirachix'
>>> school
'akirachix'
>>> b=school.capitalize
>>> b
<built-in method capitalize of str object at 0x7f903382aaf0>
>>> b=school.capitalize()
>>> b
'Akirachix'
>>> school.upper()
'AKIRACHIX'
>>> school.upper()
'AKIRACHIX'
>>> u=school.upper()
>>> u
'AKIRACHIX'
>>> u.lower()
'akirachix'
>>> s="i love akirachix"
>>> s.title()
'I Love Akirachix'
>>> school.endswith("x")
True
>>> school.endswith("z")
False
>>> school.startswith("a")
True
>>> school.startswith("e")
False
>>> startswith.akirachix("s")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    startswith.akirachix("s")
NameError: name 'startswith' is not defined
>>> school.count("x")
1
>>> school.count("o")
0
>>> school.count("a")
2
>>> school.count("i")
2
>>> school.count("I")
0
>>> "boy".upper()
'BOY'
>>> "school".upper
<built-in method upper of str object at 0x7f903383bea0>
>>> "school".upper()
'SCHOOL'
>>> girl.upper()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    girl.upper()
NameError: name 'girl' is not defined
>>> girl="Beyonce"
>>> girl
'Beyonce'
>>> girl.upper()
'BEYONCE'
>>> school="akirachix"
>>> balance=1000
>>> age="18 years"
>>> school
'akirachix'
>>> balance
1000
>>> age
'18 years'
>>> 
>>> school.islower()
True
>>> u.islower()
False
>>> school.isupper()
False
>>> u
'AKIRACHIX'
>>> u.isupper()
True
>>> school.isnumeric()
False
>>> balance.isnumeric()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    balance.isnumeric()
AttributeError: 'int' object has no attribute 'isnumeric'
>>> balance="1000"
>>> balance.isnumeric()
True
>>> age.isnumeric()
False
>>> age.isalpha()
False
>>> school.isalnum()
True
>>> balance.isalnum()
True
>>> age.isalnum()
False
>>> school.alphanum()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    school.alphanum()
AttributeError: 'str' object has no attribute 'alphanum'
>>> school.is()digit
SyntaxError: invalid syntax
>>> school.isdigit()
False
>>> balance.isdigit()
True
>>> age.digit()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    age.digit()
AttributeError: 'str' object has no attribute 'digit'
>>> age.isdigit()
False
>>> name="Jann"
>>> balance="4000000"
>>> "Helo {},your balance is {}".format(name,balance)
'Helo Jann,your balance is 4000000'
>>> name="Eric"
>>> balance="10000000"
>>> "Hello {}, your balance is {}".format(name,10000000)
'Hello Eric, your balance is 10000000'
>>> name="Eric"balance="10000000"
SyntaxError: invalid syntax
>>> name="Eric"
>>> balance="10000000"
>>> "Hello {name}, your balance is {balance}"
'Hello {name}, your balance is {balance}'
>>> f"Hello {name}, your balance is balance)"
SyntaxError: invalid syntax
>>> f"Hello{name}, your balance is{balance}"
SyntaxError: invalid syntax
>>> f"Hello {name}, your balance is {balance}"
SyntaxError: invalid syntax
>>> country="Kenya"
>>> population="49 million"
>>> "The population of {country} is {population}"
'The population of {country} is {population}'
>>> "The population of {} is {}".format(country,population)
'The population of Kenya is 49 million'
>>> country="Uganda"
>>> population="40 million"
>>> "The population of {} is {}".format(country,population)
'The population of Uganda is 40 million'
>>> school="AKIRACHIX"
>>> school[0]
'A'
>>> school[4]'A'
SyntaxError: invalid syntax
>>> school[4]
'A'
>>> school="AKIRACHIX"
>>> school[4]
'A'
>>> school[8]
'X'
>>> school[7]
'I'
>>> school[-4]
'C'
>>> school[-7]
'I'
>>> school[0:2]
'AK'
>>> school[0:6]
'AKIRAC'
>>> school[3:6]
'RAC'
>>> school[-3:-6]
''
>>> school[-8:-4]
'KIRA'
>>> school[3: ]
'RACHIX'
>>> school[-8: ]
'KIRACHIX'
>>> school[ :6]
'AKIRAC'
>>> school[ :-6]
'AKI'
>>> school[ :6]
'AKIRAC'
>>> len(school)
9
>>> len(Jann)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    len(Jann)
NameError: name 'Jann' is not defined
>>> name="Jann"
>>> len(Jann)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    len(Jann)
NameError: name 'Jann' is not defined
>>> name
'Jann'
>>> Jann=name
>>> Jann
'Jann'
>>> Jann="name"
>>> len(Jann)
4
>>> 
