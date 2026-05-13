def serve_chai():
    yield "Cup 1 : Masalaa chai"
    yield "Cup 2 : Gingeer chai"
    yield "Cup 3 : Elaichi chai"


# Generator yields one value at a time

stall = serve_chai()

# stall just has a reference not the actual values

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()

print(next(chai))
print(next(chai))
print(next(chai))