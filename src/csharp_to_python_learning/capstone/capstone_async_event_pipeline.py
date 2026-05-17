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
