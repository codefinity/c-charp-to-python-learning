from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent, indent


@dataclass(frozen=True)
class Topic:
    number: int
    group: str
    slug: str
    title: str
    summary: str
    simple_code: str
    advanced_code: str
    expected_output: list[str]
    further_study: str | None = None


TOPICS: list[Topic] = [
    Topic(
        1,
        "01_setup_and_runtime",
        "python_project_setup_with_uv",
        "Python project setup with uv",
        "Use `uv` as the Python equivalent of `dotnet new`, `dotnet restore`, and `dotnet run` in one fast workflow.",
        """
commands = ["uv init", "uv sync", "uv run src/csharp_to_python_learning/concepts/.../topic_01_python_project_setup_with_uv.py"]
for command in commands:
    print(command)
""",
        """
tooling = {
    "dependencies": "uv add requests",
    "dev_dependencies": "uv add --dev pytest ruff mypy",
    "lock_refresh": "uv sync --upgrade",
}
print(", ".join(f"{k} => {v}" for k, v in tooling.items()))
""",
        ["uv init", "dependencies => uv add requests"],
    ),
    Topic(
        2,
        "01_setup_and_runtime",
        "python_execution_model",
        "Python execution model",
        "Python executes modules top-to-bottom and binds names at runtime, then runs guarded script code under `if __name__ == '__main__'`.",
        """
module_name = __name__
print(f"module name: {module_name}")
print("main block runs only when executed as a script")
""",
        """
source = "value = 40 + 2\\nprint('compiled value:', value)"
code_object = compile(source, "<dynamic>", "exec")
exec(code_object)
""",
        ["module name:", "compiled value: 42"],
    ),
    Topic(
        3,
        "02_data_and_flow",
        "variables_names_references_and_mutability",
        "Variables, names, references, and mutability",
        "Python names point to objects; assignment rebinds names, while mutating a shared object affects all aliases.",
        """
a = [1, 2]
b = a
b.append(3)
print(a, b)
""",
        """
original = {"region": "APAC", "skills": ["C#", "SQL"]}
copy_for_edit = {**original, "skills": [*original["skills"], "Python"]}
print(original)
print(copy_for_edit)
""",
        ["[1, 2, 3] [1, 2, 3]", "{'region': 'APAC', 'skills': ['C#', 'SQL']}"],
    ),
    Topic(
        4,
        "02_data_and_flow",
        "primitive_types",
        "Primitive types",
        "Python has familiar scalar types (`int`, `float`, `bool`, `str`) plus precision types like `Decimal`.",
        """
from decimal import Decimal
amount = Decimal("19.99") * 3
print(type(amount).__name__, amount)
""",
        """
from fractions import Fraction
ratio = Fraction(1, 3) + Fraction(1, 6)
print("fraction:", ratio, "as float:", float(ratio))
""",
        ["Decimal 59.97", "fraction: 1/2 as float: 0.5"],
    ),
    Topic(
        5,
        "02_data_and_flow",
        "collections",
        "Collections: list, tuple, dict, set, frozenset",
        "Python collection types have different mutability and lookup guarantees; choosing the right one matters in production code.",
        """
items = ["build", "test", "deploy"]
mapping = {"build": 1, "test": 2}
unique = set(items)
print(items[0], mapping["test"], "deploy" in unique)
""",
        """
permissions = frozenset({"read", "write"})
profile = ("nikhil", "senior", permissions)
print(profile[0], sorted(profile[2]))
""",
        ["build 2 True", "nikhil ['read', 'write']"],
    ),
    Topic(
        6,
        "02_data_and_flow",
        "slicing_and_unpacking",
        "Slicing and unpacking",
        "Python slicing and unpacking replace many verbose loop/indexing patterns common in C#.",
        """
numbers = [10, 20, 30, 40, 50]
head, *middle, tail = numbers
print(head, middle, tail)
""",
        """
from itertools import islice
stream = (n * n for n in range(100))
window = list(islice(stream, 5, 10))
print(window)
""",
        ["10 [20, 30, 40] 50", "[25, 36, 49, 64, 81]"],
    ),
    Topic(
        7,
        "02_data_and_flow",
        "control_flow",
        "Control flow",
        "Python control flow favors readability with indentation and expressive constructs like `for ... else`.",
        """
for n in range(3):
    if n == 1:
        continue
    print("value", n)
""",
        """
target = 7
for n in [1, 3, 5]:
    if n == target:
        print("found")
        break
else:
    print("not found")
""",
        ["value 0", "not found"],
    ),
    Topic(
        8,
        "03_functions_and_functional_tools",
        "functions",
        "Functions",
        "Functions are first-class objects in Python, so you can pass and return them directly.",
        """
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))
""",
        """
def pipeline(value: int, *steps):
    result = value
    for step in steps:
        result = step(result)
    return result

print(pipeline(5, lambda x: x + 1, lambda x: x * 3))
""",
        ["5", "18"],
    ),
    Topic(
        9,
        "03_functions_and_functional_tools",
        "default_and_keyword_only_arguments",
        "Default arguments and keyword-only arguments",
        "Keyword-only arguments let you model explicit APIs like named optional parameters in C#.",
        """
def greet(name: str, *, excited: bool = False) -> str:
    return f"Hello {name}{'!' if excited else '.'}"

print(greet("Nikhil", excited=True))
""",
        """
def append_item(value: int, bucket: list[int] | None = None) -> list[int]:
    bucket = bucket or []
    bucket.append(value)
    return bucket

print(append_item(1), append_item(2))
""",
        ["Hello Nikhil!", "[1] [2]"],
    ),
    Topic(
        10,
        "03_functions_and_functional_tools",
        "lambdas",
        "Lambdas",
        "Python lambdas are small expression-only functions, best used inline for short transformations.",
        """
teams = ["platform", "api", "ml"]
print(sorted(teams, key=lambda t: len(t)))
""",
        """
records = [{"name": "A", "score": 92}, {"name": "B", "score": 81}]
top = max(records, key=lambda r: (r["score"], r["name"]))
print(top["name"], top["score"])
""",
        ["['ml', 'api', 'platform']", "A 92"],
    ),
    Topic(
        11,
        "03_functions_and_functional_tools",
        "closures",
        "Closures",
        "Closures capture surrounding state, similar to C# captured variables in local functions/lambdas.",
        """
def make_counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

counter = make_counter()
print(counter(), counter())
""",
        """
def memoized_square():
    cache: dict[int, int] = {}
    def run(value: int) -> int:
        if value not in cache:
            cache[value] = value * value
        return cache[value]
    return run

square = memoized_square()
print(square(12), square(12))
""",
        ["1 2", "144 144"],
    ),
    Topic(
        12,
        "03_functions_and_functional_tools",
        "decorators",
        "Decorators",
        "Decorators provide AOP-style wrappers for logging, validation, authorization, and instrumentation.",
        """
from functools import wraps

def tagged(tag: str):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{tag}] start")
            return func(*args, **kwargs)
        return wrapper
    return deco

@tagged("demo")
def run():
    print("work")

run()
""",
        """
import time

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"elapsed={time.perf_counter() - start:.6f}")
        return result
    return wrapper

@timed
def compute():
    return sum(range(10_000))

print(compute())
""",
        ["[demo] start", "elapsed="],
    ),
    Topic(
        13,
        "03_functions_and_functional_tools",
        "comprehensions",
        "Comprehensions",
        "Comprehensions replace many LINQ `Select`/`Where` one-liners while staying explicit and Pythonic.",
        """
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers if n % 2 == 1]
print(squares)
""",
        """
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [cell for row in matrix for cell in row]
lookup = {value: value * value for value in flat}
print(flat, lookup[6])
""",
        ["[1, 9, 25]", "[1, 2, 3, 4, 5, 6] 36"],
    ),
    Topic(
        14,
        "03_functions_and_functional_tools",
        "iterators_and_generators",
        "Iterators and generators",
        "Generators are lazy and memory-efficient, which is crucial for streaming and ETL workloads.",
        """
def count_up(limit: int):
    current = 0
    while current < limit:
        yield current
        current += 1

print(list(count_up(4)))
""",
        """
def lines():
    yield "alpha"
    yield "beta"

def upper(values):
    for value in values:
        yield value.upper()

print(list(upper(lines())))
""",
        ["[0, 1, 2, 3]", "['ALPHA', 'BETA']"],
    ),
    Topic(
        15,
        "03_functions_and_functional_tools",
        "context_managers",
        "Context managers",
        "Context managers are deterministic resource guards; think `using` blocks generalized for any enter/exit behavior.",
        """
from contextlib import contextmanager

@contextmanager
def labelled(name: str):
    print(f"enter {name}")
    try:
        yield
    finally:
        print(f"exit {name}")

with labelled("demo"):
    print("inside")
""",
        """
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "note.txt"
    path.write_text("safe write", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
""",
        ["enter demo", "safe write"],
    ),
    Topic(
        16,
        "04_errors_and_modules",
        "exceptions",
        "Exceptions",
        "Python exceptions are value-carrying objects; use narrow catches and explicit re-raising for clarity.",
        """
try:
    int("not-a-number")
except ValueError as exc:
    print(type(exc).__name__)
finally:
    print("cleanup")
""",
        """
class DomainError(RuntimeError):
    pass

def parse_port(raw: str) -> int:
    try:
        value = int(raw)
    except ValueError as exc:
        raise DomainError("invalid port") from exc
    return value

try:
    parse_port("abc")
except DomainError as exc:
    print(exc)
""",
        ["ValueError", "invalid port"],
    ),
    Topic(
        17,
        "04_errors_and_modules",
        "modules_and_packages",
        "Modules and packages",
        "A Python package is a directory namespace, similar to assemblies + namespaces but resolved at runtime.",
        """
import json
payload = json.loads('{"status":"ok"}')
print(payload["status"])
""",
        """
import importlib
module = importlib.import_module("statistics")
print(module.mean([2, 4, 8]))
""",
        ["ok", "4.666"],
    ),
    Topic(
        18,
        "04_errors_and_modules",
        "imports_and_import_system",
        "Imports and import system",
        "Imports are executable statements with caching in `sys.modules`; import style affects startup and clarity.",
        """
import importlib.util
spec = importlib.util.find_spec("pathlib")
print(spec is not None)
""",
        """
def lazy_json():
    import json
    return json.dumps({"lazy": True})

print(lazy_json())
""",
        ["True", '{"lazy": true}'],
    ),
    Topic(
        19,
        "04_oop_and_modeling",
        "object_oriented_programming",
        "Object-oriented programming",
        "Python supports classic OOP, but with less ceremony and more runtime flexibility than C#.",
        """
class Account:
    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount: int) -> None:
        self.balance += amount

a = Account("Nikhil")
a.deposit(50)
print(a.owner, a.balance)
""",
        """
from dataclasses import dataclass

@dataclass
class TaxedAmount:
    net: float
    tax_rate: float

    @property
    def gross(self) -> float:
        return self.net * (1 + self.tax_rate)

print(round(TaxedAmount(100, 0.18).gross, 2))
""",
        ["Nikhil 50", "118.0"],
    ),
    Topic(
        20,
        "04_oop_and_modeling",
        "inheritance_and_composition",
        "Inheritance and composition",
        "Prefer composition when behavior should vary at runtime; use inheritance for stable hierarchies.",
        """
class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "woof"

print(Dog().speak())
""",
        """
class EmailSender:
    def send(self, message: str) -> str:
        return f"email:{message}"

class Notifier:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)

print(Notifier(EmailSender()).notify("deployed"))
""",
        ["woof", "email:deployed"],
    ),
    Topic(
        21,
        "04_oop_and_modeling",
        "properties",
        "Properties",
        "Properties keep attribute syntax while enforcing invariants, similar to C# `get`/`set` properties.",
        """
class Temperature:
    def __init__(self):
        self._celsius = 0.0

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

t = Temperature()
t.celsius = 22.5
print(t.celsius)
""",
        """
from functools import cached_property

class Report:
    def __init__(self, values: list[int]):
        self.values = values

    @cached_property
    def total(self) -> int:
        print("computing")
        return sum(self.values)

r = Report([1, 2, 3])
print(r.total, r.total)
""",
        ["22.5", "computing"],
    ),
    Topic(
        22,
        "04_oop_and_modeling",
        "dataclasses",
        "Dataclasses",
        "Dataclasses are concise record-like types with optional immutability, ordering, and slots.",
        """
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str

print(User(1, "Nikhil"))
""",
        """
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True, slots=True)
class Job:
    priority: int
    name: str
    tags: tuple[str, ...] = field(default_factory=tuple)

print(sorted([Job(2, "test"), Job(1, "build")])[0].name)
""",
        ["User(id=1, name='Nikhil')", "build"],
    ),
    Topic(
        23,
        "04_oop_and_modeling",
        "enums",
        "Enums",
        "Enums model closed sets of values and avoid stringly-typed logic in business rules.",
        """
from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    DONE = auto()

print(Status.DONE.name)
""",
        """
from enum import StrEnum

class Environment(StrEnum):
    DEV = "dev"
    PROD = "prod"

print(Environment.PROD.upper())
""",
        ["DONE", "PROD"],
    ),
    Topic(
        24,
        "05_typing_and_protocols",
        "protocols_and_structural_typing",
        "Protocols and structural typing",
        "Protocols model behavior contracts by shape (duck typing) instead of explicit inheritance.",
        """
from typing import Protocol

class Runner(Protocol):
    def run(self) -> str: ...

class Job:
    def run(self) -> str:
        return "ok"

def execute(target: Runner) -> str:
    return target.run()

print(execute(Job()))
""",
        """
from typing import Protocol, TypeVar

T = TypeVar("T")

class Serializer(Protocol[T]):
    def serialize(self, value: T) -> str: ...

class IntSerializer:
    def serialize(self, value: int) -> str:
        return str(value)

print(IntSerializer().serialize(42))
""",
        ["ok", "42"],
    ),
    Topic(
        25,
        "04_oop_and_modeling",
        "abstract_base_classes",
        "Abstract base classes",
        "ABCs define explicit contracts and can also provide reusable default behavior.",
        """
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, key: str) -> str: ...

class InMemoryRepository(Repository):
    def get(self, key: str) -> str:
        return f"value:{key}"

print(InMemoryRepository().get("x"))
""",
        """
from collections.abc import Iterable

class CsvLike:
    def __iter__(self):
        yield from ["a,b", "c,d"]

print(isinstance(CsvLike(), Iterable))
""",
        ["value:x", "True"],
    ),
    Topic(
        26,
        "05_typing_and_protocols",
        "type_hints",
        "Type hints",
        "Type hints improve readability and tooling without changing runtime behavior.",
        """
def normalize(names: list[str]) -> list[str]:
    return [name.strip().title() for name in names]

print(normalize(["  nikhil", "PRIYA "]))
""",
        """
from typing import TypedDict

class Config(TypedDict):
    retries: int
    timeout: float

config: Config = {"retries": 3, "timeout": 1.5}
print(config["retries"])
""",
        ["['Nikhil', 'Priya']", "3"],
    ),
    Topic(
        27,
        "05_typing_and_protocols",
        "generics",
        "Generics",
        "Python generics are type-checker friendly and map closely to C# generic classes and methods.",
        """
from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

print(Box[int](10).value)
""",
        """
from typing import TypeVar

U = TypeVar("U")

def first(items: list[U]) -> U:
    return items[0]

print(first(["a", "b", "c"]))
""",
        ["10", "a"],
    ),
    Topic(
        28,
        "06_advanced_language_runtime",
        "pattern_matching",
        "Pattern matching",
        "Structural pattern matching is Python's expressive branching feature for tuple/list/dict/object shapes.",
        """
def classify(value):
    match value:
        case 0:
            return "zero"
        case int() as n if n > 0:
            return "positive"
        case _:
            return "other"

print(classify(3))
""",
        """
from dataclasses import dataclass

@dataclass
class Event:
    kind: str
    size: int

def route(event: Event) -> str:
    match event:
        case Event(kind="upload", size=size) if size > 10:
            return "large-upload"
        case Event(kind="upload"):
            return "small-upload"
        case _:
            return "other"

print(route(Event("upload", 12)))
""",
        ["positive", "large-upload"],
    ),
    Topic(
        29,
        "06_advanced_language_runtime",
        "dunder_methods_and_data_model",
        "Dunder methods and Python data model",
        "Python objects participate in language syntax by implementing special (dunder) methods.",
        """
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

print(len(Team(['a', 'b', 'c'])))
""",
        """
class Vector:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))
""",
        ["3", "Vector(4, 6)"],
    ),
    Topic(
        30,
        "06_advanced_language_runtime",
        "descriptors",
        "Descriptors",
        "Descriptors power `property`, ORM fields, and validation by intercepting attribute access at class level.",
        """
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.private_name, value)

class Order:
    quantity = Positive()

o = Order()
o.quantity = 5
print(o.quantity)
""",
        """
class Tracked:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        value = obj.__dict__[self.name]
        print(f"read {self.name}={value}")
        return value

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

class Profile:
    level = Tracked()

p = Profile()
p.level = "senior"
print(p.level)
""",
        ["5", "read level=senior"],
    ),
    Topic(
        31,
        "06_advanced_language_runtime",
        "metaclasses",
        "Metaclasses",
        "Metaclasses customize class creation and are useful for registries and framework hooks.",
        """
class AddVersion(type):
    def __new__(mcls, name, bases, namespace):
        namespace["version"] = "1.0"
        return super().__new__(mcls, name, bases, namespace)

class Service(metaclass=AddVersion):
    pass

print(Service.version)
""",
        """
class RegistryMeta(type):
    registry: dict[str, type] = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "BasePlugin":
            mcls.registry[name] = cls
        return cls

class BasePlugin(metaclass=RegistryMeta):
    pass

class CsvPlugin(BasePlugin):
    pass

print(sorted(RegistryMeta.registry))
""",
        ["1.0", "['CsvPlugin']"],
    ),
    Topic(
        32,
        "07_concurrency_and_systems",
        "async_and_await",
        "Async and await",
        "Async functions represent suspendable workflows; use them for I/O concurrency, not CPU parallelism.",
        """
import asyncio

async def work():
    await asyncio.sleep(0)
    return "done"

print(asyncio.run(work()))
""",
        """
import asyncio

async def fetch(label: str, delay: float):
    await asyncio.sleep(delay)
    return label

async def main_async():
    result = await asyncio.gather(fetch("a", 0.01), fetch("b", 0.01))
    print(result)

asyncio.run(main_async())
""",
        ["done", "['a', 'b']"],
    ),
    Topic(
        33,
        "07_concurrency_and_systems",
        "asyncio_tasks_queues_cancellation_timeouts",
        "asyncio tasks, queues, cancellation, timeouts",
        "Production asyncio code needs task orchestration, cancellation handling, queues, and timeout guards.",
        """
import asyncio

async def producer(queue: asyncio.Queue[int]) -> None:
    for value in [1, 2, 3]:
        await queue.put(value)
    await queue.put(-1)

async def consumer(queue: asyncio.Queue[int]) -> None:
    while True:
        item = await queue.get()
        if item == -1:
            break
        print("consumed", item)

async def main_async():
    q: asyncio.Queue[int] = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

asyncio.run(main_async())
""",
        """
import asyncio

async def slow():
    await asyncio.sleep(0.2)
    return "slow"

async def main_async():
    try:
        await asyncio.wait_for(slow(), timeout=0.05)
    except TimeoutError:
        print("timed out")

asyncio.run(main_async())
""",
        ["consumed 1", "timed out"],
    ),
    Topic(
        34,
        "07_concurrency_and_systems",
        "threading",
        "Threading",
        "Threading works well for blocking I/O integration, protected with locks for shared mutable state.",
        """
import threading

counter = 0
lock = threading.Lock()

def inc():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

t1 = threading.Thread(target=inc)
t2 = threading.Thread(target=inc)
t1.start(); t2.start()
t1.join(); t2.join()
print(counter)
""",
        """
from concurrent.futures import ThreadPoolExecutor

def upper(text: str) -> str:
    return text.upper()

with ThreadPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(upper, ["a", "b", "c"])))
""",
        ["2000", "['A', 'B', 'C']"],
    ),
    Topic(
        35,
        "07_concurrency_and_systems",
        "multiprocessing",
        "Multiprocessing",
        "Use multiprocessing for CPU-bound work when threads are limited by interpreter-level contention.",
        """
from multiprocessing import Pool

def square(n: int) -> int:
    return n * n

if __name__ == "__main__":
    with Pool(2) as pool:
        print(pool.map(square, [1, 2, 3]))
""",
        """
from multiprocessing import Process, Queue

def worker(queue: Queue[int]) -> None:
    queue.put(42)

if __name__ == "__main__":
    queue: Queue[int] = Queue()
    process = Process(target=worker, args=(queue,))
    process.start()
    process.join()
    print(queue.get())
""",
        ["[1, 4, 9]", "42"],
    ),
    Topic(
        36,
        "07_concurrency_and_systems",
        "file_io",
        "File I/O",
        "Prefer explicit encodings and context managers for reliable file handling in production.",
        """
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "sample.txt"
    path.write_text("hello", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
""",
        """
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "data.log"
    with path.open("w", encoding="utf-8") as file:
        for index in range(3):
            file.write(f"line-{index}\\n")
    print(path.read_text(encoding="utf-8").strip().splitlines()[-1])
""",
        ["hello", "line-2"],
    ),
    Topic(
        37,
        "07_concurrency_and_systems",
        "pathlib",
        "pathlib",
        "`pathlib` gives object-oriented filesystem handling and replaces brittle string-based path logic.",
        """
from pathlib import Path
path = Path("src") / "csharp_to_python_learning"
print(path.parts[0], path.name)
""",
        """
from pathlib import Path
python_files = list(Path("src").rglob("*.py"))
print(len(python_files) > 0)
""",
        ["src csharp_to_python_learning", "True"],
    ),
    Topic(
        38,
        "07_concurrency_and_systems",
        "json_csv_toml",
        "JSON, CSV, TOML",
        "Python's standard library handles core data formats without external dependencies.",
        """
import json
payload = {"name": "nikhil", "years": 9}
text = json.dumps(payload)
print(json.loads(text)["name"])
""",
        """
import csv
import io
import tomllib

buffer = io.StringIO("name,score\\nA,90\\n")
rows = list(csv.DictReader(buffer))
parsed = tomllib.loads("tool = { name = 'uv' }")
print(rows[0]["score"], parsed["tool"]["name"])
""",
        ["nikhil", "90 uv"],
    ),
    Topic(
        39,
        "07_concurrency_and_systems",
        "logging",
        "Logging",
        "Structured, leveled logging is the production replacement for `print` debugging.",
        """
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logging.info("service started")
""",
        """
import logging

logger = logging.getLogger("billing")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(name)s %(levelname)s %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.WARNING)
logger.warning("quota low")
""",
        ["INFO service started", "billing WARNING quota low"],
    ),
    Topic(
        40,
        "08_quality_and_tooling",
        "testing_with_pytest",
        "Testing with pytest",
        "`pytest` favors simple functions and powerful assertions for fast test feedback.",
        """
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 2) == 4)
""",
        """
cases = [(2, 2, 4), (5, 7, 12)]
results = [left + right == expected for left, right, expected in cases]
print(all(results))
""",
        ["True", "True"],
    ),
    Topic(
        41,
        "08_quality_and_tooling",
        "mocking",
        "Mocking",
        "Use `unittest.mock` to isolate collaborators, side effects, and network boundaries.",
        """
from unittest.mock import Mock

client = Mock()
client.fetch.return_value = {"ok": True}
print(client.fetch()["ok"])
""",
        """
from unittest.mock import AsyncMock
import asyncio

async def main_async():
    sender = AsyncMock(return_value="sent")
    print(await sender())

asyncio.run(main_async())
""",
        ["True", "sent"],
    ),
    Topic(
        42,
        "08_quality_and_tooling",
        "debugging",
        "Debugging",
        "Combine debugger breakpoints, targeted logging, and tracebacks for efficient incident triage.",
        """
def divide(a: int, b: int) -> float:
    return a / b

try:
    divide(5, 0)
except ZeroDivisionError as exc:
    print(type(exc).__name__)
""",
        """
import traceback

def fail():
    raise RuntimeError("boom")

try:
    fail()
except RuntimeError:
    text = traceback.format_exc().splitlines()[-1]
    print(text)
""",
        ["ZeroDivisionError", "RuntimeError: boom"],
    ),
    Topic(
        43,
        "08_quality_and_tooling",
        "packaging",
        "Packaging",
        "Packaging turns source code into installable artifacts with metadata and entry points.",
        """
metadata = {
    "name": "csharp-to-python-learning",
    "entry_point": "python -m csharp_to_python_learning",
}
print(metadata["name"])
""",
        """
build_steps = ["uv sync", "uv run -m pytest", "uv build"]
print(" -> ".join(build_steps))
""",
        ["csharp-to-python-learning", "uv sync -> uv run -m pytest -> uv build"],
    ),
    Topic(
        44,
        "08_quality_and_tooling",
        "dependency_management",
        "Dependency management",
        "Pin dependencies and commit lock files for deterministic builds across machines and CI.",
        """
dependencies = ["httpx>=0.28", "pydantic>=2.8"]
print(len(dependencies))
""",
        """
groups = {"runtime": ["httpx"], "dev": ["pytest", "ruff", "mypy"]}
print(sorted(groups["dev"]))
""",
        ["2", "['mypy', 'pytest', 'ruff']"],
    ),
    Topic(
        45,
        "08_quality_and_tooling",
        "virtual_environments",
        "Virtual environments",
        "Virtual environments isolate interpreter and package state per project, similar to per-solution toolchains.",
        """
import sys
print(sys.prefix != sys.base_prefix)
""",
        """
import sys
venv_hint = ".venv" if sys.prefix != sys.base_prefix else "no-active-venv"
print(venv_hint)
""",
        ["False", "no-active-venv"],
    ),
    Topic(
        46,
        "08_quality_and_tooling",
        "linters_and_formatters",
        "Linters and formatters",
        "Ruff can handle linting and formatting quickly, replacing multiple separate tools in many projects.",
        """
snippet = "def add(a,b):\\n return a+b\\n"
print("use: uv run ruff check .")
print("use: uv run ruff format .")
""",
        """
quality_gate = {"lint": "ruff check", "format": "ruff format", "types": "mypy src"}
print(" | ".join(f"{k}:{v}" for k, v in quality_gate.items()))
""",
        ["use: uv run ruff check .", "lint:ruff check"],
    ),
    Topic(
        47,
        "08_quality_and_tooling",
        "performance_and_profiling",
        "Performance and profiling",
        "Measure before optimizing: combine `timeit`, `cProfile`, and algorithmic changes.",
        """
import timeit
duration = timeit.timeit("sum(range(1000))", number=1000)
print(duration > 0)
""",
        """
import cProfile
import pstats
import io

profile = cProfile.Profile()
profile.enable()
sum(range(20_000))
profile.disable()
stream = io.StringIO()
pstats.Stats(profile, stream=stream).sort_stats("cumulative").print_stats(1)
print("function calls" in stream.getvalue())
""",
        ["True", "True"],
    ),
    Topic(
        48,
        "09_memory_idioms_migration",
        "memory_management_and_gc",
        "Memory management and garbage collection",
        "CPython uses reference counting plus cyclic GC; lifecycle choices affect latency and memory pressure.",
        """
import gc
print(gc.isenabled())
""",
        """
import weakref

class Resource:
    pass

resource = Resource()
finalizer = weakref.finalize(resource, print, "resource finalized")
del resource
print(finalizer.alive in {True, False})
""",
        ["True", "True"],
    ),
    Topic(
        49,
        "09_memory_idioms_migration",
        "standard_library_overview",
        "Standard library overview",
        "The standard library covers many production needs: paths, JSON, CLI parsing, concurrency, testing, and more.",
        """
import statistics
print(round(statistics.mean([10, 20, 40]), 2))
""",
        """
from itertools import pairwise
pairs = list(pairwise([1, 2, 3, 4]))
print(pairs[-1])
""",
        ["23.33", "(3, 4)"],
    ),
    Topic(
        50,
        "09_memory_idioms_migration",
        "python_3_14_specific_features",
        "Python 3.14-specific features",
        "Python 3.14 adds deferred annotation behavior and stronger support for free-threaded execution.",
        """
from __future__ import annotations

def build_user(name: "str") -> "dict[str, str]":
    return {"name": name}

print(build_user("Nikhil")["name"])
""",
        """
import importlib.util

features = {
    "annotationlib": importlib.util.find_spec("annotationlib") is not None,
    "compression.zstd": importlib.util.find_spec("compression.zstd") is not None,
}
print(features)
""",
        ["Nikhil", "{'annotationlib':"],
        further_study="Read the official 3.14 What's New document to track point-release changes in 3.14.x.",
    ),
    Topic(
        51,
        "09_memory_idioms_migration",
        "python_idioms_vs_csharp_idioms",
        "Python idioms versus C# idioms",
        "Translate intent, not syntax: many C# patterns have shorter Pythonic forms.",
        """
numbers = [1, 2, 3, 4]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
""",
        """
records = [{"name": "a", "score": 10}, {"name": "b", "score": 7}]
best = max(records, key=lambda r: r["score"])
print(best["name"])
""",
        ["[2, 4]", "a"],
    ),
    Topic(
        52,
        "09_memory_idioms_migration",
        "common_csharp_to_python_migration_mistakes",
        "Common C# to Python migration mistakes",
        "Most migration bugs come from mutability assumptions, import-time side effects, and overusing class-heavy designs.",
        """
def append_bad(item, bucket=[]):  # noqa: B006 - intentional pitfall demo
    bucket.append(item)
    return bucket

print(append_bad(1), append_bad(2))
""",
        """
def append_good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item)
    return bucket

print(append_good(1), append_good(2))
""",
        ["[1, 2]", "[1] [2]"],
        further_study="Practice migrations by porting one real .NET utility at a time and measuring readability, testability, and performance.",
    ),
]


