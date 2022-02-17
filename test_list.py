import pytest


@pytest.fixture
def mock_list():
    return [-100, -1, 0, 1, 100]


def test_item_get(mock_list):
    """Check that __getitem__ can manage indexes and return a right value."""
    assert mock_list[0] == -100, "Element doesn't exist or has a wrong value!"
    with pytest.raises(IndexError):
        assert mock_list[
            100
        ], "Expected an IndexError to be raised for unexisted element."
    assert mock_list[-1] == 100, "Unsupported negative indexing."


def test_append(mock_list):
    """Check that append command adds an item to the end of a list."""
    # Initial list size.
    LIST_SIZE = len(mock_list)
    element = 1
    mock_list.append(element)
    assert len(mock_list) == LIST_SIZE + 1, "Error append int to list!"
    assert mock_list[-1] == element, "A new element should be the last in the list!"


def test_remove(mock_list):
    """Check that remove() deletes the first item from the list whose value is
    equal to the element."""
    # Initial list size.
    LIST_SIZE = len(mock_list)
    element = 0
    # Number of elements equals to `element`.
    COUNT_ELEMENTS = sum(1 for _ in filter(lambda x: x == element, mock_list))
    mock_list.remove(element)

    assert (
        len(mock_list) == LIST_SIZE - 1
    ), "A list length should decrease after item remove."

    found_elements = sum(1 for _ in filter(lambda x: x == element, mock_list))
    assert (
        COUNT_ELEMENTS == found_elements + 1
    ), f"An element {element} was not removed."
