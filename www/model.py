import os
import re

strs = "1,2,3ssssssssss"
s = re.match('\d{1,}',strs);
print(s)