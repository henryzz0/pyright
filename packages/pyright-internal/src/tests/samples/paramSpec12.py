# This sample tests various error conditions for ParamSpec usage.

from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")


def puts_p_into_scope(f: Callable[P, int]) -> None:
    def inner(*args: P.args, **kwargs: P.kwargs) -> None:
        pass

    # This should generate two errors because P.kwargs cannot be
    # used with *args and P.args cannot be used with **kwargs.
    def mixed_up(*args: P.kwargs, **kwargs: P.args) -> None:
        pass

    # This should generate an error because P.args cannot be used
    # with a simple parameter.
    def misplaced(x: P.args) -> None:
        pass

    # This should generate an error
    stored_args: P.args

    # This should generate an error
    stored_kwargs: P.kwargs

    # This should generate an error because P.args cannot be used
    # without P.kwargs.
    def just_args(*args: P.args) -> None:
        pass

    # This should generate an error because P.kwargs cannot be used
    # without P.args.
    def just_kwargs(**kwargs: P.kwargs) -> None:
        pass


# This should generate an error because P is not defined in this context.
def out_of_scope(*args: P.args, **kwargs: P.kwargs) -> None:
    pass

# This should generate an error because ParamSpec isn't allowed in this context
out_of_scope_var2: P = 12

# This should generate an error because P isn't allowed in this context.
out_of_scope_var3: P.args = 12
