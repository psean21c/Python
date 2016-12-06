
### Requirement

* Save separated values into dictionary right after reading the line()
* Read next line until no line exists

input
```
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry
```
output
```
sam=99912222
Not found
harry=12299933
```

```python
n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
```
