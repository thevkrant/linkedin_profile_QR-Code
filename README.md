# 
<div align="center">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/156916372-d8c1bbdd-5fe9-40d1-a250-5a1d4d454832.png">
</div>

<h1 align="center">Linkedin profile QR code using Python</h1>

### Python tip:
There is a simple way to create a code countdown timer using the perf_counter() class from the time module. I wrote a function that demonstrates how you can use it as a performance counter for your code. 
* perf_counter() returns how long it takes to create a list from a range using a for loop.

### Prerequisites
`Python 3`

### Source Code
```python3
import time

def timer():
    list1 = []
    start = time.perf_counter()
    for i in range(10000000):
        list1.append(i**2)
    end = time.perf_counter()
    return f'Code Run time is {end - start:0.2f} seconds'

if __name__ == "__main__":
    print(timer())
```

## *Author Name*
[Vikrant](https://github.com/vikrant-v28)