PYTHON_ONLY_FEATURES = [
    (
        "feature_01_duck_typing_and_protocols.py",
        "Duck typing and structural behavior",
        """
from typing import Protocol

class Writer(Protocol):
    def write(self, text: str) -> str: ...

class ConsoleWriter:
    def write(self, text: str) -> str:
        return text.upper()

def publish(writer: Writer) -> str:
    return writer.write("pythonic")

def main() -> None:
    print(publish(ConsoleWriter()))

if __name__ == "__main__":
    main()
""",
    ),
    (
        "feature_02_extended_unpacking.py",
        "Extended unpacking with starred targets",
        """
def main() -> None:
    first, *middle, last = [10, 20, 30, 40, 50]
    print(first, middle, last)

if __name__ == "__main__":
    main()
""",
    ),
    (
        "feature_03_generator_pipelines.py",
        "Lazy generator pipelines",
        """
def numbers():
    for value in range(5):
        yield value

def pipeline():
    return (value * value for value in numbers() if value % 2 == 0)

def main() -> None:
    print(list(pipeline()))

if __name__ == "__main__":
    main()
""",
    ),
    (
        "feature_04_contextlib_magic.py",
        "Reusable context managers with contextlib",
        """
from contextlib import contextmanager

@contextmanager
def banner(label: str):
    print(f"start:{label}")
    try:
        yield
    finally:
        print(f"end:{label}")

def main() -> None:
    with banner("deploy"):
        print("inside")

if __name__ == "__main__":
    main()
""",
    ),
    (
        "feature_05_descriptors.py",
        "Descriptors behind attribute access",
        """
class Lowercase:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value.lower()

class User:
    email = Lowercase()

def main() -> None:
    user = User()
    user.email = "TEAM@EXAMPLE.COM"
    print(user.email)

if __name__ == "__main__":
    main()
""",
    ),
    (
        "feature_06_pattern_matching.py",
        "Structural pattern matching guards",
        """
def describe(value):
    match value:
        case {"kind": "http", "status": status} if status >= 500:
            return "server-error"
        case {"kind": "http", "status": status}:
            return f"http-{status}"
        case _:
            return "unknown"

def main() -> None:
    print(describe({"kind": "http", "status": 503}))

if __name__ == "__main__":
    main()
""",
    ),
    (
        "feature_07_metaclass_registry.py",
        "Class registration via metaclass",
        """
class RegistryMeta(type):
    plugins: dict[str, type] = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        if name != "Plugin":
            mcls.plugins[name] = cls
        return cls

class Plugin(metaclass=RegistryMeta):
    pass

class SlackPlugin(Plugin):
    pass

def main() -> None:
    print(sorted(RegistryMeta.plugins))

if __name__ == "__main__":
    main()
""",
    ),
]


