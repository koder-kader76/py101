# Program c.py requires version 3.11 of Python and version 2.1.2 of Flask:

import sys
import flask

print(f"This is program {__file__}")
print(f"The Python version is {sys.version}")
print(f"The Flask version is {flask.__version__}")

# source ~/.venv/env_c/bin/activate           # Step 1
# python c.py                                 # Step 2
# deactivate                                  # Step 3