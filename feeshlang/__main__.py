import sys
from .execute import ExecutionContext

if len(sys.argv) == 2:
    ExecutionContext().execute_file(sys.argv[1])
else:
    print('Error: must have one argument (filename)', file=sys.stderr)
