from re import X


def square(l):
    x=0
    while x < l:
        yield x*x
        yield x*x*x
        x+=1

a = square(5)

print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
print(next(a),next(a))
