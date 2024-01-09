# UoT - DSI - Machine Learning certificate - Module 3 - Building Software - Lesson 3 Exercise
This repository contains all files for Exercise 3 - the Building Software module (Jan 2024)

## Description

As part of the UoT - DSI - Machine Learning certificate program, the Building Software module lesson 3 includes exercises in:  
* Python Packages

## Usage

in Google Colab, import the package with:
```
pip install git+https://github.com/germane4oss/lesson3_python_package
```

Once the package is imported, the code can be used like:

```
from package_code import package_code

package_code.calc_average(5,6)

package_code.calc_min(9,3)
```
## Testing

Use pytest to test the code with
```
pytest test_package_code.py
```

## Authors

German Silva  
gsilva2k5@gmail.com

## Version History

* 0.1 Initial version including all files related to exercise 3 - Python Packages


