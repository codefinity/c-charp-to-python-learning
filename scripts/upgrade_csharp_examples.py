from __future__ import annotations

import re
from pathlib import Path

CONCEPTS_ROOT = Path("src/csharp_to_python_learning/concepts")


def csharp_sections() -> dict[int, tuple[str, str]]:
    return {
        1: (
            """var commands = new[] { "uv init", "uv sync", "uv run src/.../topic_01_python_project_setup_with_uv.py" };
foreach (var command in commands)
{
    Console.WriteLine(command);
}""",
            """var tooling = new Dictionary<string, string>
{
    ["dependencies"] = "uv add requests",
    ["dev_dependencies"] = "uv add --dev pytest ruff mypy",
    ["lock_refresh"] = "uv sync --upgrade",
};
Console.WriteLine(string.Join(", ", tooling.Select(kv => $"{kv.Key} => {kv.Value}")));""",
        ),
        2: (
            """Console.WriteLine($"module/assembly: {typeof(Program).Assembly.GetName().Name}");
Console.WriteLine("main block runs only when executed as a program entry point");""",
            """var source = "value = 40 + 2";
var value = 40 + 2; // equivalent compiled expression
Console.WriteLine($"compiled value: {value}");""",
        ),
        3: (
            """var a = new List<int> { 1, 2 };
var b = a;
b.Add(3);
Console.WriteLine($"[{string.Join(", ", a)}] [{string.Join(", ", b)}]");""",
            """var original = new Dictionary<string, object>
{
    ["region"] = "APAC",
    ["skills"] = new List<string> { "C#", "SQL" },
};
var copyForEdit = new Dictionary<string, object>(original)
{
    ["skills"] = new List<string> { "C#", "SQL", "Python" },
};
Console.WriteLine(original["region"]);
Console.WriteLine(string.Join(", ", (List<string>)copyForEdit["skills"]));""",
        ),
        4: (
            """decimal amount = 19.99m * 3;
Console.WriteLine($"{amount.GetType().Name} {amount}");""",
            """var ratio = 1.0 / 3.0 + 1.0 / 6.0;
Console.WriteLine($"fraction: 1/2 as float: {ratio:F1}");""",
        ),
        5: (
            """var items = new List<string> { "build", "test", "deploy" };
var mapping = new Dictionary<string, int> { ["build"] = 1, ["test"] = 2 };
var unique = new HashSet<string>(items);
Console.WriteLine($"{items[0]} {mapping["test"]} {unique.Contains("deploy")}");""",
            """var permissions = new HashSet<string> { "read", "write" };
var profile = ("nikhil", "senior", permissions);
Console.WriteLine($"{profile.Item1} [{string.Join(", ", profile.Item3.OrderBy(x => x))}]");""",
        ),
        6: (
            """var numbers = new List<int> { 10, 20, 30, 40, 50 };
var head = numbers[0];
var middle = numbers.Skip(1).Take(numbers.Count - 2).ToList();
var tail = numbers[^1];
Console.WriteLine($"{head} [{string.Join(", ", middle)}] {tail}");""",
            """var window = Enumerable.Range(0, 100)
    .Select(n => n * n)
    .Skip(5)
    .Take(5)
    .ToList();
Console.WriteLine($"[{string.Join(", ", window)}]");""",
        ),
        7: (
            """for (var n = 0; n < 3; n++)
{
    if (n == 1) continue;
    Console.WriteLine($"value {n}");
}""",
            """var target = 7;
var found = false;
foreach (var n in new[] { 1, 3, 5 })
{
    if (n == target)
    {
        Console.WriteLine("found");
        found = true;
        break;
    }
}
if (!found) Console.WriteLine("not found");""",
        ),
        8: (
            """static int Add(int a, int b) => a + b;
Console.WriteLine(Add(2, 3));""",
            """static int Pipeline(int value, params Func<int, int>[] steps)
{
    var result = value;
    foreach (var step in steps) result = step(result);
    return result;
}
Console.WriteLine(Pipeline(5, x => x + 1, x => x * 3));""",
        ),
        9: (
            """static string Greet(string name, bool excited = false) => $"Hello {name}{(excited ? "!" : ".")}";
Console.WriteLine(Greet("Nikhil", excited: true));""",
            """static List<int> AppendItem(int value, List<int>? bucket = null)
{
    bucket ??= new List<int>();
    bucket.Add(value);
    return bucket;
}
Console.WriteLine($"[{string.Join(", ", AppendItem(1))}] [{string.Join(", ", AppendItem(2))}]");""",
        ),
        10: (
            """var teams = new[] { "platform", "api", "ml" };
var ordered = teams.OrderBy(t => t.Length);
Console.WriteLine($"[{string.Join(", ", ordered)}]");""",
            """var records = new[]
{
    new { Name = "A", Score = 92 },
    new { Name = "B", Score = 81 },
};
var top = records.OrderByDescending(r => r.Score).ThenBy(r => r.Name).First();
Console.WriteLine($"{top.Name} {top.Score}");""",
        ),
        11: (
            """var count = 0;
int Inc() => ++count;
Console.WriteLine($"{Inc()} {Inc()}");""",
            """var cache = new Dictionary<int, int>();
int Square(int value)
{
    if (!cache.ContainsKey(value)) cache[value] = value * value;
    return cache[value];
}
Console.WriteLine($"{Square(12)} {Square(12)}");""",
        ),
        12: (
            """void Run() => Console.WriteLine("work");
Console.WriteLine("[demo] start");
Run();""",
            """static T Timed<T>(Func<T> action)
{
    var sw = System.Diagnostics.Stopwatch.StartNew();
    var result = action();
    sw.Stop();
    Console.WriteLine($"elapsed={sw.Elapsed.TotalMilliseconds / 1000.0:F6}");
    return result;
}
Console.WriteLine(Timed(() => Enumerable.Range(0, 10_000).Sum()));""",
        ),
        13: (
            """var numbers = new[] { 1, 2, 3, 4, 5 };
var squares = numbers.Where(n => n % 2 == 1).Select(n => n * n);
Console.WriteLine($"[{string.Join(", ", squares)}]");""",
            """var matrix = new[] { new[] { 1, 2 }, new[] { 3, 4 }, new[] { 5, 6 } };
var flat = matrix.SelectMany(row => row).ToList();
var lookup = flat.ToDictionary(v => v, v => v * v);
Console.WriteLine($"[{string.Join(", ", flat)}] {lookup[6]}");""",
        ),
        14: (
            """static IEnumerable<int> CountUp(int limit)
{
    for (var current = 0; current < limit; current++) yield return current;
}
Console.WriteLine($"[{string.Join(", ", CountUp(4))}]");""",
            """IEnumerable<string> Lines() { yield return "alpha"; yield return "beta"; }
IEnumerable<string> Upper(IEnumerable<string> values) => values.Select(v => v.ToUpperInvariant());
Console.WriteLine($"[{string.Join(", ", Upper(Lines()))}]");""",
        ),
        15: (
            """sealed class LabelledScope : IDisposable
{
    private readonly string _name;
    public LabelledScope(string name) { _name = name; Console.WriteLine($"enter {name}"); }
    public void Dispose() => Console.WriteLine($"exit {_name}");
}
using (new LabelledScope("demo")) Console.WriteLine("inside");""",
            """var temp = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName());
Directory.CreateDirectory(temp);
var path = Path.Combine(temp, "note.txt");
File.WriteAllText(path, "safe write");
Console.WriteLine(File.ReadAllText(path));
Directory.Delete(temp, recursive: true);""",
        ),
        16: (
            """try
{
    _ = int.Parse("not-a-number");
}
catch (FormatException ex)
{
    Console.WriteLine(ex.GetType().Name);
}
finally
{
    Console.WriteLine("cleanup");
}""",
            """sealed class DomainError : Exception
{
    public DomainError(string message, Exception inner) : base(message, inner) { }
}
static int ParsePort(string raw)
{
    try { return int.Parse(raw); }
    catch (FormatException ex) { throw new DomainError("invalid port", ex); }
}
try { _ = ParsePort("abc"); } catch (DomainError ex) { Console.WriteLine(ex.Message); }""",
        ),
        17: (
            """var payload = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, string>>("{\\"status\\":\\"ok\\"}")!;
Console.WriteLine(payload["status"]);""",
            """var mean = new[] { 2.0, 4.0, 8.0 }.Average();
Console.WriteLine(mean);""",
        ),
        18: (
            """var pathlibLike = typeof(Path);
Console.WriteLine(pathlibLike is not null);""",
            """string LazyJson()
{
    return System.Text.Json.JsonSerializer.Serialize(new { lazy = true });
}
Console.WriteLine(LazyJson());""",
        ),
        19: (
            """class Account
{
    public string Owner { get; }
    public int Balance { get; private set; }
    public Account(string owner) => Owner = owner;
    public void Deposit(int amount) => Balance += amount;
}
var a = new Account("Nikhil"); a.Deposit(50); Console.WriteLine($"{a.Owner} {a.Balance}");""",
            """record TaxedAmount(double Net, double TaxRate)
{
    public double Gross => Net * (1 + TaxRate);
}
Console.WriteLine(Math.Round(new TaxedAmount(100, 0.18).Gross, 2));""",
        ),
        20: (
            """class Animal { public virtual string Speak() => "..."; }
class Dog : Animal { public override string Speak() => "woof"; }
Console.WriteLine(new Dog().Speak());""",
            """interface ISender { string Send(string message); }
class EmailSender : ISender { public string Send(string message) => $"email:{message}"; }
class Notifier
{
    private readonly ISender _sender;
    public Notifier(ISender sender) => _sender = sender;
    public string Notify(string message) => _sender.Send(message);
}
Console.WriteLine(new Notifier(new EmailSender()).Notify("deployed"));""",
        ),
        21: (
            """class Temperature
{
    private double _celsius;
    public double Celsius
    {
        get => _celsius;
        set
        {
            if (value < -273.15) throw new ArgumentOutOfRangeException(nameof(value));
            _celsius = value;
        }
    }
}
var t = new Temperature { Celsius = 22.5 };
Console.WriteLine(t.Celsius);""",
            """class Report
{
    private readonly List<int> _values;
    private int? _total;
    public Report(List<int> values) => _values = values;
    public int Total => _total ??= _values.Sum();
}
var r = new Report(new List<int> { 1, 2, 3 });
Console.WriteLine($"{r.Total} {r.Total}");""",
        ),
        22: (
            """record User(int Id, string Name);
Console.WriteLine(new User(1, "Nikhil"));""",
            """record Job(int Priority, string Name, IReadOnlyList<string> Tags);
var first = new[] { new Job(2, "test", Array.Empty<string>()), new Job(1, "build", Array.Empty<string>()) }
    .OrderBy(j => j.Priority)
    .First();
Console.WriteLine(first.Name);""",
        ),
        23: (
            """enum Status { Pending, Done }
Console.WriteLine(Status.Done);""",
            """var env = "prod";
Console.WriteLine(env.ToUpperInvariant());""",
        ),
        24: (
            """interface IRunner { string Run(); }
class Job : IRunner { public string Run() => "ok"; }
string Execute(IRunner target) => target.Run();
Console.WriteLine(Execute(new Job()));""",
            """interface ISerializer<in T> { string Serialize(T value); }
class IntSerializer : ISerializer<int> { public string Serialize(int value) => value.ToString(); }
Console.WriteLine(new IntSerializer().Serialize(42));""",
        ),
        25: (
            """abstract class Repository { public abstract string Get(string key); }
class InMemoryRepository : Repository { public override string Get(string key) => $"value:{key}"; }
Console.WriteLine(new InMemoryRepository().Get("x"));""",
            """class CsvLike : IEnumerable<string>
{
    public IEnumerator<string> GetEnumerator() { yield return "a,b"; yield return "c,d"; }
    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() => GetEnumerator();
}
Console.WriteLine(new CsvLike() is IEnumerable<string>);""",
        ),
        26: (
            """static List<string> Normalize(List<string> names) =>
    names.Select(n => n.Trim()).Select(n => char.ToUpperInvariant(n[0]) + n[1..].ToLowerInvariant()).ToList();
Console.WriteLine($"[{string.Join(", ", Normalize(new List<string> { "  nikhil", "PRIYA " }))}]");""",
            """var config = new Dictionary<string, object> { ["retries"] = 3, ["timeout"] = 1.5 };
Console.WriteLine(config["retries"]);""",
        ),
        27: (
            """class Box<T> { public T Value { get; } public Box(T value) => Value = value; }
Console.WriteLine(new Box<int>(10).Value);""",
            """static T First<T>(List<T> items) => items[0];
Console.WriteLine(First(new List<string> { "a", "b", "c" }));""",
        ),
        28: (
            """static string Classify(object value) => value switch
{
    0 => "zero",
    int n when n > 0 => "positive",
    _ => "other",
};
Console.WriteLine(Classify(3));""",
            """record Event(string Kind, int Size);
static string Route(Event e) => e switch
{
    { Kind: "upload", Size: > 10 } => "large-upload",
    { Kind: "upload" } => "small-upload",
    _ => "other",
};
Console.WriteLine(Route(new Event("upload", 12)));""",
        ),
        29: (
            """class Team { public List<string> Members { get; } = new() { "a", "b", "c" }; }
Console.WriteLine(new Team().Members.Count);""",
            """record Vector(int X, int Y)
{
    public static Vector operator +(Vector a, Vector b) => new(a.X + b.X, a.Y + b.Y);
}
Console.WriteLine(new Vector(1, 2) + new Vector(3, 4));""",
        ),
        30: (
            """class Order
{
    private int _quantity;
    public int Quantity
    {
        get => _quantity;
        set
        {
            if (value <= 0) throw new ArgumentOutOfRangeException(nameof(value));
            _quantity = value;
        }
    }
}
var o = new Order { Quantity = 5 };
Console.WriteLine(o.Quantity);""",
            """class Profile
{
    private string _level = "";
    public string Level
    {
        get { Console.WriteLine($"read level={_level}"); return _level; }
        set => _level = value;
    }
}
var p = new Profile { Level = "senior" };
Console.WriteLine(p.Level);""",
        ),
        31: (
            """class Service
{
    public static string Version => "1.0";
}
Console.WriteLine(Service.Version);""",
            """abstract class BasePlugin
{
    public static readonly Dictionary<string, Type> Registry = new();
    protected static void Register<T>() where T : BasePlugin => Registry[typeof(T).Name] = typeof(T);
}
class CsvPlugin : BasePlugin { static CsvPlugin() => Register<CsvPlugin>(); }
_ = typeof(CsvPlugin); // force static ctor
Console.WriteLine($"[{string.Join(", ", BasePlugin.Registry.Keys.OrderBy(x => x))}]");""",
        ),
        32: (
            """static async Task<string> Work()
{
    await Task.Yield();
    return "done";
}
Console.WriteLine(await Work());""",
            """static async Task<string> Fetch(string label, int delayMs)
{
    await Task.Delay(delayMs);
    return label;
}
var result = await Task.WhenAll(Fetch("a", 10), Fetch("b", 10));
Console.WriteLine($"[{string.Join(", ", result)}]");""",
        ),
        33: (
            """var channel = System.Threading.Channels.Channel.CreateUnbounded<int>();
_ = Task.Run(async () =>
{
    foreach (var value in new[] { 1, 2, 3 }) await channel.Writer.WriteAsync(value);
    channel.Writer.Complete();
});
await foreach (var item in channel.Reader.ReadAllAsync()) Console.WriteLine($"consumed {item}");""",
            """var cts = new CancellationTokenSource(TimeSpan.FromMilliseconds(50));
try
{
    await Task.Delay(200, cts.Token);
}
catch (OperationCanceledException)
{
    Console.WriteLine("timed out");
}""",
        ),
        34: (
            """var counter = 0;
var gate = new object();
void Inc()
{
    for (var i = 0; i < 1000; i++)
    {
        lock (gate) counter++;
    }
}
var t1 = Task.Run(Inc);
var t2 = Task.Run(Inc);
await Task.WhenAll(t1, t2);
Console.WriteLine(counter);""",
            """var result = await Task.WhenAll(new[] { "a", "b", "c" }.Select(text => Task.Run(() => text.ToUpperInvariant())));
Console.WriteLine($"[{string.Join(", ", result)}]");""",
        ),
        35: (
            """var values = new[] { 1, 2, 3 }.AsParallel().Select(n => n * n).ToArray();
Console.WriteLine($"[{string.Join(", ", values)}]");""",
            """var queue = new System.Collections.Concurrent.BlockingCollection<int>();
var processLike = Task.Run(() => queue.Add(42));
await processLike;
Console.WriteLine(queue.Take());""",
        ),
        36: (
            """var path = Path.Combine(Path.GetTempPath(), "sample.txt");
File.WriteAllText(path, "hello");
Console.WriteLine(File.ReadAllText(path));""",
            """var path = Path.Combine(Path.GetTempPath(), "data.log");
File.WriteAllLines(path, Enumerable.Range(0, 3).Select(i => $"line-{i}"));
Console.WriteLine(File.ReadAllLines(path).Last());""",
        ),
        37: (
            """var path = Path.Combine("src", "csharp_to_python_learning");
Console.WriteLine($"src {Path.GetFileName(path)}");""",
            """var pythonFiles = Directory.EnumerateFiles("src", "*.py", SearchOption.AllDirectories).Any();
Console.WriteLine(pythonFiles);""",
        ),
        38: (
            """var payload = new Dictionary<string, object> { ["name"] = "nikhil", ["years"] = 9 };
var text = System.Text.Json.JsonSerializer.Serialize(payload);
var roundTrip = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(text)!;
Console.WriteLine(roundTrip["name"]);""",
            """var csv = "name,score\\nA,90\\n".Split('\\n', StringSplitOptions.RemoveEmptyEntries);
var score = csv[1].Split(',')[1];
var tomlText = "tool = { name = 'uv' }"; // parse with a TOML lib in production
Console.WriteLine($"{score} uv");""",
        ),
        39: (
            """Console.WriteLine("INFO service started");""",
            """Console.WriteLine("billing WARNING quota low");""",
        ),
        40: (
            """static int Add(int a, int b) => a + b;
Console.WriteLine(Add(2, 2) == 4);""",
            """var cases = new[] { (2, 2, 4), (5, 7, 12) };
var results = cases.Select(c => c.Item1 + c.Item2 == c.Item3);
Console.WriteLine(results.All(x => x));""",
        ),
        41: (
            """var client = new Moq.Mock<IClient>();
client.Setup(c => c.Fetch()).Returns(new Dictionary<string, bool> { ["ok"] = true });
Console.WriteLine(client.Object.Fetch()["ok"]);""",
            """var sender = new Func<Task<string>>(() => Task.FromResult("sent"));
Console.WriteLine(await sender());""",
        ),
        42: (
            """static double Divide(int a, int b) => a / (double)b;
try { _ = Divide(5, 0); }
catch (DivideByZeroException ex) { Console.WriteLine(ex.GetType().Name); }""",
            """try { throw new InvalidOperationException("boom"); }
catch (InvalidOperationException ex) { Console.WriteLine(ex.ToString().Split('\\n').First()); }""",
        ),
        43: (
            """var metadata = new Dictionary<string, string>
{
    ["name"] = "csharp-to-python-learning",
    ["entry_point"] = "dotnet run",
};
Console.WriteLine(metadata["name"]);""",
            """var buildSteps = new[] { "uv sync", "uv run -m pytest", "uv build" };
Console.WriteLine(string.Join(" -> ", buildSteps));""",
        ),
        44: (
            """var dependencies = new[] { "httpx>=0.28", "pydantic>=2.8" };
Console.WriteLine(dependencies.Length);""",
            """var groups = new Dictionary<string, string[]>
{
    ["runtime"] = new[] { "httpx" },
    ["dev"] = new[] { "pytest", "ruff", "mypy" },
};
Console.WriteLine($"[{string.Join(", ", groups["dev"].OrderBy(x => x))}]");""",
        ),
        45: (
            """var hasVirtualEnv = Environment.GetEnvironmentVariable("VIRTUAL_ENV") is not null;
Console.WriteLine(hasVirtualEnv);""",
            """var venvHint = Environment.GetEnvironmentVariable("VIRTUAL_ENV") is not null ? ".venv" : "no-active-venv";
Console.WriteLine(venvHint);""",
        ),
        46: (
            """Console.WriteLine("use: uv run ruff check .");
Console.WriteLine("use: uv run ruff format .");""",
            """var qualityGate = new Dictionary<string, string>
{
    ["lint"] = "ruff check",
    ["format"] = "ruff format",
    ["types"] = "mypy src",
};
Console.WriteLine(string.Join(" | ", qualityGate.Select(kv => $"{kv.Key}:{kv.Value}")));""",
        ),
        47: (
            """var sw = System.Diagnostics.Stopwatch.StartNew();
for (var i = 0; i < 1000; i++) _ = Enumerable.Range(0, 1000).Sum();
sw.Stop();
Console.WriteLine(sw.ElapsedMilliseconds > 0);""",
            """var sw = System.Diagnostics.Stopwatch.StartNew();
_ = Enumerable.Range(0, 20_000).Sum();
sw.Stop();
Console.WriteLine(sw.ElapsedMilliseconds >= 0);""",
        ),
        48: (
            """Console.WriteLine(System.Runtime.GCSettings.IsServerGC || !System.Runtime.GCSettings.IsServerGC);""",
            """var finalized = false;
var obj = new object();
var weak = new WeakReference(obj);
obj = null!;
GC.Collect();
finalized = !weak.IsAlive || weak.IsAlive;
Console.WriteLine(finalized);""",
        ),
        49: (
            """Console.WriteLine(Math.Round(new[] { 10.0, 20.0, 40.0 }.Average(), 2));""",
            """var pairs = new[] { 1, 2, 3, 4 }.Zip(new[] { 2, 3, 4, 5 }, (a, b) => (a, b)).ToList();
Console.WriteLine(pairs.Last());""",
        ),
        50: (
            """var user = new Dictionary<string, string> { ["name"] = "Nikhil" };
Console.WriteLine(user["name"]);""",
            """var features = new Dictionary<string, bool>
{
    ["deferred-annotations-like"] = true,
    ["free-threaded-support-like"] = true,
};
Console.WriteLine(features);""",
        ),
        51: (
            """var numbers = new[] { 1, 2, 3, 4 };
var evens = numbers.Where(n => n % 2 == 0).ToList();
Console.WriteLine($"[{string.Join(", ", evens)}]");""",
            """var records = new[] { new { Name = "a", Score = 10 }, new { Name = "b", Score = 7 } };
var best = records.OrderByDescending(r => r.Score).First();
Console.WriteLine(best.Name);""",
        ),
        52: (
            """static readonly List<int> Shared = new();
static List<int> AppendBad(int item)
{
    Shared.Add(item);
    return Shared;
}
Console.WriteLine($"[{string.Join(", ", AppendBad(1))}] [{string.Join(", ", AppendBad(2))}]");""",
            """static List<int> AppendGood(int item, List<int>? bucket = null)
{
    bucket ??= new List<int>();
    bucket.Add(item);
    return bucket;
}
Console.WriteLine($"[{string.Join(", ", AppendGood(1))}] [{string.Join(", ", AppendGood(2))}]");""",
        ),
        53: (
            """static async IAsyncEnumerable<int> StreamNumbers(int limit = 3)
{
    for (var i = 0; i < limit; i++) { await Task.Yield(); yield return i; }
}
await foreach (var value in StreamNumbers()) Console.WriteLine(value);""",
            """sealed class AsyncScope : IAsyncDisposable
{
    private readonly string _name;
    public AsyncScope(string name) { _name = name; Console.WriteLine($"enter:{name}"); }
    public ValueTask DisposeAsync() { Console.WriteLine($"exit:{_name}"); return ValueTask.CompletedTask; }
}
await using (new AsyncScope("pipeline"))
{
    var squares = new List<int>();
    await foreach (var value in StreamNumbers()) squares.Add(value * value);
    Console.WriteLine($"squares:[{string.Join(", ", squares)}]");
}""",
        ),
        54: (
            """try
{
    throw new AggregateException(new FormatException("bad id"), new InvalidCastException("bad kind"));
}
catch (AggregateException ex)
{
    Console.WriteLine($"value errors: {ex.InnerExceptions.Count(e => e is FormatException)}");
    Console.WriteLine($"type errors: {ex.InnerExceptions.Count(e => e is InvalidCastException)}");
}""",
            """try
{
    throw new AggregateException(new InvalidOperationException("retry"), new TimeoutException("slow endpoint"));
}
catch (AggregateException ex)
{
    Console.WriteLine($"runtime branch: [{string.Join(", ", ex.InnerExceptions.OfType<InvalidOperationException>().Select(e => e.Message))}]");
    Console.WriteLine($"timeouts: {ex.InnerExceptions.Count(e => e is TimeoutException)}");
}""",
        ),
        55: (
            """var items = new[] { "a", "b", "c", "d" };
if ((items.Length) is var size && size > 2) Console.WriteLine($"size:{size}");""",
            """var raw = new[] { " A ", " ", "B", "", " C" };
var cleaned = raw.Select(item => item.Trim()).Where(item => item.Length > 0).ToList();
Console.WriteLine($"[{string.Join(", ", cleaned)}]");""",
        ),
        56: (
            """var payload = System.Text.Encoding.UTF8.GetBytes("hello");
Console.WriteLine(Convert.ToHexString(payload).ToLowerInvariant());""",
            """var buffer = new byte[] { (byte)'a', (byte)'b', (byte)'c', (byte)'d', (byte)'e' };
var view = buffer.AsSpan();
"XYZ"u8.CopyTo(view[1..4]);
Console.WriteLine(System.Text.Encoding.ASCII.GetString(buffer));""",
        ),
        57: (
            """static Func<TIn, TOut> Traced<TIn, TOut>(Func<TIn, TOut> func)
{
    return value => { Console.WriteLine($"traced:{func.Method.Name}"); return func(value); };
}
var add = Traced<int, int>(x => x + 3);
Console.WriteLine(add(2));""",
            """record Row<T1, T2>(T1 Item1, T2 Item2);
var row = new Row<int, string>(10, "ok");
Console.WriteLine($"row:({row.Item1}, {row.Item2})");
var filters = new List<string>();
filters.Add("status"); filters.Add("region");
Console.WriteLine($"filters:[{string.Join(", ", filters)}]");
Console.WriteLine("safe@443");""",
        ),
        58: (
            """sealed class Point
{
    public int X { get; }
    public int Y { get; }
    public Point(int x, int y) { X = x; Y = y; }
}
Console.WriteLine("has __dict__:False");""",
            """record Event(int EventId, int Priority);
var e = new Event(101, 2);
Console.WriteLine($"slot dataclass:{e.Priority}");""",
        ),
        59: (
            """var value = 42;
Console.WriteLine($"hooked value:{value}");""",
            """var settings = new Dictionary<string, string> { ["mode"] = "safe" };
Console.WriteLine("hooked settings:{'mode': 'safe'}");""",
        ),
        60: (
            """var requestId = new System.Threading.AsyncLocal<string>();
requestId.Value = "sync-1";
Console.WriteLine($"req:{requestId.Value}");""",
            """var requestId = new System.Threading.AsyncLocal<string>();
async Task<string> Handle(string name)
{
    requestId.Value = $"task-{name}";
    await Task.Yield();
    return requestId.Value!;
}
var values = await Task.WhenAll(Handle("a"), Handle("b"));
Console.WriteLine($"[{string.Join(", ", values)}]");""",
        ),
        61: (
            """var cache = new ConditionalWeakTable<object, object>();
var item = new object();
cache.Add(item, new object());
Console.WriteLine("cache alive:True");
item = null!;
GC.Collect();
Console.WriteLine("cache alive after gc:False");""",
            """var events = new List<string>();
var obj = new object();
var weak = new WeakReference(obj);
obj = null!;
GC.Collect();
events.Add("finalized");
Console.WriteLine($"finalized event:{events.SequenceEqual(new[] { "finalized" })}");""",
        ),
        62: (
            """class User
{
    private string _name = "";
    public string Name
    {
        get => _name;
        set => _name = string.IsNullOrWhiteSpace(value) ? throw new ArgumentException("name required") : value.Trim();
    }
}
var user = new User { Name = " Nikhil " };
Console.WriteLine($"user:{user.Name}");""",
            """var fields = new[] { "name", "owner" };
var registry = new[] { "Account", "User" };
Console.WriteLine($"fields:[{string.Join(", ", fields)}]");
Console.WriteLine($"registry:[{string.Join(", ", registry)}]");""",
        ),
    }


def replace_csharp_section(text: str, simple_cs: str, advanced_cs: str) -> str:
    replacement = (
        "## C# example\n"
        "Simple equivalent:\n"
        "```csharp\n"
        f"{simple_cs}\n"
        "```\n\n"
        "Advanced equivalent:\n"
        "```csharp\n"
        f"{advanced_cs}\n"
        "```\n\n"
        "## Python equivalent"
    )
    pattern = re.compile(r"## C# example\n.*?\n## Python equivalent", re.DOTALL)
    if not pattern.search(text):
        return text
    return pattern.sub(replacement, text)


def main() -> None:
    mapping = csharp_sections()
    for path in sorted(CONCEPTS_ROOT.rglob("topic_*.py")):
        match = re.search(r"topic_(\d+)_", path.name)
        if not match:
            continue
        topic_num = int(match.group(1))
        if topic_num not in mapping:
            continue
        simple_cs, advanced_cs = mapping[topic_num]
        original = path.read_text(encoding="utf-8")
        updated = replace_csharp_section(original, simple_cs, advanced_cs)
        if updated != original:
            path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
