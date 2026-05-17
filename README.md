# C# to Python: Advanced, Production-Ready Tutorial (Python 3.14.5 + uv)

## Who This Repository Is For
This repository is for experienced C#/.NET developers who already understand OOP, generics, LINQ, async/await, dependency injection, build tools, and testing.  
The goal is to help you become an advanced Python developer who can ship production-grade code confidently.

## Table of Contents
- [Who This Repository Is For](#who-this-repository-is-for)
- [Quick Start](#quick-start)
- [How To Use uv In This Project](#how-to-use-uv-in-this-project)
- [Tutorial Concepts](#tutorial-concepts)
- [Advanced Walkthrough for C# Developers](#advanced-walkthrough-for-c-developers)
- [Python-Only Features](#python-only-features)
- [C# Features With No Direct Python Equivalent](#c-features-with-no-direct-python-equivalent)
- [Python Features With No Direct C# Equivalent](#python-features-with-no-direct-c-equivalent)
- [1-Week Study Plan](#1-week-study-plan)
- [Capstone Project](#capstone-project)
- [Further Study](#further-study)

## Quick Start
```bash
uv sync
uv run src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py
uv run -m pytest
```

## How To Use uv In This Project
### `uv init`
Initialize a new project (already done in this repository):
```bash
uv init --package --python 3.14.5
```

### `uv sync`
Create/update `.venv` and install dependencies from `pyproject.toml` + `uv.lock`:
```bash
uv sync
```

### `uv run`
Run a command inside the project environment:
```bash
uv run -m pytest
uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py
```

### `uv add`
Add a runtime dependency:
```bash
uv add httpx
```
Add a dev dependency:
```bash
uv add --dev pytest ruff mypy
```

### Running Tests
```bash
uv run -m pytest
uv run -m pytest tests/test_concept_smoke.py -k asyncio
```

### Running Individual Examples
Every concept is runnable directly:
```bash
uv run src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_50_python_3_14_specific_features.py
```

## Tutorial Concepts
- **1. Python project setup with uv**: Use `uv` as the Python equivalent of `dotnet new`, `dotnet restore`, and `dotnet run` in one fast workflow. Run: `uv run src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py` | File: [src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py](src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py)
- **2. Python execution model**: Python executes modules top-to-bottom and binds names at runtime, then runs guarded script code under `if __name__ == '__main__'`. Run: `uv run src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_02_python_execution_model.py` | File: [src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_02_python_execution_model.py](src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_02_python_execution_model.py)
- **3. Variables, names, references, and mutability**: Python names point to objects; assignment rebinds names, while mutating a shared object affects all aliases. Run: `uv run src/csharp_to_python_learning/concepts/02_data_and_flow/topic_03_variables_names_references_and_mutability.py` | File: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_03_variables_names_references_and_mutability.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_03_variables_names_references_and_mutability.py)
- **4. Primitive types**: Python has familiar scalar types (`int`, `float`, `bool`, `str`) plus precision types like `Decimal`. Run: `uv run src/csharp_to_python_learning/concepts/02_data_and_flow/topic_04_primitive_types.py` | File: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_04_primitive_types.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_04_primitive_types.py)
- **5. Collections: list, tuple, dict, set, frozenset**: Python collection types have different mutability and lookup guarantees; choosing the right one matters in production code. Run: `uv run src/csharp_to_python_learning/concepts/02_data_and_flow/topic_05_collections.py` | File: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_05_collections.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_05_collections.py)
- **6. Slicing and unpacking**: Python slicing and unpacking replace many verbose loop/indexing patterns common in C#. Run: `uv run src/csharp_to_python_learning/concepts/02_data_and_flow/topic_06_slicing_and_unpacking.py` | File: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_06_slicing_and_unpacking.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_06_slicing_and_unpacking.py)
- **7. Control flow**: Python control flow favors readability with indentation and expressive constructs like `for ... else`. Run: `uv run src/csharp_to_python_learning/concepts/02_data_and_flow/topic_07_control_flow.py` | File: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_07_control_flow.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_07_control_flow.py)
- **8. Functions**: Functions are first-class objects in Python, so you can pass and return them directly. Run: `uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_08_functions.py` | File: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_08_functions.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_08_functions.py)
- **9. Default arguments and keyword-only arguments**: Keyword-only arguments let you model explicit APIs like named optional parameters in C#. Run: `uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_09_default_and_keyword_only_arguments.py` | File: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_09_default_and_keyword_only_arguments.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_09_default_and_keyword_only_arguments.py)
- **10. Lambdas**: Python lambdas are small expression-only functions, best used inline for short transformations. Run: `uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_10_lambdas.py` | File: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_10_lambdas.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_10_lambdas.py)
- **11. Closures**: Closures capture surrounding state, similar to C# captured variables in local functions/lambdas. Run: `uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_11_closures.py` | File: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_11_closures.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_11_closures.py)
- **12. Decorators**: Decorators provide AOP-style wrappers for logging, validation, authorization, and instrumentation. Run: `uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py` | File: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py)
- **13. Comprehensions**: Comprehensions replace many LINQ `Select`/`Where` one-liners while staying explicit and Pythonic. Run: `uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_13_comprehensions.py` | File: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_13_comprehensions.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_13_comprehensions.py)
- **14. Iterators and generators**: Generators are lazy and memory-efficient, which is crucial for streaming and ETL workloads. Run: `uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_14_iterators_and_generators.py` | File: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_14_iterators_and_generators.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_14_iterators_and_generators.py)
- **15. Context managers**: Context managers are deterministic resource guards; think `using` blocks generalized for any enter/exit behavior. Run: `uv run src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_15_context_managers.py` | File: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_15_context_managers.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_15_context_managers.py)
- **16. Exceptions**: Python exceptions are value-carrying objects; use narrow catches and explicit re-raising for clarity. Run: `uv run src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_16_exceptions.py` | File: [src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_16_exceptions.py](src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_16_exceptions.py)
- **17. Modules and packages**: A Python package is a directory namespace, similar to assemblies + namespaces but resolved at runtime. Run: `uv run src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_17_modules_and_packages.py` | File: [src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_17_modules_and_packages.py](src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_17_modules_and_packages.py)
- **18. Imports and import system**: Imports are executable statements with caching in `sys.modules`; import style affects startup and clarity. Run: `uv run src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_18_imports_and_import_system.py` | File: [src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_18_imports_and_import_system.py](src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_18_imports_and_import_system.py)
- **19. Object-oriented programming**: Python supports classic OOP, but with less ceremony and more runtime flexibility than C#. Run: `uv run src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_19_object_oriented_programming.py` | File: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_19_object_oriented_programming.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_19_object_oriented_programming.py)
- **20. Inheritance and composition**: Prefer composition when behavior should vary at runtime; use inheritance for stable hierarchies. Run: `uv run src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_20_inheritance_and_composition.py` | File: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_20_inheritance_and_composition.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_20_inheritance_and_composition.py)
- **21. Properties**: Properties keep attribute syntax while enforcing invariants, similar to C# `get`/`set` properties. Run: `uv run src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_21_properties.py` | File: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_21_properties.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_21_properties.py)
- **22. Dataclasses**: Dataclasses are concise record-like types with optional immutability, ordering, and slots. Run: `uv run src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_22_dataclasses.py` | File: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_22_dataclasses.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_22_dataclasses.py)
- **23. Enums**: Enums model closed sets of values and avoid stringly-typed logic in business rules. Run: `uv run src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_23_enums.py` | File: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_23_enums.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_23_enums.py)
- **24. Protocols and structural typing**: Protocols model behavior contracts by shape (duck typing) instead of explicit inheritance. Run: `uv run src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_24_protocols_and_structural_typing.py` | File: [src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_24_protocols_and_structural_typing.py](src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_24_protocols_and_structural_typing.py)
- **25. Abstract base classes**: ABCs define explicit contracts and can also provide reusable default behavior. Run: `uv run src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_25_abstract_base_classes.py` | File: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_25_abstract_base_classes.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_25_abstract_base_classes.py)
- **26. Type hints**: Type hints improve readability and tooling without changing runtime behavior. Run: `uv run src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_26_type_hints.py` | File: [src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_26_type_hints.py](src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_26_type_hints.py)
- **27. Generics**: Python generics are type-checker friendly and map closely to C# generic classes and methods. Run: `uv run src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_27_generics.py` | File: [src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_27_generics.py](src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_27_generics.py)
- **28. Pattern matching**: Structural pattern matching is Python's expressive branching feature for tuple/list/dict/object shapes. Run: `uv run src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_28_pattern_matching.py` | File: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_28_pattern_matching.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_28_pattern_matching.py)
- **29. Dunder methods and Python data model**: Python objects participate in language syntax by implementing special (dunder) methods. Run: `uv run src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_29_dunder_methods_and_data_model.py` | File: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_29_dunder_methods_and_data_model.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_29_dunder_methods_and_data_model.py)
- **30. Descriptors**: Descriptors power `property`, ORM fields, and validation by intercepting attribute access at class level. Run: `uv run src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_30_descriptors.py` | File: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_30_descriptors.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_30_descriptors.py)
- **31. Metaclasses**: Metaclasses customize class creation and are useful for registries and framework hooks. Run: `uv run src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_31_metaclasses.py` | File: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_31_metaclasses.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_31_metaclasses.py)
- **32. Async and await**: Async functions represent suspendable workflows; use them for I/O concurrency, not CPU parallelism. Run: `uv run src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_32_async_and_await.py` | File: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_32_async_and_await.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_32_async_and_await.py)
- **33. asyncio tasks, queues, cancellation, timeouts**: Production asyncio code needs task orchestration, cancellation handling, queues, and timeout guards. Run: `uv run src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_33_asyncio_tasks_queues_cancellation_timeouts.py` | File: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_33_asyncio_tasks_queues_cancellation_timeouts.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_33_asyncio_tasks_queues_cancellation_timeouts.py)
- **34. Threading**: Threading works well for blocking I/O integration, protected with locks for shared mutable state. Run: `uv run src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_34_threading.py` | File: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_34_threading.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_34_threading.py)
- **35. Multiprocessing**: Use multiprocessing for CPU-bound work when threads are limited by interpreter-level contention. Run: `uv run src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_35_multiprocessing.py` | File: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_35_multiprocessing.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_35_multiprocessing.py)
- **36. File I/O**: Prefer explicit encodings and context managers for reliable file handling in production. Run: `uv run src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_36_file_io.py` | File: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_36_file_io.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_36_file_io.py)
- **37. pathlib**: `pathlib` gives object-oriented filesystem handling and replaces brittle string-based path logic. Run: `uv run src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_37_pathlib.py` | File: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_37_pathlib.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_37_pathlib.py)
- **38. JSON, CSV, TOML**: Python's standard library handles core data formats without external dependencies. Run: `uv run src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_38_json_csv_toml.py` | File: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_38_json_csv_toml.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_38_json_csv_toml.py)
- **39. Logging**: Structured, leveled logging is the production replacement for `print` debugging. Run: `uv run src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_39_logging.py` | File: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_39_logging.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_39_logging.py)
- **40. Testing with pytest**: `pytest` favors simple functions and powerful assertions for fast test feedback. Run: `uv run src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_40_testing_with_pytest.py` | File: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_40_testing_with_pytest.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_40_testing_with_pytest.py)
- **41. Mocking**: Use `unittest.mock` to isolate collaborators, side effects, and network boundaries. Run: `uv run src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_41_mocking.py` | File: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_41_mocking.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_41_mocking.py)
- **42. Debugging**: Combine debugger breakpoints, targeted logging, and tracebacks for efficient incident triage. Run: `uv run src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_42_debugging.py` | File: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_42_debugging.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_42_debugging.py)
- **43. Packaging**: Packaging turns source code into installable artifacts with metadata and entry points. Run: `uv run src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_43_packaging.py` | File: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_43_packaging.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_43_packaging.py)
- **44. Dependency management**: Pin dependencies and commit lock files for deterministic builds across machines and CI. Run: `uv run src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_44_dependency_management.py` | File: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_44_dependency_management.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_44_dependency_management.py)
- **45. Virtual environments**: Virtual environments isolate interpreter and package state per project, similar to per-solution toolchains. Run: `uv run src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_45_virtual_environments.py` | File: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_45_virtual_environments.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_45_virtual_environments.py)
- **46. Linters and formatters**: Ruff can handle linting and formatting quickly, replacing multiple separate tools in many projects. Run: `uv run src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_46_linters_and_formatters.py` | File: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_46_linters_and_formatters.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_46_linters_and_formatters.py)
- **47. Performance and profiling**: Measure before optimizing: combine `timeit`, `cProfile`, and algorithmic changes. Run: `uv run src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_47_performance_and_profiling.py` | File: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_47_performance_and_profiling.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_47_performance_and_profiling.py)
- **48. Memory management and garbage collection**: CPython uses reference counting plus cyclic GC; lifecycle choices affect latency and memory pressure. Run: `uv run src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_48_memory_management_and_gc.py` | File: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_48_memory_management_and_gc.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_48_memory_management_and_gc.py)
- **49. Standard library overview**: The standard library covers many production needs: paths, JSON, CLI parsing, concurrency, testing, and more. Run: `uv run src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_49_standard_library_overview.py` | File: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_49_standard_library_overview.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_49_standard_library_overview.py)
- **50. Python 3.14-specific features**: Python 3.14 adds deferred annotation behavior and stronger support for free-threaded execution. Run: `uv run src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_50_python_3_14_specific_features.py` | File: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_50_python_3_14_specific_features.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_50_python_3_14_specific_features.py)
- **51. Python idioms versus C# idioms**: Translate intent, not syntax: many C# patterns have shorter Pythonic forms. Run: `uv run src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_51_python_idioms_vs_csharp_idioms.py` | File: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_51_python_idioms_vs_csharp_idioms.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_51_python_idioms_vs_csharp_idioms.py)
- **52. Common C# to Python migration mistakes**: Most migration bugs come from mutability assumptions, import-time side effects, and overusing class-heavy designs. Run: `uv run src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_52_common_csharp_to_python_migration_mistakes.py` | File: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_52_common_csharp_to_python_migration_mistakes.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_52_common_csharp_to_python_migration_mistakes.py)
- **53. Async iteration, async generators, and async context managers**: Use `async for`, async comprehensions, and `async with` for async streaming and cleanup. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_53_async_iteration_and_async_context_managers.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_53_async_iteration_and_async_context_managers.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_53_async_iteration_and_async_context_managers.py)
- **54. Exception groups and `except*`**: Handle multiple concurrent failures by exception type in one flow. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_54_exception_groups_and_except_star.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_54_exception_groups_and_except_star.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_54_exception_groups_and_except_star.py)
- **55. Assignment expressions (`:=`)**: Use walrus assignments where inline binding improves readability. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_55_assignment_expressions.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_55_assignment_expressions.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_55_assignment_expressions.py)
- **56. Binary data: `bytes`, `bytearray`, and `memoryview`**: Work with immutable and mutable binary buffers and zero-copy views. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_56_binary_data_bytes_bytearray_memoryview.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_56_binary_data_bytes_bytearray_memoryview.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_56_binary_data_bytes_bytearray_memoryview.py)
- **57. Advanced typing extras**: Practical `ParamSpec`, `TypeVarTuple`, `Literal`, `Annotated`, and `Self` patterns. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_57_advanced_typing_paramspec_typevartuple_and_more.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_57_advanced_typing_paramspec_typevartuple_and_more.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_57_advanced_typing_paramspec_typevartuple_and_more.py)
- **58. `__slots__` as a language feature**: Restrict dynamic attributes and reduce instance overhead in hot paths. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_58_slots_as_a_language_feature.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_58_slots_as_a_language_feature.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_58_slots_as_a_language_feature.py)
- **59. Import hooks and custom loaders**: Customize module resolution using `sys.meta_path`, finders, and loaders. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_59_import_hooks_custom_finders_and_loaders.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_59_import_hooks_custom_finders_and_loaders.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_59_import_hooks_custom_finders_and_loaders.py)
- **60. `contextvars` and task-local state**: Carry request context safely across async tasks. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_60_contextvars_and_task_local_state.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_60_contextvars_and_task_local_state.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_60_contextvars_and_task_local_state.py)
- **61. Weak references and finalization patterns**: Build leak-resistant caches and lifecycle callbacks with `weakref`. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_61_weakref_and_finalization_patterns.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_61_weakref_and_finalization_patterns.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_61_weakref_and_finalization_patterns.py)
- **62. Advanced descriptor and metaclass patterns**: Centralized field validation and class-time registration patterns. Run: `uv run src/csharp_to_python_learning/concepts/11_additional_language_features/topic_62_advanced_descriptor_and_metaclass_patterns.py` | File: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_62_advanced_descriptor_and_metaclass_patterns.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_62_advanced_descriptor_and_metaclass_patterns.py)

