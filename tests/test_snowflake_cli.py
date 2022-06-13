from snowflakecli import __version__
from tests import *

def test_version():
    assert __version__ == '0.1.0'

def main():
    tests.testcalc()
    snowflakecli.start_run()

if __name__ == '__main__':
    main()
