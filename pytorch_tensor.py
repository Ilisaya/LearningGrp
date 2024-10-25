# -*- coding: utf-8 -*-
"""PyTorch_Tensor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pyhX8b0vI5snJumTIcrexSUA_usQVb9u

**Import** **Libraries**
"""

import numpy as np
import torch

arr1 = np.array([])
#arr1.dtype
type(arr1)

tens1 = torch.tensor([])
#tens1.dtype
type(tens1)

arr2 = np.array([1,2,3,4])
#print(arr2)
type(arr2)

tens2 = torch.from_numpy(arr2)
print(tens2)

tens2[1] = 10
print(tens2)

print(arr2)

arr3 = np.array([10,11,12,13])
tens3 = torch.tensor(arr3)
print(tens3)

tens3[0] = 200
print(tens3)

print(arr3)