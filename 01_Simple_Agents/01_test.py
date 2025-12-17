def test_factorial(factorial):
    # Test valid cases
    
    assert factorial(0) == 1, "factorial(0) failed: Expected 1"
    assert factorial(5) == 120, "factorial(5) failed: Expected 120"
    assert factorial(10) == 3_628_800, "factorial(10) failed: Expected 3,628,800"
    
    
    # Test invalid cases

    invalid_inputs = [-1, 2.5, "hello world!"]
    for inp in invalid_inputs:
        try:
            assert factorial(inp) == None, f"factorial({inp}) failed: Expected None"
        except:
            raise AssertionError(f"factorial({inp}) raise an error (must be None)")
    
    print("All tests passed!")

test_factorial(factorial)