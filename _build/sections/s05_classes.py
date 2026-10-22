SECTION = "05_classes"

EXERCISES = [
    dict(
        name="cls1",
        intro="""
        A class body defines methods; `__init__` sets up a new instance.
        Every method takes the instance as its first parameter, and by
        convention it is called `self`. It is explicit -- there is no
        implicit `this`, and no way to lose the binding.

        Attributes are created by assigning to self.something. There is no
        separate declaration step.
        """,
        hint="""
        In __init__, assign start to self.value.
        In increment, do self.value += by. It returns nothing.
        """,
        stub="""
        class Counter:
            def __init__(self, start: int = 0) -> None:
                ...

            def increment(self, by: int = 1) -> None:
                ...
        """,
        solution="""
        class Counter:
            def __init__(self, start: int = 0) -> None:
                self.value = start

            def increment(self, by: int = 1) -> None:
                self.value += by
        """,
        checks="""
        c = Counter()
        eq(c.value, 0)
        c.increment()
        eq(c.value, 1)
        c.increment(10)
        eq(c.value, 11)

        other = Counter(100)
        eq(other.value, 100)
        eq(c.value, 11, "instances do not share state")
        """,
    ),
    dict(
        name="cls2",
        intro="""
        Two string conversions, for two audiences.

          __repr__  for you: unambiguous, ideally valid Python. repr() and
                    the REPL and the contents of a printed list use it.
          __str__   for users: readable. str(), print() and f-strings use it,
                    and fall back to __repr__ when __str__ is not defined.

        Always write __repr__. A debugging session against
        <__main__.Point object at 0x7f...> is wasted time.
        """,
        hint="""
        __repr__ should return exactly: Point(x=1, y=2)
        __str__ should return exactly: (1, 2)
        Both are f-strings over self.x and self.y.
        """,
        stub="""
        class Point:
            def __init__(self, x: int, y: int) -> None:
                self.x = x
                self.y = y

            def __repr__(self) -> str:
                ...

            def __str__(self) -> str:
                ...
        """,
        solution="""
        class Point:
            def __init__(self, x: int, y: int) -> None:
                self.x = x
                self.y = y

            def __repr__(self) -> str:
                return f"Point(x={self.x}, y={self.y})"

            def __str__(self) -> str:
                return f"({self.x}, {self.y})"
        """,
        checks="""
        p = Point(1, 2)
        eq(repr(p), "Point(x=1, y=2)")
        eq(str(p), "(1, 2)")
        eq(f"{p}", "(1, 2)", "f-strings use __str__")
        eq(f"{p!r}", "Point(x=1, y=2)", "!r forces __repr__")
        eq(str([p]), "[Point(x=1, y=2)]", "containers show their items with repr")
        """,
    ),
    dict(
        name="cls3",
        intro="""
        By default two objects are equal only if they are the same object.
        Define __eq__ to compare by value instead.

        The moment you define __eq__, Python sets __hash__ to None and your
        class becomes unusable in a set or as a dict key. You must define
        __hash__ too, and the contract is: equal objects MUST have equal
        hashes. Hash whatever you compared.

        Returning NotImplemented (not False) for an unknown type lets Python
        try the other object's __eq__ before giving up.
        """,
        hint="""
        __eq__: if not isinstance(other, Tag), return NotImplemented.
        Otherwise compare self.name to other.name.
        __hash__: return hash(self.name) -- the same field you compared.
        """,
        stub="""
        class Tag:
            def __init__(self, name: str) -> None:
                self.name = name.lower()

            def __eq__(self, other: object) -> bool:
                ...

            def __hash__(self) -> int:
                ...
        """,
        solution="""
        class Tag:
            def __init__(self, name: str) -> None:
                self.name = name.lower()

            def __eq__(self, other: object) -> bool:
                if not isinstance(other, Tag):
                    return NotImplemented
                return self.name == other.name

            def __hash__(self) -> int:
                return hash(self.name)
        """,
        checks="""
        ok(Tag("Python") == Tag("python"), "compared by value, case-insensitively")
        not_ok(Tag("a") == Tag("b"))
        not_ok(Tag("a") == "a", "a Tag is not equal to a plain string")
        eq(hash(Tag("Python")), hash(Tag("python")), "equal objects must hash equal")
        eq(len({Tag("A"), Tag("a"), Tag("b")}), 2, "sets rely on both methods")
        eq({Tag("x"): 1}[Tag("X")], 1, "and so do dict keys")
        """,
    ),
    dict(
        name="cls4",
        intro="""
        @property turns a method into an attribute that is computed on
        access. This is why Python code has almost no getFoo()/setFoo()
        methods: you start with a plain attribute, and if it later needs
        logic you turn it into a property without changing a single caller.

        A matching @name.setter makes it assignable.
        """,
        hint="""
        fahrenheit getter: self._celsius * 9 / 5 + 32
        The setter is decorated @fahrenheit.setter, takes (self, value), and
        assigns (value - 32) * 5 / 9 to self._celsius.
        """,
        stub="""
        class Temperature:
            def __init__(self, celsius: float) -> None:
                self._celsius = celsius

            @property
            def fahrenheit(self) -> float:
                ...

            # TODO: add the setter, so `t.fahrenheit = 212` works.
        """,
        solution="""
        class Temperature:
            def __init__(self, celsius: float) -> None:
                self._celsius = celsius

            @property
            def fahrenheit(self) -> float:
                return self._celsius * 9 / 5 + 32

            @fahrenheit.setter
            def fahrenheit(self, value: float) -> None:
                self._celsius = (value - 32) * 5 / 9
        """,
        checks="""
        t = Temperature(100)
        eq(t.fahrenheit, 212.0, "accessed as an attribute, with no parentheses")

        t.fahrenheit = 32
        eq(t._celsius, 0.0, "the setter converts back")

        frozen = Temperature(0)
        eq(frozen.fahrenheit, 32.0)
        """,
    ),
    dict(
        name="cls5",
        intro="""
        Two more decorators for methods:

          @classmethod   receives the class as `cls`. The standard way to
                         write alternative constructors, and using cls(...)
                         rather than the class name means subclasses get the
                         right type back.
          @staticmethod  receives nothing special. A plain function that
                         lives in the class's namespace because it belongs
                         there conceptually.
        """,
        hint="""
        from_minutes is a @classmethod taking (cls, minutes) and returning
        cls(minutes * 60).
        is_valid is a @staticmethod taking just (seconds).
        """,
        stub="""
        class Duration:
            def __init__(self, seconds: int) -> None:
                self.seconds = seconds

            # TODO: an alternative constructor Duration.from_minutes(3)

            # TODO: a validator Duration.is_valid(-1) -> False
        """,
        solution="""
        class Duration:
            def __init__(self, seconds: int) -> None:
                self.seconds = seconds

            @classmethod
            def from_minutes(cls, minutes: int) -> "Duration":
                return cls(minutes * 60)

            @staticmethod
            def is_valid(seconds: int) -> bool:
                return seconds >= 0
        """,
        checks="""
        eq(Duration.from_minutes(3).seconds, 180)
        eq(Duration.from_minutes(0).seconds, 0)
        ok(Duration.is_valid(0))
        not_ok(Duration.is_valid(-1))
        ok(Duration.is_valid(5))

        # Because from_minutes builds with cls(...), subclasses get their own type.
        class Timeout(Duration):
            pass

        eq(type(Timeout.from_minutes(1)), Timeout)
        """,
    ),
    dict(
        name="cls6",
        intro="""
        @dataclass writes __init__, __repr__ and __eq__ for you from the
        annotated fields. It is the default choice for anything that mostly
        holds data.

          frozen=True   immutable -- assignment raises, and you get __hash__
          slots=True    no per-instance __dict__: less memory, faster
                        attribute access, and typos raise instead of quietly
                        creating a new attribute

        Fields with defaults must come after fields without.
        """,
        hint="""
        Decorate with @dataclass(frozen=True, slots=True) and declare the
        two fields as annotations, with port defaulting to 8080. You write
        no methods at all.
        """,
        stub="""
        from dataclasses import dataclass


        # TODO: make this a frozen, slotted dataclass with fields
        #       host: str  and  port: int = 8080
        class Config:
            ...
        """,
        solution="""
        from dataclasses import dataclass


        @dataclass(frozen=True, slots=True)
        class Config:
            host: str
            port: int = 8080
        """,
        checks="""
        c = Config("db.example.com")
        eq(c.host, "db.example.com")
        eq(c.port, 8080)
        eq(Config("a", 1), Config("a", 1), "__eq__ compares field by field")
        not_ok(Config("a", 1) == Config("a", 2))
        eq(repr(Config("a", 1)), "Config(host='a', port=1)")
        ok(hash(Config("a", 1)) == hash(Config("a", 1)), "frozen dataclasses hash")
        raises(Exception, lambda: setattr(c, "host", "other"), "frozen means frozen")
        not_ok(hasattr(c, "__dict__"), "slots=True removes the per-instance dict")
        """,
    ),
    dict(
        name="cls7",
        intro="""
        Inheritance, and super().

        super().__init__(...) calls the parent's initialiser. Forgetting it
        is the usual cause of "my attribute does not exist" in a subclass.

        Note that Shape.describe calls self.area(), and gets the subclass's
        version. That is ordinary dynamic dispatch, and it is most of what
        you actually need inheritance for.
        """,
        hint="""
        Rectangle.__init__ takes (self, width, height), calls
        super().__init__("rectangle"), then stores width and height.
        area returns self.width * self.height.
        """,
        stub="""
        class Shape:
            def __init__(self, name: str) -> None:
                self.name = name

            def area(self) -> float:
                raise NotImplementedError

            def describe(self) -> str:
                return f"{self.name} with area {self.area()}"


        class Rectangle(Shape):
            # TODO: __init__(self, width, height) -- remember super()
            # TODO: area()
            ...
        """,
        solution="""
        class Shape:
            def __init__(self, name: str) -> None:
                self.name = name

            def area(self) -> float:
                raise NotImplementedError

            def describe(self) -> str:
                return f"{self.name} with area {self.area()}"


        class Rectangle(Shape):
            def __init__(self, width: float, height: float) -> None:
                super().__init__("rectangle")
                self.width = width
                self.height = height

            def area(self) -> float:
                return self.width * self.height
        """,
        checks="""
        r = Rectangle(3, 4)
        eq(r.area(), 12)
        eq(r.name, "rectangle", "did you call super().__init__?")
        eq(r.describe(), "rectangle with area 12", "the parent method calls your area()")
        ok(isinstance(r, Shape))
        raises(NotImplementedError, lambda: Shape("blob").area())
        """,
    ),
]