CAPSTONE_CODE = dedent(
    """
from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Protocol


logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
logger = logging.getLogger("capstone")


@dataclass(frozen=True, slots=True)
class Event:
    source: str
    payload: dict[str, int]


class Sink(Protocol):
    async def write(self, event: Event) -> None: ...


class InMemorySink:
    def __init__(self) -> None:
        self.data: list[Event] = []

    async def write(self, event: Event) -> None:
        self.data.append(event)


async def producer(queue: asyncio.Queue[Event]) -> None:
    for index in range(5):
        await queue.put(Event(source="api", payload={"value": index}))
    await queue.put(Event(source="system", payload={"value": -1}))


async def consumer(queue: asyncio.Queue[Event], sink: Sink) -> None:
    while True:
        event = await queue.get()
        if event.payload["value"] == -1:
            break
        transformed = Event(source=event.source, payload={"value": event.payload["value"] * 10})
        await sink.write(transformed)


def summarize(events: list[Event]) -> dict[str, int]:
    return {
        "count": len(events),
        "total": sum(event.payload["value"] for event in events),
    }


async def main_async() -> None:
    queue: asyncio.Queue[Event] = asyncio.Queue()
    sink = InMemorySink()
    await asyncio.gather(producer(queue), consumer(queue, sink))
    summary = summarize(sink.data)
    logger.info("capstone summary: %s", summary)
    print(summary)


def main() -> None:
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
"""
).strip()


