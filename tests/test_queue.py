from dsa_utilities.queue import queue
from dsa_utilities.queue.queue import QueueUnderFlow, QueueOverFlow

def test_queue():
    limit = 10
    str_queue = queue.Queue[str](limit)
    assert bool(str_queue) is False
    assert str_queue.is_empty() is True
    assert str_queue.size() == 0

    try:
        str_queue.dequeue()
        assert False # This should not happen
    except QueueUnderFlow:
        assert True # This should happen
    
    str_queue.enqueue("Hello")
    str_queue.enqueue("Dog")
    assert str_queue.dequeue() == "Dog"
    assert str_queue.dequeue() == "Hello"
    assert str_queue.is_empty() == True
    
if __name__ == "__main__":
    test_queue()