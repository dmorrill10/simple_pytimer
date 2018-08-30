# Simple Pytimer

Simple timer classes to record and log execution times of Python code in a pythonic way.

## Usage

```python
timer = Timer('long running process')
with timer:
  # do computations...
print(timer)
```

## Example

```python
timer = Timer('adding up a bunch of the numbers')
with timer:
  s = sum(range(10000000))
print(timer)  # "adding up a bunch of the numbers" block took 287.7 ms
```
