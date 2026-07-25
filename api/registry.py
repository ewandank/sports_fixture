import asyncio
from collections.abc import Callable
from typing import Any

from hishel.httpx import AsyncCacheClient
from ics.event import Event

from enums import Teams


class CalendarHandlerRegistry:
    def __init__(self):
        self._handlers: dict[Teams, Callable[[AsyncCacheClient], Any]] = {}

    def register(self, option: Teams):

        def decorator(func: Callable[[AsyncCacheClient], Any]):
            self._handlers[option] = func
            return func

        return decorator

    async def get_combined_data(
        self, active_mask: Teams, client: AsyncCacheClient
    ) -> list[Event]:
        # Pass the client instance into each matching task

        tasks = []

        for option, handler in self._handlers.items():
            if option in active_mask:
                task = handler(client)
                tasks.append(task)
        if not tasks:
            return []

        # Run all requests concurrently
        results = await asyncio.gather(*tasks)
        # Flatten list of lists
        return [item for sublist in results for item in sublist]


registry = CalendarHandlerRegistry()
register_option = registry.register
