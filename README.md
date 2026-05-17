# C# to Python: Advanced, Production-Ready Tutorial (Python 3.14.5 + uv)

## Who This Repository Is For
This repository is for experienced C#/.NET developers who already understand OOP, generics, LINQ, async/await, dependency injection, build tools, and testing.  
The goal is to help you become an advanced Python developer who can ship production-grade code confidently.

## Table of Contents
- [Who This Repository Is For](#who-this-repository-is-for)
- [Quick Start](#quick-start)
- [How To Use uv In This Project](#how-to-use-uv-in-this-project)
- [Tutorial Concepts](#tutorial-concepts)
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