<!-- ADVANCED_WALKTHROUGH_START -->
## Advanced Walkthrough for C# Developers
This section pulls advanced examples directly from each concept file and explains how to map them from familiar C#/.NET patterns to Python production practices.
Use this as the deep-dive track after you run each concept script once.

### 1. Python project setup with uv
Source: [src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py](src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
tooling = {
    "dependencies": "uv add requests",
    "dev_dependencies": "uv add --dev pytest ruff mypy",
    "lock_refresh": "uv sync --upgrade",
}
print(", ".join(f"{k} => {v}" for k, v in tooling.items()))
```

**Python equivalent**
Python approaches this concept with less ceremony: Use `uv` as the Python equivalent of `dotnet new`, `dotnet restore`, and `dotnet run` in one fast workflow. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Use `uv` as the Python equivalent of `dotnet new`, `dotnet restore`, and `dotnet run` in one fast workflow. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Python project setup with uv` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Python project setup with uv`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- uv init
- dependencies => uv add requests


### 2. Python execution model
Source: [src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_02_python_execution_model.py](src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_02_python_execution_model.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
source = "value = 40 + 2\nprint('compiled value:', value)"
code_object = compile(source, "<dynamic>", "exec")
exec(code_object)
```

**Python equivalent**
Python approaches this concept with less ceremony: Python executes modules top-to-bottom and binds names at runtime, then runs guarded script code under `if __name__ == '__main__'`. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python executes modules top-to-bottom and binds names at runtime, then runs guarded script code under `if __name__ == '__main__'`. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Python execution model` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Python execution model`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- module name:
- compiled value: 42


### 3. Variables, names, references, and mutability
Source: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_03_variables_names_references_and_mutability.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_03_variables_names_references_and_mutability.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
original = {"region": "APAC", "skills": ["C#", "SQL"]}
copy_for_edit = {**original, "skills": [*original["skills"], "Python"]}
print(original)
print(copy_for_edit)
```

**Python equivalent**
Python approaches this concept with less ceremony: Python names point to objects; assignment rebinds names, while mutating a shared object affects all aliases. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python names point to objects; assignment rebinds names, while mutating a shared object affects all aliases. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Variables, names, references, and mutability` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Variables, names, references, and mutability`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [1, 2, 3] [1, 2, 3]
- {'region': 'APAC', 'skills': ['C#', 'SQL']}


### 4. Primitive types
Source: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_04_primitive_types.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_04_primitive_types.py)

**What C# developers usually expect**
C# developers usually expect compile-time type contracts and explicit interfaces.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from fractions import Fraction

ratio = Fraction(1, 3) + Fraction(1, 6)
print("fraction:", ratio, "as float:", float(ratio))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python has familiar scalar types (`int`, `float`, `bool`, `str`) plus precision types like `Decimal`. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python has familiar scalar types (`int`, `float`, `bool`, `str`) plus precision types like `Decimal`. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Primitive types` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Primitive types`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- Decimal 59.97
- fraction: 1/2 as float: 0.5


### 5. Collections: list, tuple, dict, set, frozenset
Source: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_05_collections.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_05_collections.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
permissions = frozenset({"read", "write"})
profile = ("nikhil", "senior", permissions)
print(profile[0], sorted(profile[2]))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python collection types have different mutability and lookup guarantees; choosing the right one matters in production code. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python collection types have different mutability and lookup guarantees; choosing the right one matters in production code. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Collections: list, tuple, dict, set, frozenset` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Collections: list, tuple, dict, set, frozenset`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- build 2 True
- nikhil ['read', 'write']


### 6. Slicing and unpacking
Source: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_06_slicing_and_unpacking.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_06_slicing_and_unpacking.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from itertools import islice

stream = (n * n for n in range(100))
window = list(islice(stream, 5, 10))
print(window)
```

**Python equivalent**
Python approaches this concept with less ceremony: Python slicing and unpacking replace many verbose loop/indexing patterns common in C#. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python slicing and unpacking replace many verbose loop/indexing patterns common in C#. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Slicing and unpacking` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Slicing and unpacking`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 10 [20, 30, 40] 50
- [25, 36, 49, 64, 81]


### 7. Control flow
Source: [src/csharp_to_python_learning/concepts/02_data_and_flow/topic_07_control_flow.py](src/csharp_to_python_learning/concepts/02_data_and_flow/topic_07_control_flow.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
target = 7
for n in [1, 3, 5]:
    if n == target:
        print("found")
        break
else:
    print("not found")
```

**Python equivalent**
Python approaches this concept with less ceremony: Python control flow favors readability with indentation and expressive constructs like `for ... else`. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python control flow favors readability with indentation and expressive constructs like `for ... else`. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Control flow` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Control flow`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- value 0
- not found


### 8. Functions
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_08_functions.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_08_functions.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
def pipeline(value: int, *steps):
    result = value
    for step in steps:
        result = step(result)
    return result

print(pipeline(5, lambda x: x + 1, lambda x: x * 3))
```

**Python equivalent**
Python approaches this concept with less ceremony: Functions are first-class objects in Python, so you can pass and return them directly. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Functions are first-class objects in Python, so you can pass and return them directly. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Functions` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Functions`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 5
- 18


### 9. Default arguments and keyword-only arguments
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_09_default_and_keyword_only_arguments.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_09_default_and_keyword_only_arguments.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
def append_item(value: int, bucket: list[int] | None = None) -> list[int]:
    bucket = bucket or []
    bucket.append(value)
    return bucket

print(append_item(1), append_item(2))
```

**Python equivalent**
Python approaches this concept with less ceremony: Keyword-only arguments let you model explicit APIs like named optional parameters in C#. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Keyword-only arguments let you model explicit APIs like named optional parameters in C#. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Default arguments and keyword-only arguments` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Default arguments and keyword-only arguments`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- Hello Nikhil!
- [1] [2]


### 10. Lambdas
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_10_lambdas.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_10_lambdas.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
records = [{"name": "A", "score": 92}, {"name": "B", "score": 81}]
top = max(records, key=lambda r: (r["score"], r["name"]))
print(top["name"], top["score"])
```

**Python equivalent**
Python approaches this concept with less ceremony: Python lambdas are small expression-only functions, best used inline for short transformations. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python lambdas are small expression-only functions, best used inline for short transformations. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Lambdas` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Lambdas`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ['ml', 'api', 'platform']
- A 92


### 11. Closures
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_11_closures.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_11_closures.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
def memoized_square():
    cache: dict[int, int] = {}

    def run(value: int) -> int:
        if value not in cache:
            cache[value] = value * value
        return cache[value]

    return run

square = memoized_square()
print(square(12), square(12))
```

**Python equivalent**
Python approaches this concept with less ceremony: Closures capture surrounding state, similar to C# captured variables in local functions/lambdas. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Closures capture surrounding state, similar to C# captured variables in local functions/lambdas. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Closures` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Closures`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 1 2
- 144 144


### 12. Decorators
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
[LogExecution]
public void Run() { Console.WriteLine("work"); }
```

**Advanced Python example from this file**
```python
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
```

**Python equivalent**
Python approaches this concept with less ceremony: Decorators provide AOP-style wrappers for logging, validation, authorization, and instrumentation. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Decorators provide AOP-style wrappers for logging, validation, authorization, and instrumentation. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Decorators` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Decorators`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [demo] start
- elapsed=


### 13. Comprehensions
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_13_comprehensions.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_13_comprehensions.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [cell for row in matrix for cell in row]
lookup = {value: value * value for value in flat}
print(flat, lookup[6])
```

**Python equivalent**
Python approaches this concept with less ceremony: Comprehensions replace many LINQ `Select`/`Where` one-liners while staying explicit and Pythonic. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Comprehensions replace many LINQ `Select`/`Where` one-liners while staying explicit and Pythonic. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Comprehensions` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Comprehensions`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [1, 9, 25]
- [1, 2, 3, 4, 5, 6] 36


### 14. Iterators and generators
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_14_iterators_and_generators.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_14_iterators_and_generators.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
def lines():
    yield "alpha"
    yield "beta"

def upper(values):
    for value in values:
        yield value.upper()

print(list(upper(lines())))
```

**Python equivalent**
Python approaches this concept with less ceremony: Generators are lazy and memory-efficient, which is crucial for streaming and ETL workloads. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Generators are lazy and memory-efficient, which is crucial for streaming and ETL workloads. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Iterators and generators` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Iterators and generators`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [0, 1, 2, 3]
- ['ALPHA', 'BETA']


### 15. Context managers
Source: [src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_15_context_managers.py](src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_15_context_managers.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "note.txt"
    path.write_text("safe write", encoding="utf-8")
    print(path.read_text(encoding="utf-8"))
```

**Python equivalent**
Python approaches this concept with less ceremony: Context managers are deterministic resource guards; think `using` blocks generalized for any enter/exit behavior. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Context managers are deterministic resource guards; think `using` blocks generalized for any enter/exit behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Context managers` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Context managers`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- enter demo
- safe write


### 16. Exceptions
Source: [src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_16_exceptions.py](src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_16_exceptions.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
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
```

**Python equivalent**
Python approaches this concept with less ceremony: Python exceptions are value-carrying objects; use narrow catches and explicit re-raising for clarity. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python exceptions are value-carrying objects; use narrow catches and explicit re-raising for clarity. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Exceptions` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Exceptions`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ValueError
- invalid port


### 17. Modules and packages
Source: [src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_17_modules_and_packages.py](src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_17_modules_and_packages.py)

**What C# developers usually expect**
C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import importlib

module = importlib.import_module("statistics")
print(module.mean([2, 4, 8]))
```

**Python equivalent**
Python approaches this concept with less ceremony: A Python package is a directory namespace, similar to assemblies + namespaces but resolved at runtime. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
A Python package is a directory namespace, similar to assemblies + namespaces but resolved at runtime. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Modules and packages` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Modules and packages`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ok
- 4.666


### 18. Imports and import system
Source: [src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_18_imports_and_import_system.py](src/csharp_to_python_learning/concepts/04_errors_and_modules/topic_18_imports_and_import_system.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
def lazy_json():
    import json

    return json.dumps({"lazy": True})

print(lazy_json())
```

**Python equivalent**
Python approaches this concept with less ceremony: Imports are executable statements with caching in `sys.modules`; import style affects startup and clarity. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Imports are executable statements with caching in `sys.modules`; import style affects startup and clarity. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Imports and import system` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Imports and import system`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- {"lazy": true}


### 19. Object-oriented programming
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_19_object_oriented_programming.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_19_object_oriented_programming.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from dataclasses import dataclass

@dataclass
class TaxedAmount:
    net: float
    tax_rate: float

    @property
    def gross(self) -> float:
        return self.net * (1 + self.tax_rate)

print(round(TaxedAmount(100, 0.18).gross, 2))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python supports classic OOP, but with less ceremony and more runtime flexibility than C#. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python supports classic OOP, but with less ceremony and more runtime flexibility than C#. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Object-oriented programming` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Object-oriented programming`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- Nikhil 50
- 118.0


### 20. Inheritance and composition
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_20_inheritance_and_composition.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_20_inheritance_and_composition.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
class EmailSender:
    def send(self, message: str) -> str:
        return f"email:{message}"

class Notifier:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)

print(Notifier(EmailSender()).notify("deployed"))
```

**Python equivalent**
Python approaches this concept with less ceremony: Prefer composition when behavior should vary at runtime; use inheritance for stable hierarchies. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Prefer composition when behavior should vary at runtime; use inheritance for stable hierarchies. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Inheritance and composition` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Inheritance and composition`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- woof
- email:deployed


### 21. Properties
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_21_properties.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_21_properties.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
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
```

**Python equivalent**
Python approaches this concept with less ceremony: Properties keep attribute syntax while enforcing invariants, similar to C# `get`/`set` properties. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Properties keep attribute syntax while enforcing invariants, similar to C# `get`/`set` properties. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Properties` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Properties`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 22.5
- computing


### 22. Dataclasses
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_22_dataclasses.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_22_dataclasses.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True, slots=True)
class Job:
    priority: int
    name: str
    tags: tuple[str, ...] = field(default_factory=tuple)

print(sorted([Job(2, "test"), Job(1, "build")])[0].name)
```

**Python equivalent**
Python approaches this concept with less ceremony: Dataclasses are concise record-like types with optional immutability, ordering, and slots. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Dataclasses are concise record-like types with optional immutability, ordering, and slots. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Dataclasses` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Dataclasses`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- User(id=1, name='Nikhil')
- build


### 23. Enums
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_23_enums.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_23_enums.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from enum import StrEnum

class Environment(StrEnum):
    DEV = "dev"
    PROD = "prod"

print(Environment.PROD.upper())
```

**Python equivalent**
Python approaches this concept with less ceremony: Enums model closed sets of values and avoid stringly-typed logic in business rules. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Enums model closed sets of values and avoid stringly-typed logic in business rules. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Enums` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Enums`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- DONE
- PROD


### 24. Protocols and structural typing
Source: [src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_24_protocols_and_structural_typing.py](src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_24_protocols_and_structural_typing.py)

**What C# developers usually expect**
C# developers usually expect compile-time type contracts and explicit interfaces.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from typing import Protocol, TypeVar

T = TypeVar("T", contravariant=True)

class Serializer(Protocol[T]):
    def serialize(self, value: T) -> str: ...

class IntSerializer:
    def serialize(self, value: int) -> str:
        return str(value)

print(IntSerializer().serialize(42))
```

**Python equivalent**
Python approaches this concept with less ceremony: Protocols model behavior contracts by shape (duck typing) instead of explicit inheritance. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Protocols model behavior contracts by shape (duck typing) instead of explicit inheritance. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Protocols and structural typing` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Protocols and structural typing`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ok
- 42


### 25. Abstract base classes
Source: [src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_25_abstract_base_classes.py](src/csharp_to_python_learning/concepts/05_oop_and_modeling/topic_25_abstract_base_classes.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from collections.abc import Iterable

class CsvLike:
    def __iter__(self):
        yield from ["a,b", "c,d"]

print(isinstance(CsvLike(), Iterable))
```

**Python equivalent**
Python approaches this concept with less ceremony: ABCs define explicit contracts and can also provide reusable default behavior. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
ABCs define explicit contracts and can also provide reusable default behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Abstract base classes` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Abstract base classes`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- value:x
- True


### 26. Type hints
Source: [src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_26_type_hints.py](src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_26_type_hints.py)

**What C# developers usually expect**
C# developers usually expect compile-time type contracts and explicit interfaces.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from typing import TypedDict

class Config(TypedDict):
    retries: int
    timeout: float

config: Config = {"retries": 3, "timeout": 1.5}
print(config["retries"])
```

**Python equivalent**
Python approaches this concept with less ceremony: Type hints improve readability and tooling without changing runtime behavior. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Type hints improve readability and tooling without changing runtime behavior. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Type hints` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Type hints`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ['Nikhil', 'Priya']
- 3


### 27. Generics
Source: [src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_27_generics.py](src/csharp_to_python_learning/concepts/06_typing_and_protocols/topic_27_generics.py)

**What C# developers usually expect**
C# developers usually expect compile-time type contracts and explicit interfaces.

**C# example**
```csharp
public sealed class Box<T>
{
    public T Value { get; }
    public Box(T value) => Value = value;
}
```

**Advanced Python example from this file**
```python
from typing import TypeVar

U = TypeVar("U")

def first(items: list[U]) -> U:
    return items[0]

print(first(["a", "b", "c"]))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python generics are type-checker friendly and map closely to C# generic classes and methods. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python generics are type-checker friendly and map closely to C# generic classes and methods. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Generics` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Generics`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 10
- a


### 28. Pattern matching
Source: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_28_pattern_matching.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_28_pattern_matching.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
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
```

**Python equivalent**
Python approaches this concept with less ceremony: Structural pattern matching is Python's expressive branching feature for tuple/list/dict/object shapes. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Structural pattern matching is Python's expressive branching feature for tuple/list/dict/object shapes. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Pattern matching` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Pattern matching`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- positive
- large-upload


### 29. Dunder methods and Python data model
Source: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_29_dunder_methods_and_data_model.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_29_dunder_methods_and_data_model.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
class Vector:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))
```

**Python equivalent**
Python approaches this concept with less ceremony: Python objects participate in language syntax by implementing special (dunder) methods. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python objects participate in language syntax by implementing special (dunder) methods. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Dunder methods and Python data model` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Dunder methods and Python data model`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 3
- Vector(4, 6)


### 30. Descriptors
Source: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_30_descriptors.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_30_descriptors.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
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
```

**Python equivalent**
Python approaches this concept with less ceremony: Descriptors power `property`, ORM fields, and validation by intercepting attribute access at class level. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Descriptors power `property`, ORM fields, and validation by intercepting attribute access at class level. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Descriptors` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Descriptors`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 5
- read level=senior


### 31. Metaclasses
Source: [src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_31_metaclasses.py](src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_31_metaclasses.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
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
```

**Python equivalent**
Python approaches this concept with less ceremony: Metaclasses customize class creation and are useful for registries and framework hooks. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Metaclasses customize class creation and are useful for registries and framework hooks. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Metaclasses` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Metaclasses`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 1.0
- ['CsvPlugin']


### 32. Async and await
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_32_async_and_await.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_32_async_and_await.py)

