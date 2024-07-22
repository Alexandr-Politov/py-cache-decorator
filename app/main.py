from typing import Callable


def cache(func: Callable) -> Callable:

    results_storage = {}

    def inner_checker(*args) -> str:

        if args in results_storage:
            print("Getting from cache")
            return results_storage[args]
        else:
            print("Calculating new result")
            results_storage[key] = func(*args)
        return results_storage[key]

    return inner_checker
