import sys
from pylib.template import SET_LOCAL_READ

def test_template_local_read():
    SET_LOCAL_READ()
    assert sys.stdin.name == 'debug/in.txt'