**What C# developers usually expect**
C# developers usually expect `Task`-centric async flows, explicit cancellation tokens, and thread-pool awareness.

**C# example**
```csharp
static async Task<string> FetchAsync()
{
    await Task.Delay(10);
    return "done";
}
```

**Advanced Python example from this file**
```python
import asyncio

async def fetch(label: str, delay: float):
    await asyncio.sleep(delay)
    return label

async def main_async():
    result = await asyncio.gather(fetch("a", 0.01), fetch("b", 0.01))
    print(result)

asyncio.run(main_async())
```

**Python equivalent**
Python approaches this concept with less ceremony: Async functions represent suspendable workflows; use them for I/O concurrency, not CPU parallelism. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Async functions represent suspendable workflows; use them for I/O concurrency, not CPU parallelism. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Async and await` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Async and await`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- done
- ['a', 'b']


### 33. asyncio tasks, queues, cancellation, timeouts
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_33_asyncio_tasks_queues_cancellation_timeouts.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_33_asyncio_tasks_queues_cancellation_timeouts.py)

**What C# developers usually expect**
C# developers usually expect `Task`-centric async flows, explicit cancellation tokens, and thread-pool awareness.

**C# example**
```csharp
static async Task<string> FetchAsync()
{
    await Task.Delay(10);
    return "done";
}
```

