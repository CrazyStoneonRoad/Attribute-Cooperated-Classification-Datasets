# 1. Attributes.json
Attributes label vectors with the form of `0001000100101`.
Each number represents whether this attribute item is true for the current image.

# 2. count.txt
Numbers of each attribute in the dataset, in the form of `lawn 450`. 
The first string represents attribute name, and the secon string represents number of this attribute.

# 3. check_attr.py
Python file to generate `count.txt`

# 4. Dict.py
Ordered dictionary of attributes in this dataset. 
The sequence of attributes in this dictionary cooresponds to that of vectors in `Attributes.json`. 