def to_module_path(file_path: Path) -> str:
    relative = file_path.relative_to(Path("src"))
    return ".".join(relative.with_suffix("").parts)


def csharp_expectation_for(topic: Topic) -> str:
    if "async" in topic.title.lower() or "thread" in topic.title.lower():
        return "C# developers usually expect `Task`-centric async flows, explicit cancellation tokens, and thread-pool awareness."
    if (
        "type" in topic.title.lower()
        or "generic" in topic.title.lower()
        or "protocol" in topic.title.lower()
    ):
        return "C# developers usually expect compile-time type contracts and explicit interfaces."
    if (
        "package" in topic.title.lower()
        or "dependency" in topic.title.lower()
        or "virtual environment" in topic.title.lower()
    ):
        return "C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps."
    if "testing" in topic.title.lower() or "mock" in topic.title.lower():
        return (
            "C# developers usually expect xUnit/NUnit style tests and dedicated mocking frameworks."
        )
    return "C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance."


def csharp_example_for(topic: Topic) -> str:
    title = topic.title.lower()
    if "async" in title:
        return dedent(
            """
            static async Task<string> FetchAsync()
            {
                await Task.Delay(10);
                return "done";
            }
            """
        ).strip()
    if "generics" in title:
        return dedent(
            """
            public sealed class Box<T>
            {
                public T Value { get; }
                public Box(T value) => Value = value;
            }
            """
        ).strip()
    if "decorator" in title:
        return dedent(
            """
            [LogExecution]
            public void Run() { Console.WriteLine("work"); }
            """
        ).strip()
    return dedent(
        """
        var values = new[] { 1, 2, 3 };
        Console.WriteLine(values.Length);
        """
    ).strip()


