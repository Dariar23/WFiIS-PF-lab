class Punkt:

    def __init__(self , x=0, y=0):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val


def check_range(xmin=-100, xmax=100, ymin=-100, ymax=100):
    def decorator(fun):
        def wrapper(p1: Punkt , p2: Punkt):
            for p in (p1, p2):
                if not (xmin <= p.x <= xmax and ymin <= p.y <= ymax):
                    raise ValueError(f"punkt {p.x}, {p.y} nie lezy w zakresie")
            return fun(p1, p2)
        return wrapper
    return decorator


@check_range() 
def add_points(p1: Punkt, p2: Punkt):
    return Punkt(p1.x + p2.x, p1.y + p2.y)


@check_range()
def sub_points(p1: Punkt, p2: Punkt):
    return Punkt(p1.x - p2.x, p1.y - p2.y)


class CountDetector:
    calls = {}

    def __init__(self, fun):
        self.fun = fun
        CountDetector.calls[fun.__name__] = 0

    def __call__(self, *args, **kwargs):
        CountDetector.calls[self.fun.__name__] += 1
        return self.fun(*args, **kwargs)
    
    @staticmethod
    def counter():
        return CountDetector.calls


def prefix_filter(prefix):
    def decorator(cls):
        original_load = cls.load

        def new_load(self):
            original_load(self)
            self.lines = [line for line in self.lines if line.startswith(prefix)]

        cls.load = new_load
        return cls
    return decorator


@prefix_filter("INFO")
class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.lines = None

    def load(self):
        with open(self.filename, "r") as f:
            self.lines = f.readlines()

    def __iter__(self):
        return iter(self.lines or [])
    
    def __bool__(self):
        return bool(self.lines)


def capitalize_first(self):
    if self.lines:
        self.lines = [line.capitalize() for line in self.lines]


def count(self, mode="lines"):
    if not self.lines:
        return 0
    if mode == "lines":
        return len(self.lines)
    elif mode == "words":
        return sum(len(line.split()) for line in self.lines)
    elif mode == "chars":
        return sum(len(line) for line in self.lines)
    elif mode == "all":
        return {
            "lines": len(self.lines),
            "words": sum(len(line.split()) for line in self.lines),
            "chars": sum(len(line) for line in self.lines),
        }


setattr(FileReader, "capitalize_first", capitalize_first)
setattr(FileReader, "count", count)

if __name__ == "__main__":
    # Test Punkt + add/sub
    p1 = Punkt(10, 20)
    p2 = Punkt(5, -5)

    print("addition ", add_points(p1, p2).x, add_points(p1, p2).y)
    print("sub", sub_points(p1, p2).x, sub_points(p1, p2).y)

    # Test CountDetector
    @CountDetector
    def test():
        return "ok"

    test()
    test()
    print("CountDetector:", CountDetector.counter())

    # Test FileReader
    reader = FileReader("test.txt")
    reader.load()

    print("bool:", bool(reader))

    print("lines (raw):")
    for line in reader:
        print(line.strip())

    reader.capitalize_first()
    print("lines (capitalized):")
    for line in reader:
        print(line.strip())

    print("count all:", reader.count("all"))
