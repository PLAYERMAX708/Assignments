try:
    from a03 import sqrt, average, improve_guess
except:
    pass

epsilon = 1e-4 # precision needed

#         __________________________________________


    # this is the only test that is failed and not solved by me
def test_improve_guess_zero():
    n = 1e-7
    g = 0
    res = improve_guess(g, n)
    assert abs(res - 5.000000005) < epsilon


#         __________________________________________

    # all these tests are correct and passed
def test_improve_guess():
    n = 54
    g = 7.0 # haven't discussed casting yet. So, need to send at least one float
    # no need in python v3 
    
    res = improve_guess(g, n)
    assert abs(res - 7.3571) < epsilon

def test_improve_guess_2():
    # this one is for a student who can handle extremely bad cases.
    # It CAN be done given the content we have covered already!
    n = 54
    g = 7
    res = improve_guess(g, n)
    assert abs(res - 7.3571) < epsilon

def test_improve_guess_2_dup():
    # dup to increase weightage 
    n = 54
    g = 7
    res = improve_guess(g, n)
    assert abs(res - 7.3571) < epsilon

def test_sqrt_int():
    v = 674
    assert abs(sqrt(v) - 25.9615) < epsilon


# output capturing decorator
def capture_output(fn):
    def wrapper(*args, **kwargs):
        import io
        import sys
        orig_stdout = sys.stdout
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        v = fn(*args, **kwargs)

        sys.stdout = orig_stdout # don't rely on __stdout__

        # print 'Captured', capturedOutput.getvalue()
        output_val = capturedOutput.getvalue()
        return v, output_val

    return wrapper
