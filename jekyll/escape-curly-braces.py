import sys
import re

text = input("Type string to escape:")    
text = re.sub(r"(\{+)",r'{{"\1"}}', text)
sys.stdout.write(text)
