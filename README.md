# Ptick Ptock

[![Tests](https://github.com/ADorigi/ptick-ptock/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/ADorigi/ptick-ptock/actions/workflows/tests.yaml)  

## Summary

![Ptick-Ptock](https://media1.giphy.com/media/Qz4RaxcOh4qndWOG5N/giphy.gif)

A simple stopwatch imitating tool inspired by tic toc in MATLAB 

Have you been a victim of scrutinous time calculation in python?  
The constant time subtractions and manipulations.....? I know.  
This library masks those steps for you; "abstracts it" as you would term it.  

Link to PyPi [Ptick-Ptock](https://pypi.org/project/ptick-ptock/)

<img src="https://i.ibb.co/hgpyfk5/honest-work.jpg" alt="HonestWork" width="400"/>

## Project Timeline

<img src="https://i.ibb.co/cgM9Z3T/Timeline.jpg" alt="Timeline" width="1000"/>  

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ptick-ptock.

```bash
pip install ptick-ptock
```
## Usage

```python
from ptick_ptock import ptick_ptock

# returns ptick-ptock object
object = ptick_ptock()

#starts time calculation
object.ptick()

#returns elapsed time
object.datetime_ptock()

#prints elapsed time
object.print_ptock()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)



\* P.S. : The timeline was a joke 🤓 \*
