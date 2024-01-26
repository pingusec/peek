import pytest
import subprocess

def pytest_namespace():
    return {'peek_proc': subprocess.Popen(['python', 'peek/peek.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)}

@pytest.fixture(autouse=True)
def procSetup():
    pytest.peek_proc = subprocess.Popen(['python', 'peek/peek.py'], 
                                    stdout=subprocess.PIPE, stdin=subprocess.PIPE)

def test_ProgramExists():
    peek_output = pytest.peek_proc.communicate(input='1'.encode())[0]
    assert peek_output != None