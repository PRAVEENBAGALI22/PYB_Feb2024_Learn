import pytest


# here are using skipping testcase to be not to executed in pytest
@pytest.mark.skip
def testLogin():
    print("Login Successful")


# here the test case is ready but the functionality is not ready, to have better report we skip this testcase deliberate
@pytest.mark.xfail
def testLogff():
    print("Logff Successful")


@pytest.mark.sanity
def testcalculation():
    assert 2 + 2 == 6

@pytest.mark.xfail
def testcalculation1():
    assert 2 + 2 == 6