def python_equivalent_for(topic: Topic) -> str:
    return (
        f"Python approaches this concept with less ceremony: {topic.summary} "
        "You still keep production discipline through tests, typing, and tooling."
    )


def explanation_for(topic: Topic) -> str:
    return (
        f"{topic.summary} In practice, combine this with logging, tests, and type hints so the flexibility does not "
        "turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters."
    )


def mistakes_for(topic: Topic) -> list[str]:
    return [
        f"Assuming C# defaults apply directly in `{topic.title}` without checking Python runtime behavior.",
        "Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.",
    ]


def exercises_for(topic: Topic) -> list[str]:
    return [
        f"Rewrite one recent C# snippet in Python using this concept: `{topic.title}`.",
        "Add input validation, type hints, and one `pytest` test for the rewritten snippet.",
    ]


def render_topic(topic: Topic) -> str:
    expected = "\n".join(f"- {line}" for line in topic.expected_output)
    mistakes = "\n".join(
        f"1. {line}" if index == 0 else f"{index + 1}. {line}"
        for index, line in enumerate(mistakes_for(topic))
    )
    exercises = "\n".join(
        f"1. {line}" if index == 0 else f"{index + 1}. {line}"
        for index, line in enumerate(exercises_for(topic))
    )
    csharp_example = csharp_example_for(topic).strip()
    simple_code = dedent(topic.simple_code).strip()
    advanced_code = dedent(topic.advanced_code).strip()

    further_study = ""
    if topic.further_study:
        further_study = f"\n## Further Study\n{topic.further_study}\n"

    return (
        f'"""\n'
        f"# {topic.number}. {topic.title}\n\n"
        f"## What C# developers usually expect\n"
        f"{csharp_expectation_for(topic)}\n\n"
        f"## C# example\n"
        f"```csharp\n"
        f"{csharp_example}\n"
        f"```\n\n"
        f"## Python equivalent\n"
        f"{python_equivalent_for(topic)}\n\n"
        f"## Simple Python example\n"
        f"```python\n"
        f"{simple_code}\n"
        f"```\n\n"
        f"## Advanced Python example\n"
        f"```python\n"
        f"{advanced_code}\n"
        f"```\n\n"
        f"## Detailed explanation\n"
        f"{explanation_for(topic)}\n\n"
        f"## Common mistakes for C# developers\n"
        f"{mistakes}\n\n"
        f"## Exercises\n"
        f"{exercises}\n\n"
        f"## Expected output\n"
        f"{expected}\n"
        f"{further_study}"
        f'"""\n\n'
        "from __future__ import annotations\n\n\n"
        "def simple_python_example() -> None:\n"
        f"{indent(simple_code, '    ')}\n\n\n"
        "def advanced_python_example() -> None:\n"
        f"{indent(advanced_code, '    ')}\n\n\n"
        "def main() -> None:\n"
        f'    print("=== {topic.number}. {topic.title} ===")\n'
        '    print("-- Simple Python example --")\n'
        "    simple_python_example()\n"
        '    print("-- Advanced Python example --")\n'
        "    advanced_python_example()\n\n\n"
        'if __name__ == "__main__":\n'
        "    main()\n"
    )


