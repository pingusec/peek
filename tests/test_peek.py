import pytest
import subprocess

def test_ProgramExists():
    peek_proc = subprocess.Popen(['python', 'peek/peek.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    peek_output = peek_proc.communicate()[0]
    assert peek_output != None