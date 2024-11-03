#!/bin/python3

import math
import os
import random
import re
import sys


n = int(5)
validate_n = (n % 2) == 0
if validate_n and n > 20:
    print('Not Weird')
elif  validate_n and n >=6 and n <= 20:
    print('Weird')
elif validate_n and n >= 2 and n <=5:
    print('Not Weird')
else:
     print('Weird')