**Advanced Python example from this file**
```python
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
```

**Python equivalent**
Python approaches this concept with less ceremony: Production asyncio code needs task orchestration, cancellation handling, queues, and timeout guards. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Production asyncio code needs task orchestration, cancellation handling, queues, and timeout guards. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `asyncio tasks, queues, cancellation, timeouts` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `asyncio tasks, queues, cancellation, timeouts`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- consumed 1
- timed out


### 34. Threading
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_34_threading.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_34_threading.py)

**What C# developers usually expect**
C# developers usually expect `Task`-centric async flows, explicit cancellation tokens, and thread-pool awareness.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from concurrent.futures import ThreadPoolExecutor

def upper(text: str) -> str:
    return text.upper()

with ThreadPoolExecutor(max_workers=2) as pool:
    print(list(pool.map(upper, ["a", "b", "c"])))
```

**Python equivalent**
Python approaches this concept with less ceremony: Threading works well for blocking I/O integration, protected with locks for shared mutable state. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Threading works well for blocking I/O integration, protected with locks for shared mutable state. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Threading` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Threading`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 2000
- ['A', 'B', 'C']


### 35. Multiprocessing
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_35_multiprocessing.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_35_multiprocessing.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
queue: Queue[int] = Queue()
process = Process(target=_publish_answer, args=(queue,))
process.start()
process.join()
print(queue.get())
```

