from ctypes.wintypes import INT
import pytest


@pytest.fixture
def float1():
    return float(1)


@pytest.fixture
def float2():
    return float(1.999999999999999999999999999999999999999999999999)


@pytest.fixture
def float3():
    return 3.14e-2


def test_add_operator(float1, float2):
    """Test addition."""
    print(type(float1))
    assert (
        float1 + float2 == 2.999999999999999999999999999999999999999999999999
    ), "Failed to sum two floats."
    # Forcefully set variable to int.
    INT_ELEMENT = int(1)
    assert float1 + INT_ELEMENT == 2, "Failed to sum float and int!"
    with pytest.raises(TypeError):
        assert float1 + None


def test_sub_operator(float1, float2):
    """Test substraction."""
    print(type(float1))
    assert (
        float1 - float2 == -0.999999999999999999999999999999999999999999999999
    ), "Failed to substract two floats."
    # Forcefully set variable to int.
    INT_ELEMENT = int(1)
    assert float1 - INT_ELEMENT == 0, "Failed to substract float and int!"
    with pytest.raises(TypeError):
        assert float1 - None


def test_arithmetic_priority(float1, float3):
    """Test priority in arithmetic operations."""
    assert float3 * 10e3 + float1 == 315
    assert 3.0 * 2.0 ** 3 == 24
    assert (2.0 + 2.0) * 2 == 8
    assert 2.0 + 2.0 * 2 == 6
    # Floating point bottleneck.
    with pytest.raises(AssertionError):
        assert 0.1 + 0.2 == 0.3
