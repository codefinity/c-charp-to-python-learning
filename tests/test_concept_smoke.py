from __future__ import annotations

import runpy
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_script(script: Path) -> None:
    runpy.run_path(str(script), run_name="__main__")


def test_selected_concepts_run_without_errors() -> None:
    scripts = [
        PROJECT_ROOT
        / "src/csharp_to_python_learning/concepts/01_setup_and_runtime/topic_01_python_project_setup_with_uv.py",
        PROJECT_ROOT
        / "src/csharp_to_python_learning/concepts/03_functions_and_functional_tools/topic_12_decorators.py",
        PROJECT_ROOT
        / "src/csharp_to_python_learning/concepts/07_advanced_language_runtime/topic_30_descriptors.py",
        PROJECT_ROOT
        / "src/csharp_to_python_learning/concepts/08_concurrency_and_systems/topic_33_asyncio_tasks_queues_cancellation_timeouts.py",
        PROJECT_ROOT
        / "src/csharp_to_python_learning/concepts/10_memory_idioms_migration/topic_50_python_3_14_specific_features.py",
    ]
    for script in scripts:
        run_script(script)


def test_python_only_examples_run_without_errors() -> None:
    feature_dir = PROJECT_ROOT / "src/csharp_to_python_learning/python_only_features"
    targets = sorted(feature_dir.glob("feature_*.py"))
    for script in targets:
        run_script(script)


def test_capstone_pipeline_runs_without_errors() -> None:
    script = (
        PROJECT_ROOT / "src/csharp_to_python_learning/capstone/capstone_async_event_pipeline.py"
    )
    run_script(script)