def build_readme(concept_files: list[Path], python_only_files: list[Path]) -> str:
    toc_entries = [
        "- [Who This Repository Is For](#who-this-repository-is-for)",
        "- [Quick Start](#quick-start)",
        "- [How To Use uv In This Project](#how-to-use-uv-in-this-project)",
        "- [Tutorial Concepts](#tutorial-concepts)",
        "- [Python-Only Features](#python-only-features)",
        "- [C# Features With No Direct Python Equivalent](#c-features-with-no-direct-python-equivalent)",
        "- [Python Features With No Direct C# Equivalent](#python-features-with-no-direct-c-equivalent)",
        "- [1-Week Study Plan](#1-week-study-plan)",
        "- [Capstone Project](#capstone-project)",
        "- [Further Study](#further-study)",
    ]

    concept_lines = []
    for topic, file_path in zip(TOPICS, concept_files, strict=True):
        concept_lines.append(
            f"- **{topic.number}. {topic.title}**: {topic.summary} "
            f"Run: `uv run {file_path.as_posix()}` | File: [{file_path.as_posix()}]({file_path.as_posix()})"
        )

    python_only_lines = [
        f"- [{path.name}]({path.as_posix()}): runnable Python-only feature example."
        for path in python_only_files
    ]

    return (
        "# C# to Python: Advanced, Production-Ready Tutorial (Python 3.14.5 + uv)\n\n"
        "## Who This Repository Is For\n"
        "This repository is for experienced C#/.NET developers who already understand OOP, generics, LINQ, async/await, dependency injection, build tools, and testing.  \n"
        "The goal is to help you become an advanced Python developer who can ship production-grade code confidently.\n\n"
        "## Table of Contents\n"
        f"{'\n'.join(toc_entries)}\n\n"
        "## Quick Start\n"
        "```bash\n"
        "uv sync\n"
        "uv run src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py\n"
        "uv run -m pytest\n"
        "```\n\n"
        "## How To Use uv In This Project\n"
        "### `uv init`\n"
        "Initialize a new project (already done in this repository):\n"
        "```bash\n"
        "uv init --package --python 3.14.5\n"
        "```\n\n"
        "### `uv sync`\n"
        "Create/update `.venv` and install dependencies from `pyproject.toml` + `uv.lock`:\n"
        "```bash\n"
        "uv sync\n"
        "```\n\n"
        "### `uv run`\n"
        "Run a command inside the project environment:\n"
        "```bash\n"
        "uv run -m pytest\n"
        "uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py\n"
        "```\n\n"
        "### `uv add`\n"
        "Add a runtime dependency:\n"
        "```bash\n"
        "uv add httpx\n"
        "```\n"
        "Add a dev dependency:\n"
        "```bash\n"
        "uv add --dev pytest ruff mypy\n"
        "```\n\n"
        "### Running Tests\n"
        "```bash\n"
        "uv run -m pytest\n"
        "uv run -m pytest tests/test_concept_smoke.py -k asyncio\n"
        "```\n\n"
        "### Running Individual Examples\n"
        "Every concept is runnable directly:\n"
        "```bash\n"
        "uv run src/csharp_to_python_learning/concepts/09_memory_idioms_migration/topic_50_python_3_14_specific_features.py\n"
        "```\n\n"
        "## Tutorial Concepts\n"
        f"{'\n'.join(concept_lines)}\n\n"
        "## Python-Only Features\n"
        f"{'\n'.join(python_only_lines)}\n\n"
        "## C# Features With No Direct Python Equivalent\n"
        "- Reified generics at runtime with CLR metadata behavior.\n"
        "- Method overloading resolution by compile-time signature.\n"
        "- `ref`, `out`, and unsafe pointer patterns as first-class language features.\n"
        "- Attribute-driven compile-time/source-generator ecosystems.\n"
        "- Value types (`struct`) with stack semantics equivalent to .NET.\n\n"
        "## Python Features With No Direct C# Equivalent\n"
        "- Runtime monkey-patching of modules/classes/functions.\n"
        "- Descriptors as first-class attribute access primitives.\n"
        "- Structural pattern matching with heterogeneous shape patterns.\n"
        "- Context manager protocol (`with`) as a language-level resource hook.\n"
        "- Rich dunder protocol for integrating with core syntax at runtime.\n"
        "- Metaclass-driven class construction customization.\n"
        "- Extended iterable unpacking in assignments and function calls.\n\n"
        "## 1-Week Study Plan\n"
        "1. **Day 1**: Setup + execution model + names/references/mutability + primitive types.  \n"
        "   Practice: run topics 1-4 and rewrite one .NET utility script in Python.\n"
        "2. **Day 2**: Collections, slicing/unpacking, control flow, functions, defaults, lambdas.  \n"
        "   Practice: port a LINQ-heavy method to comprehensions and generator pipelines.\n"
        "3. **Day 3**: Closures, decorators, iterators/generators, context managers, exceptions.  \n"
        "   Practice: wrap an I/O workflow with proper context managers and exception boundaries.\n"
        "4. **Day 4**: Modules, imports, OOP, dataclasses, enums, properties, composition.  \n"
        "   Practice: model a domain object set with dataclasses and validation.\n"
        "5. **Day 5**: Typing, protocols, ABCs, generics, pattern matching, data model, descriptors/metaclasses.  \n"
        "   Practice: introduce protocols and static typing to an existing Python script.\n"
        "6. **Day 6**: Asyncio, threading, multiprocessing, file/path/data formats, logging.  \n"
        "   Practice: build a small concurrent ingestion script with structured logging.\n"
        "7. **Day 7**: Testing/mocking/debugging, packaging/tooling, profiling/memory, migration pitfalls, capstone.  \n"
        "   Practice: complete capstone and add tests + lint + type checks.\n\n"
        "## Capstone Project\n"
        "Run the capstone:\n"
        "```bash\n"
        "uv run src/csharp_to_python_learning/capstone/capstone_async_event_pipeline.py\n"
        "```\n"
        "Capstone combines:\n"
        "- dataclasses\n"
        "- protocols/typing\n"
        "- asyncio queues/tasks\n"
        "- transformation pipeline patterns\n"
        "- logging\n"
        "- deterministic summary output\n\n"
        "## Further Study\n"
        "- Official Python docs for 3.14 language/runtime updates.\n"
        "- `asyncio` internals and cancellation design patterns.\n"
        "- Advanced typing (`TypeVarTuple`, `ParamSpec`, plugin/tooling ecosystems).\n"
        "- Packaging and release automation for internal Python platforms.\n"
    )


