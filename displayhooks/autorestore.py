import sys

if sys.version_info >= (3, 10):
    from typing import ParamSpec  # pragma: no cover
else:
    from typing_extensions import ParamSpec  # pragma: no cover

from functools import wraps
from typing import Callable, TypeVar

FunctionParameters = ParamSpec('FunctionParameters')
ReturningValue = TypeVar('ReturningValue')

def autorestore_displayhook(function: Callable[FunctionParameters, ReturningValue]) -> Callable[FunctionParameters, ReturningValue]:
    @wraps(function)
    def wrapper(*args: FunctionParameters.args, **kwargs: FunctionParameters.kwargs) -> ReturningValue:
        old_displayhook = sys.displayhook

        try:
            return function(*args, **kwargs)
        finally:
            sys.displayhook = old_displayhook

    return wrapper
