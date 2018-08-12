import pytest
def test_a():
    print("test_a被执行...")
    assert 1
@pytest.mark.run(order=10)
def test_b():
    print("test_b被执行...")
    assert 0
if __name__ == '__main__':
    pytest.main()