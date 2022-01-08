from dsa_utilities.stacks import stack
from dsa_utilities.stacks.stack import StackUnderflowError, StackOverflowError


def test_stacks():
    """Tests the implementation of stack
    """
    limit = 10
    int_stack = stack.Stack[int](limit)
    assert bool(int_stack) is False
    assert int_stack.is_empty() is True
    assert int_stack.is_full() is False
    assert str(int_stack) == "[]"

    try:
        int_stack.pop()
        assert False # This should not happen
    except StackUnderflowError:
        assert True # This should happen
    
    try:
        int_stack.peek()
        assert False # This should not happen
    except StackUnderflowError:
        assert True # This should happen
    
    for i in range(limit):
        assert int_stack.size() == i
        int_stack.push(i)
    
    assert bool(int_stack)
    assert not int_stack.is_empty()
    assert int_stack.is_full()
    assert str(int_stack) == str(list(range(10)))
    assert int_stack.pop() == 9
    assert int_stack.peek() == 8

    int_stack.push(100)
    assert str(int_stack) == str([0, 1, 2, 3, 4, 5, 6, 7, 8, 100])

    try:
        int_stack.push(200)
        assert False  # This should not happen
    except StackOverflowError:
        assert True  # This should happen

    assert not int_stack.is_empty()
    assert int_stack.size() == 10

    assert 5 in int_stack
    assert 55 not in int_stack
    


if __name__ == "__main__":
    test_stacks()

