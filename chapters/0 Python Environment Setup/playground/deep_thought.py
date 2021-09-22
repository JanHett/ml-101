import numpy as np

numbers = np.array([-12.7, 42, 31, -47, 3.141, 6.282], dtype=np.float32)

the_answer = max(numbers)

print(f"The answer is {the_answer}")

def max(arr):
    current_max = np.finfo(arr.dtype).min

    for e in arr:
        print(e)
        if current_max < e:
            current_max = e

    return current_max
