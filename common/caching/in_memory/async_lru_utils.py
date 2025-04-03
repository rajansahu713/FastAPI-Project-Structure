from typing import Callable, Dict, Optional

from async_lru import alru_cache

# Global registry to keep track of all cached functions
_cached_functions: Dict[str, Callable] = {}


def async_lru_cache(maxsize: int = 128, ttl: Optional[float] = None):
    """
    A simple decorator that applies async LRU caching if enabled via environment variable.

    Usage:
        @insight_cache(maxsize=100, ttl=60)
        async def my_function(param):
            # function implementation

    Enable/disable via environment variable ENABLE_CACHE=true/false
    """

    def decorator(func: Callable) -> Callable:
        cache_enabled = True

        # Generate a unique key for this function
        func_key = f"{func.__module__}.{func.__qualname__}"

        if cache_enabled:
            cached_func = alru_cache(maxsize=maxsize, ttl=ttl)(func)

            # Register the cached function for later access
            _cached_functions[func_key] = cached_func
            print("_cached_functions \n\n", _cached_functions)
            return cached_func
        return func

    return decorator


def clear_all_cache():
    """
    Clear the cache for a specific function or all cached functions.

    Usage:
        # Clear cache for a specific function
        clear_cache(my_function)

        # Clear all caches
        clear_cache()
    """
    for cached_func in _cached_functions.values():
        if hasattr(cached_func, "cache_clear"):
            cached_func.cache_clear()
    return {"message": "All caches cleared"}


def clear_cache_by_names(function_names: list):
    """
    Clear the cache for specific functions by their names.

    Args:
        function_names: List of function names (can be partial matches)

    Returns:
        Dict with results of the clearing operation
    """
    results = {}

    for func_name in function_names:
        found = False
        for func_key, cached_func in _cached_functions.items():
            # Check if the provided name is in the function key
            if func_name in func_key and hasattr(cached_func, "cache_clear"):
                cached_func.cache_clear()
                results[func_key] = "Cache cleared"
                found = True

        if not found:
            results[func_name] = "No matching function found"

    return {"results": results}