**Python equivalent**
Python approaches this concept with less ceremony: Use multiprocessing for CPU-bound work when threads are limited by interpreter-level contention. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Use multiprocessing for CPU-bound work when threads are limited by interpreter-level contention. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Multiprocessing` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Multiprocessing`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [1, 4, 9]
- 42


### 36. File I/O
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_36_file_io.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_36_file_io.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as directory:
    path = Path(directory) / "data.log"
    with path.open("w", encoding="utf-8") as file:
        for index in range(3):
            file.write(f"line-{index}\n")
    print(path.read_text(encoding="utf-8").strip().splitlines()[-1])
```

**Python equivalent**
Python approaches this concept with less ceremony: Prefer explicit encodings and context managers for reliable file handling in production. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Prefer explicit encodings and context managers for reliable file handling in production. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `File I/O` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `File I/O`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- hello
- line-2


### 37. pathlib
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_37_pathlib.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_37_pathlib.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from pathlib import Path

python_files = list(Path("src").rglob("*.py"))
print(len(python_files) > 0)
```

**Python equivalent**
Python approaches this concept with less ceremony: `pathlib` gives object-oriented filesystem handling and replaces brittle string-based path logic. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
`pathlib` gives object-oriented filesystem handling and replaces brittle string-based path logic. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `pathlib` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `pathlib`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- src csharp_to_python_learning
- True


### 38. JSON, CSV, TOML
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_38_json_csv_toml.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_38_json_csv_toml.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import csv
import io
import tomllib

buffer = io.StringIO("name,score\nA,90\n")
rows = list(csv.DictReader(buffer))
parsed = tomllib.loads("tool = { name = 'uv' }")
print(rows[0]["score"], parsed["tool"]["name"])
```

**Python equivalent**
Python approaches this concept with less ceremony: Python's standard library handles core data formats without external dependencies. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python's standard library handles core data formats without external dependencies. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `JSON, CSV, TOML` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `JSON, CSV, TOML`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- nikhil
- 90 uv


### 39. Logging
Source: [src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_39_logging.py](src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_39_logging.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import logging

logger = logging.getLogger("billing")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(name)s %(levelname)s %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.WARNING)
logger.warning("quota low")
```

**Python equivalent**
Python approaches this concept with less ceremony: Structured, leveled logging is the production replacement for `print` debugging. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Structured, leveled logging is the production replacement for `print` debugging. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Logging` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Logging`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- INFO service started
- billing WARNING quota low


