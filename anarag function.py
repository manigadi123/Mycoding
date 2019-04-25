import os
import re


with open(os.environ['OUTPUT_PATH'], 'w') as f:
    f.read()
    
print(type(f))
