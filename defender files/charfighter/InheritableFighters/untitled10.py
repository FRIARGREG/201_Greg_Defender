# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:04:54 2018

@author: friar
"""

import datetime
first_flag = datetime.datetime.now()

while int(second_flag.second) - int(first_flag.second) < 25:
    second_flag = datetime.datetime.now()
    print(int(second_flag.minute), int(second_flag.second))