def write_tests(root: Path) -> None:
    tests_dir = root / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)

    smoke = (
        dedent(
            """
        from __future__ import annotations

        import runpy
        from pathlib import Path


        PROJECT_ROOT = Path(__file__).resolve().parents[1]


        def run_script(script: Path) -> None:
            runpy.run_path(str(script), run_name="__main__")


        def test_selected_concepts_run_without_errors() -> None:
            scripts = [
                PROJECT_ROOT / "src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py",
                PROJECT_ROOT / "src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py",
                PROJECT_ROOT / "src/csharp_to_python_learning/concepts/06_advanced_language_runtime/topic_30_descriptors.py",
                PROJECT_ROOT / "src/csharp_to_python_learning/concepts/07_concurrency_and_systems/topic_33_asyncio_tasks_queues_cancellation_timeouts.py",
                PROJECT_ROOT / "src/csharp_to_python_learning/concepts/09_memory_idioms_migration/topic_50_python_3_14_specific_features.py",
            ]
            for script in scripts:
                run_script(script)


        def test_python_only_examples_run_without_errors() -> None:
            feature_dir = PROJECT_ROOT / "src/csharp_to_python_learning/python_only_features"
            targets = sorted(feature_dir.glob("feature_*.py"))
            for script in targets:
                run_script(script)


        def test_capstone_pipeline_runs_without_errors() -> None:
            script = PROJECT_ROOT / "src/csharp_to_python_learning/capstone/capstone_async_event_pipeline.py"
            run_script(script)
        """
        ).strip()
        + "\n"
    )
    (tests_dir / "test_concept_smoke.py").write_text(smoke, encoding="utf-8")


