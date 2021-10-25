

def a():
    t = [1]
    b(t)
    print(t)

def b(t):
    t.append(10)
    print(t)

if __name__ == '__main__':
    a()