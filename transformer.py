import sys        
import os    
import shutil  


defaultContent = "not good content"


# appending the directory of mod.py
# in the sys.path list
 
from xdtransform import xdtransform    
print(dir(xdtransform))

 
 

 
source_filename = sys.argv[1]
transform_filename = sys.argv[2]
out_filename = sys.argv[3]
 

f = open(out_filename, "w")
f.write(defaultContent)
f.close()

xdtransform.transform(source_filename, transform_filename,  out_filename)



f = open(out_filename, "r")
content = f.read()
f.close()

 
if content.strip() == defaultContent.strip():
  os.remove(out_filename)
  shutil.copy(source_filename, out_filename)
  
  
  
f = open(out_filename, "r")
content2 = f.read()
f.close()

print(content2)