### 40. Testing with pytest
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_40_testing_with_pytest.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_40_testing_with_pytest.py)

**What C# developers usually expect**
C# developers usually expect xUnit/NUnit style tests and dedicated mocking frameworks.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
cases = [(2, 2, 4), (5, 7, 12)]
results = [left + right == expected for left, right, expected in cases]
print(all(results))
```

**Python equivalent**
Python approaches this concept with less ceremony: `pytest` favors simple functions and powerful assertions for fast test feedback. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
`pytest` favors simple functions and powerful assertions for fast test feedback. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Testing with pytest` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Testing with pytest`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- True


### 41. Mocking
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_41_mocking.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_41_mocking.py)

**What C# developers usually expect**
C# developers usually expect xUnit/NUnit style tests and dedicated mocking frameworks.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import asyncio
from unittest.mock import AsyncMock

async def main_async():
    sender = AsyncMock(return_value="sent")
    print(await sender())

asyncio.run(main_async())
```

**Python equivalent**
Python approaches this concept with less ceremony: Use `unittest.mock` to isolate collaborators, side effects, and network boundaries. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Use `unittest.mock` to isolate collaborators, side effects, and network boundaries. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Mocking` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Mocking`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- sent


### 42. Debugging
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_42_debugging.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_42_debugging.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import traceback

def fail():
    raise RuntimeError("boom")

try:
    fail()
except RuntimeError:
    text = traceback.format_exc().splitlines()[-1]
    print(text)
```

**Python equivalent**
Python approaches this concept with less ceremony: Combine debugger breakpoints, targeted logging, and tracebacks for efficient incident triage. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Combine debugger breakpoints, targeted logging, and tracebacks for efficient incident triage. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Debugging` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Debugging`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- ZeroDivisionError
- RuntimeError: boom


### 43. Packaging
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_43_packaging.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_43_packaging.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
build_steps = ["uv sync", "uv run -m pytest", "uv build"]
print(" -> ".join(build_steps))
```

**Python equivalent**
Python approaches this concept with less ceremony: Packaging turns source code into installable artifacts with metadata and entry points. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Packaging turns source code into installable artifacts with metadata and entry points. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Packaging` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Packaging`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- csharp-to-python-learning
- uv sync -> uv run -m pytest -> uv build


### 44. Dependency management
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_44_dependency_management.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_44_dependency_management.py)

**What C# developers usually expect**
C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
groups = {"runtime": ["httpx"], "dev": ["pytest", "ruff", "mypy"]}
print(sorted(groups["dev"]))
```

**Python equivalent**
Python approaches this concept with less ceremony: Pin dependencies and commit lock files for deterministic builds across machines and CI. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Pin dependencies and commit lock files for deterministic builds across machines and CI. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Dependency management` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Dependency management`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 2
- ['mypy', 'pytest', 'ruff']


### 45. Virtual environments
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_45_virtual_environments.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_45_virtual_environments.py)

**What C# developers usually expect**
C# developers usually expect NuGet + csproj tooling and deterministic restore/build steps.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import sys

venv_hint = ".venv" if sys.prefix != sys.base_prefix else "no-active-venv"
print(venv_hint)
```

**Python equivalent**
Python approaches this concept with less ceremony: Virtual environments isolate interpreter and package state per project, similar to per-solution toolchains. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Virtual environments isolate interpreter and package state per project, similar to per-solution toolchains. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Virtual environments` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Virtual environments`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- False
- no-active-venv


### 46. Linters and formatters
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_46_linters_and_formatters.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_46_linters_and_formatters.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
quality_gate = {"lint": "ruff check", "format": "ruff format", "types": "mypy src"}
print(" | ".join(f"{k}:{v}" for k, v in quality_gate.items()))
```

**Python equivalent**
Python approaches this concept with less ceremony: Ruff can handle linting and formatting quickly, replacing multiple separate tools in many projects. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Ruff can handle linting and formatting quickly, replacing multiple separate tools in many projects. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Linters and formatters` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Linters and formatters`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- use: uv run ruff check .
- lint:ruff check


### 47. Performance and profiling
Source: [src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_47_performance_and_profiling.py](src/csharp_to_python_learning/concepts/09_quality_and_tooling/topic_47_performance_and_profiling.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import cProfile
import io
import pstats

profile = cProfile.Profile()
profile.enable()
sum(range(20_000))
profile.disable()
stream = io.StringIO()
pstats.Stats(profile, stream=stream).sort_stats("cumulative").print_stats(1)
print("function calls" in stream.getvalue())
```

**Python equivalent**
Python approaches this concept with less ceremony: Measure before optimizing: combine `timeit`, `cProfile`, and algorithmic changes. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Measure before optimizing: combine `timeit`, `cProfile`, and algorithmic changes. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Performance and profiling` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Performance and profiling`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- True


### 48. Memory management and garbage collection
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_48_memory_management_and_gc.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_48_memory_management_and_gc.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import weakref

class Resource:
    pass

resource = Resource()
finalizer = weakref.finalize(resource, print, "resource finalized")
del resource
print(finalizer.alive in {True, False})
```

**Python equivalent**
Python approaches this concept with less ceremony: CPython uses reference counting plus cyclic GC; lifecycle choices affect latency and memory pressure. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
CPython uses reference counting plus cyclic GC; lifecycle choices affect latency and memory pressure. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Memory management and garbage collection` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Memory management and garbage collection`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- True
- True


### 49. Standard library overview
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_49_standard_library_overview.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_49_standard_library_overview.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from itertools import pairwise

pairs = list(pairwise([1, 2, 3, 4]))
print(pairs[-1])
```

**Python equivalent**
Python approaches this concept with less ceremony: The standard library covers many production needs: paths, JSON, CLI parsing, concurrency, testing, and more. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
The standard library covers many production needs: paths, JSON, CLI parsing, concurrency, testing, and more. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Standard library overview` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Standard library overview`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- 23.33
- (3, 4)


### 50. Python 3.14-specific features
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_50_python_3_14_specific_features.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_50_python_3_14_specific_features.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
import importlib.util

features = {
    "annotationlib": importlib.util.find_spec("annotationlib") is not None,
    "compression.zstd": importlib.util.find_spec("compression.zstd") is not None,
}
print(features)
```

**Python equivalent**
Python approaches this concept with less ceremony: Python 3.14 adds deferred annotation behavior and stronger support for free-threaded execution. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Python 3.14 adds deferred annotation behavior and stronger support for free-threaded execution. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Python 3.14-specific features` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Python 3.14-specific features`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- Nikhil
- {'annotationlib':


### 51. Python idioms versus C# idioms
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_51_python_idioms_vs_csharp_idioms.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_51_python_idioms_vs_csharp_idioms.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
from typing import TypedDict

class ScoreRecord(TypedDict):
    name: str
    score: int

records: list[ScoreRecord] = [{"name": "a", "score": 10}, {"name": "b", "score": 7}]
best = max(records, key=lambda r: r["score"])
print(best["name"])
```

**Python equivalent**
Python approaches this concept with less ceremony: Translate intent, not syntax: many C# patterns have shorter Pythonic forms. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Translate intent, not syntax: many C# patterns have shorter Pythonic forms. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Python idioms versus C# idioms` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Python idioms versus C# idioms`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [2, 4]
- a


### 52. Common C# to Python migration mistakes
Source: [src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_52_common_csharp_to_python_migration_mistakes.py](src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_52_common_csharp_to_python_migration_mistakes.py)

**What C# developers usually expect**
C# developers usually expect explicit type declarations, predictable object lifetimes, and compile-time guidance.

**C# example**
```csharp
var values = new[] { 1, 2, 3 };
Console.WriteLine(values.Length);
```

**Advanced Python example from this file**
```python
def append_good(item, bucket=None):
    bucket = [] if bucket is None else bucket
    bucket.append(item)
    return bucket

print(append_good(1), append_good(2))
```

