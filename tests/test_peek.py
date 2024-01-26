import pytest
import subprocess

def test_ProgramExists():
    peek_proc = subprocess.Popen(['python', 'peek/peek.py'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    peek_output = peek_proc.communicate()[0]
    assert peek_output != None

def test_CanContactGoodUrl():
    peek_proc = subprocess.Popen(['python', 'peek/peek.py', 'https://www.google.com'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    peek_output = peek_proc.communicate()[0]
    assert peek_output == b'Welcome to peek v0.1\r\nTarget website up!\r\n'