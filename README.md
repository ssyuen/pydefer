# pydefer

`pydefer` aims to emulate the same experience you get from using Golang's `defer` keyword. `pydefer` allows you to execute a function around a given wrapped function after the wrapped function has executed.

## Installing

`$ pip install pydefer`

or

`$ pipenv install pydefer`

## Usage

Here's a basic example of using defer to print the sequence of numbers between [6,10] after `print_sequence` is called (which calls the sequence of numbers between [1,5]).

```python
>>> from pydefer.defer import defer
>>>
>>> @defer(print,6,7,8,9,10)
... def print_sequence():
...     print(1,2,3,4,5)
...
>>> print_seqeuence()
1 2 3 4 5
6 7 8 9 10
```

Some more complex use cases of `pydefer` is to be able to close files and not have to worry about closing them yourself in the actual function. Another use case is possibly session management for a web app after a user visits different routes.

Here's the aforementioned more complex example of deferring of closing a file.

```python
from python.defer import defer

@defer(open('employee_data.txt','r').close)
def update_employee(e_id):
    f = open('employee_data.txt','w')
    # DO STUFF TO FILE

    f.write(e_id.salary)

    # DO MORE STUFF LATER ON
```

In the above example, you do not need to manage the file anywhere inside the function as the `defer` function wrapper will close that file for you after the `update_employee` function has finished.