**Python equivalent**
Python approaches this concept with less ceremony: Most migration bugs come from mutability assumptions, import-time side effects, and overusing class-heavy designs. You still keep production discipline through tests, typing, and tooling.

**Detailed explanation for C# developers**
Most migration bugs come from mutability assumptions, import-time side effects, and overusing class-heavy designs. In practice, combine this with logging, tests, and type hints so the flexibility does not turn into ambiguity. Prefer small functions, clear data boundaries, and explicit contracts where behavior matters.

**Common mistakes for C# developers**
1. Assuming C# defaults apply directly in `Common C# to Python migration mistakes` without checking Python runtime behavior.
2. Skipping tests because dynamic code feels simpler at first; regressions grow quickly without guardrails.

**Exercises**
1. Rewrite one recent C# snippet in Python using this concept: `Common C# to Python migration mistakes`.
2. Add input validation, type hints, and one `pytest` test for the rewritten snippet.

**Expected output**
- [1, 2]
- [1] [2]


### 53. Async iteration, async generators, and async context managers
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_53_async_iteration_and_async_context_managers.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_53_async_iteration_and_async_context_managers.py)

**What C# developers usually expect**
C# developers usually expect `await foreach` and `await using` for asynchronous streaming and cleanup.

**C# example**
```csharp
await foreach (var item in ReadAsync())
{
    Console.WriteLine(item);
}
```

**Advanced Python example from this file**
```python
pass
```

**Python equivalent**
Python uses `async for`, async generators, async comprehensions, and `async with` to model the same patterns.

**Detailed explanation for C# developers**
Use `async for` when values arrive over time, and `async with` when setup/cleanup must also await I/O.

**Common mistakes for C# developers**
1. Treating async generators like regular lists.
2. Forgetting that async context managers require `async with`, not `with`.

**Exercises**
1. Convert a synchronous generator pipeline to an async pipeline.
2. Add timing logs with an async context manager.

**Expected output**
- enter:pipeline
- squares:[0, 1, 4]


### 54. Exception groups and `except*`
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_54_exception_groups_and_except_star.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_54_exception_groups_and_except_star.py)

**What C# developers usually expect**
C# developers usually expect one exception instance per `catch` flow.

**C# example**
```csharp
try { Run(); }
catch (ValidationException ex) { ... }
catch (TimeoutException ex) { ... }
```

**Advanced Python example from this file**
```python
try:
    raise ExceptionGroup(
        "task errors",
        [RuntimeError("retry"), TimeoutError("slow endpoint"), RuntimeError("retry again")],
    )
except* RuntimeError as group:
    messages = [str(item) for item in group.exceptions]
    print(f"runtime branch: {messages}")
except* TimeoutError as group:
    print(f"timeouts: {len(group.exceptions)}")
```

**Python equivalent**
Python can raise multiple failures together with `ExceptionGroup` and handle each subtype with `except*`.

**Detailed explanation for C# developers**
This is useful in concurrent code where multiple tasks fail and you need partial handling.

**Common mistakes for C# developers**
1. Using plain `except` when `except*` is required.
2. Assuming one handler consumes the full grouped failure.

**Exercises**
1. Build an `ExceptionGroup` with three exception types and handle each branch.
2. Re-raise unhandled branches and log them separately.

**Expected output**
- value errors: 1
- type errors: 1


### 55. Assignment expressions (`:=`)
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_55_assignment_expressions.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_55_assignment_expressions.py)

**What C# developers usually expect**
C# developers usually declare a variable before condition checks.

**C# example**
```csharp
var size = items.Count;
if (size > 2) { Console.WriteLine(size); }
```

**Advanced Python example from this file**
```python
raw = [" A ", " ", "B", "", " C"]
cleaned = [item for raw_item in raw if (item := raw_item.strip())]
print(cleaned)
```

**Python equivalent**
Python's walrus operator (`:=`) allows assignment inside expressions when it improves clarity.

**Detailed explanation for C# developers**
Use this feature sparingly for readable pipelines, loop conditions, and lightweight parsing.

**Common mistakes for C# developers**
1. Overusing walrus in dense expressions.
2. Hiding important state changes inside nested conditions.

**Exercises**
1. Refactor one parsing loop to use a single walrus assignment.
2. Compare readability with and without walrus in a code review.

**Expected output**
- size:4
- ['A', 'B', 'C']


### 56. Binary data: `bytes`, `bytearray`, and `memoryview`
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_56_binary_data_bytes_bytearray_memoryview.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_56_binary_data_bytes_bytearray_memoryview.py)

**What C# developers usually expect**
C# developers usually work with `byte[]`, `Span<T>`, and buffer slices.

**C# example**
```csharp
byte[] payload = Encoding.UTF8.GetBytes("hello");
```

**Advanced Python example from this file**
```python
buffer = bytearray(b"abcde")
view = memoryview(buffer)
view[1:4] = b"XYZ"
print(buffer.decode("ascii"))
```

**Python equivalent**
Python provides immutable `bytes`, mutable `bytearray`, and zero-copy `memoryview`.

**Detailed explanation for C# developers**
Use `memoryview` for high-throughput transformations where copies are expensive.

**Common mistakes for C# developers**
1. Mutating `bytes` (immutable).
2. Copying buffers when a view is enough.

**Exercises**
1. Parse a binary header with `memoryview`.
2. Benchmark slice-copy vs. slice-view on a larger payload.

**Expected output**
- 68656c6c6f
- aXYZe


### 57. Advanced typing: `ParamSpec`, `TypeVarTuple`, `Literal`, `Annotated`, `Self`
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_57_advanced_typing_paramspec_typevartuple_and_more.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_57_advanced_typing_paramspec_typevartuple_and_more.py)

**What C# developers usually expect**
C# developers usually expect compile-time generic metadata and fluent APIs with strong type flow.

**C# example**
```csharp
public TOut Wrap<TIn, TOut>(Func<TIn, TOut> func) => ...
```

**Advanced Python example from this file**
```python
row = Row[int, str](10, "ok")
print(f"row:{row.values}")
query = Query().where("status").where("region")
print(f"filters:{query.filters}")
print(fetch("safe", 443))
```

**Python equivalent**
Python typing can express callable signatures (`ParamSpec`), variadic generic shapes (`TypeVarTuple`), value-level modes (`Literal`), metadata (`Annotated`), and fluent `Self`.

**Detailed explanation for C# developers**
These hints improve editor accuracy, API contracts, and static checks without changing runtime semantics.

**Common mistakes for C# developers**
1. Expecting type hints to enforce runtime behavior automatically.
2. Ignoring value-level contracts where `Literal` improves safety.

**Exercises**
1. Convert one decorator-heavy helper to use `ParamSpec`.
2. Add `Literal` modes to one public API.

**Expected output**
- traced:add
- row:(10, 'ok')


### 58. `__slots__` as a language feature
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_58_slots_as_a_language_feature.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_58_slots_as_a_language_feature.py)

**What C# developers usually expect**
C# developers usually expect object field layout to be explicit and stable.

**C# example**
```csharp
public sealed class Point { public int X; public int Y; }
```

**Advanced Python example from this file**
```python
event = Event(event_id=101, priority=2)
print(f"slot dataclass:{event.priority}")
```

**Python equivalent**
`__slots__` restricts dynamic attribute creation and can reduce per-instance memory overhead.

**Detailed explanation for C# developers**
Use slots in hot paths with many short-lived objects, but avoid them when dynamic attributes are required.

**Common mistakes for C# developers**
1. Assuming slots make objects immutable.
2. Adding dynamic fields to slotted classes without planning.

**Exercises**
1. Convert one high-volume model to slots and benchmark memory.
2. Decide where slots hurt flexibility in your codebase.

**Expected output**
- has __dict__:False
- slot dataclass:2


### 59. Import hooks: custom finders and loaders
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_59_import_hooks_custom_finders_and_loaders.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_59_import_hooks_custom_finders_and_loaders.py)

**What C# developers usually expect**
C# developers usually expect assembly loading to be mostly static at startup.