def write_package_files(src: Path) -> None:
    init_text = (
        dedent(
            """
        from __future__ import annotations


        def main() -> None:
            print("Run README.md for the full tutorial index and commands.")
        """
        ).strip()
        + "\n"
    )
    (src / "__init__.py").write_text(init_text, encoding="utf-8")

    main_text = (
        dedent(
            """
        from __future__ import annotations

        from csharp_to_python_learning import main


        if __name__ == "__main__":
            main()
        """
        ).strip()
        + "\n"
    )
    (src / "__main__.py").write_text(main_text, encoding="utf-8")


def write_capstone(root: Path) -> Path:
    capstone_dir = root / "src" / "csharp_to_python_learning" / "capstone"
    capstone_dir.mkdir(parents=True, exist_ok=True)
    path = capstone_dir / "capstone_async_event_pipeline.py"
    path.write_text(CAPSTONE_CODE + "\n", encoding="utf-8")
    return path


def write_python_only(root: Path) -> list[Path]:
    feature_dir = root / "src" / "csharp_to_python_learning" / "python_only_features"
    feature_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for filename, _title, code in PYTHON_ONLY_FEATURES:
        path = feature_dir / filename
        path.write_text(dedent(code).strip() + "\n", encoding="utf-8")
        paths.append(path)
    return paths


def write_concepts(root: Path) -> list[Path]:
    concept_paths: list[Path] = []
    concept_root = root / "src" / "csharp_to_python_learning" / "concepts"
    for topic in TOPICS:
        directory = concept_root / topic.group
        directory.mkdir(parents=True, exist_ok=True)
        filename = f"topic_{topic.number:02d}_{topic.slug}.py"
        path = directory / filename
        path.write_text(render_topic(topic), encoding="utf-8")
        concept_paths.append(path)
    return concept_paths


def write_gitkeep(root: Path) -> None:
    tools = root / "tools"
    tools.mkdir(parents=True, exist_ok=True)
    (tools / ".gitkeep").write_text("", encoding="utf-8")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    src = root / "src" / "csharp_to_python_learning"
    src.mkdir(parents=True, exist_ok=True)
    write_package_files(src)
    concept_paths = write_concepts(root)
    python_only_paths = write_python_only(root)
    capstone_path = write_capstone(root)
    write_tests(root)
    write_gitkeep(root)

    readme = build_readme(
        [path.relative_to(root) for path in concept_paths],
        [path.relative_to(root) for path in python_only_paths] + [capstone_path.relative_to(root)],
    )
    (root / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    main()
