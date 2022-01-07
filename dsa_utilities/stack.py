"""
LIFO
"""
from typing import Generic, TypeVar

T = TypeVar("T")

class StackOverflowError(BaseException):
    pass

class StackUnderflowError(BaseException):
    pass

class Stack(Generic[T]):
    """Represents a stack data structure

    """
    def __init__(self, limit: int = 10):
        self.stack: list[T] = []
        self.limit = limit
    
    def push(self, item: T) -> None:
        """This method push an element to thee top of the stack."""
        if len(self.stack) >= self.limit:
            raise StackOverflowError
        self.stack.append(item)
    
    def pop(self) -> T:
        """Delete and return the last item of the stack."""
        if not self.stack:
            raise StackUnderflowError
        self.stack.pop()

    def peek(self) -> T:
        """Peek at the top most item of the stack."""
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]