**C# example**
```csharp
var assembly = Assembly.Load("Plugin");
```

**Advanced Python example from this file**
```python
module = run_with_hook("hooked_config", {"hooked_config": {"settings": {"mode": "safe"}}})
print(f"hooked settings:{module.settings}")
```

**Python equivalent**
Python's import system is programmable through `sys.meta_path` with custom finder and loader objects.

**Detailed explanation for C# developers**
Import hooks are useful for plugin systems, generated modules, and advanced testing seams.

**Common mistakes for C# developers**
1. Forgetting to clean up `sys.meta_path` after temporary hooks.
2. Leaving generated modules in `sys.modules` across tests.

**Exercises**
1. Build a small plugin loader that resolves modules from a dictionary.
2. Add tests that isolate import hook side effects.

**Expected output**
- hooked value:42
- hooked settings:{'mode': 'safe'}


### 60. `contextvars` and task-local state
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_60_contextvars_and_task_local_state.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_60_contextvars_and_task_local_state.py)

**What C# developers usually expect**
C# developers usually expect `AsyncLocal<T>` style correlation IDs across async call chains.

**C# example**
```csharp
AsyncLocal<string> RequestId = new();
```

**Advanced Python example from this file**
```python
pass
```

**Python equivalent**
Python uses `contextvars.ContextVar` to carry per-task request context safely in async workflows.

**Detailed explanation for C# developers**
Use `contextvars` for trace IDs, tenant IDs, and auth context when concurrent tasks share execution threads.

**Common mistakes for C# developers**
1. Storing request state in global variables.
2. Assuming normal module globals are task-isolated.

**Exercises**
1. Add a request-id context var to one async pipeline.
2. Propagate context into logging formatters.

**Expected output**
- req:sync-1
- ['task-a', 'task-b']


### 61. Weak references and finalization patterns
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_61_weakref_and_finalization_patterns.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_61_weakref_and_finalization_patterns.py)

**What C# developers usually expect**
C# developers usually expect GC-managed objects with explicit disposal for critical resources.

**C# example**
```csharp
var cache = new ConditionalWeakTable<object, Metadata>();
```

**Advanced Python example from this file**
```python
events: list[str] = []
payload = Payload(7)
weakref.finalize(payload, events.append, "finalized")
del payload
gc.collect()
print(f"finalized event:{events == ['finalized']}")
```

**Python equivalent**
Python provides `weakref` containers and `weakref.finalize` for non-owning references and cleanup callbacks.

**Detailed explanation for C# developers**
Weak references help avoid cache-induced leaks and can trigger cleanup hooks when objects are collected.

**Common mistakes for C# developers**
1. Assuming weak references keep objects alive.
2. Depending on exact GC timing for business logic.

**Exercises**
1. Replace a strong-reference cache with `WeakValueDictionary`.
2. Add diagnostics around object lifecycle transitions.

**Expected output**
- cache alive:True
- cache alive after gc:False


### 62. Advanced descriptor and metaclass patterns
Source: [src/csharp_to_python_learning/concepts/11_additional_language_features/topic_62_advanced_descriptor_and_metaclass_patterns.py](src/csharp_to_python_learning/concepts/11_additional_language_features/topic_62_advanced_descriptor_and_metaclass_patterns.py)

**What C# developers usually expect**
C# developers usually expect validation and model registration through attributes, base classes, or DI containers.

**C# example**
```csharp
[Required]
public string Name { get; set; } = "";
```

**Advanced Python example from this file**
```python
print(f"fields:{Account.__fields__}")
print(f"registry:{sorted(ModelMeta.registry)}")
```

**Python equivalent**
Python can enforce field rules with descriptors and auto-register model classes with metaclasses.

**Detailed explanation for C# developers**
Descriptors centralize reusable field behavior; metaclasses automate class-time metadata and registration.

**Common mistakes for C# developers**
1. Putting too much business logic in metaclasses.
2. Forgetting that descriptor validation runs at assignment time.

**Exercises**
1. Add an integer range descriptor and apply it to two models.
2. Build a mini plugin registry with metaclass-based discovery.

**Expected output**
- user:Nikhil
- fields:['name', 'owner']

<!-- ADVANCED_WALKTHROUGH_END -->

## Python-Only Features
- [feature_01_duck_typing_and_protocols.py](src/csharp_to_python_learning/python_only_features/feature_01_duck_typing_and_protocols.py): runnable Python-only feature example.
- [feature_02_extended_unpacking.py](src/csharp_to_python_learning/python_only_features/feature_02_extended_unpacking.py): runnable Python-only feature example.
- [feature_03_generator_pipelines.py](src/csharp_to_python_learning/python_only_features/feature_03_generator_pipelines.py): runnable Python-only feature example.
- [feature_04_contextlib_magic.py](src/csharp_to_python_learning/python_only_features/feature_04_contextlib_magic.py): runnable Python-only feature example.
- [feature_05_descriptors.py](src/csharp_to_python_learning/python_only_features/feature_05_descriptors.py): runnable Python-only feature example.
- [feature_06_pattern_matching.py](src/csharp_to_python_learning/python_only_features/feature_06_pattern_matching.py): runnable Python-only feature example.
- [feature_07_metaclass_registry.py](src/csharp_to_python_learning/python_only_features/feature_07_metaclass_registry.py): runnable Python-only feature example.
- [capstone_async_event_pipeline.py](src/csharp_to_python_learning/capstone/capstone_async_event_pipeline.py): runnable Python-only feature example.

## C# Features With No Direct Python Equivalent
- Reified generics at runtime with CLR metadata behavior.
- Method overloading resolution by compile-time signature.
- `ref`, `out`, and unsafe pointer patterns as first-class language features.
- Attribute-driven compile-time/source-generator ecosystems.
- Value types (`struct`) with stack semantics equivalent to .NET.

## Python Features With No Direct C# Equivalent
- Runtime monkey-patching of modules/classes/functions.
- Descriptors as first-class attribute access primitives.
- Structural pattern matching with heterogeneous shape patterns.
- Context manager protocol (`with`) as a language-level resource hook.
- Rich dunder protocol for integrating with core syntax at runtime.
- Metaclass-driven class construction customization.
- Extended iterable unpacking in assignments and function calls.

## 1-Week Study Plan
1. **Day 1**: Setup + execution model + names/references/mutability + primitive types.  
   Practice: run topics 1-4 and rewrite one .NET utility script in Python.
2. **Day 2**: Collections, slicing/unpacking, control flow, functions, defaults, lambdas.  
   Practice: port a LINQ-heavy method to comprehensions and generator pipelines.
3. **Day 3**: Closures, decorators, iterators/generators, context managers, exceptions.  
   Practice: wrap an I/O workflow with proper context managers and exception boundaries.
4. **Day 4**: Modules, imports, OOP, dataclasses, enums, properties, composition.  
   Practice: model a domain object set with dataclasses and validation.
5. **Day 5**: Typing, protocols, ABCs, generics, pattern matching, data model, descriptors/metaclasses.  
   Practice: introduce protocols and static typing to an existing Python script.
6. **Day 6**: Asyncio, threading, multiprocessing, file/path/data formats, logging.  
   Practice: build a small concurrent ingestion script with structured logging.
7. **Day 7**: Testing/mocking/debugging, packaging/tooling, profiling/memory, migration pitfalls, capstone.  
   Practice: complete capstone and add tests + lint + type checks.

## Capstone Project
Run the capstone:
```bash
uv run src/csharp_to_python_learning/capstone/capstone_async_event_pipeline.py
```
Capstone combines:
- dataclasses
- protocols/typing
- asyncio queues/tasks
- transformation pipeline patterns
- logging
- deterministic summary output

## Further Study
- Official Python docs for 3.14 language/runtime updates.
- `asyncio` internals and cancellation design patterns.
- Advanced typing (`TypeVarTuple`, `ParamSpec`, plugin/tooling ecosystems).
- Packaging and release automation for internal Python platforms.
