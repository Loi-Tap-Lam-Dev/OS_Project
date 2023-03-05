from typing import Union, Optional
from pathlib import Path
import os

def ptree(startpath: Union[str, Path], 
          max_depth:int = 1, 
          quick_glance: Optional[int] = None, 
          _current_depth:int = 0) -> None:
  """
  Recursively print directory tree up to a given `max_depth`, specifying if you
  like a limited number of files and dirs to include in a `quick_glance`.
  
  Parameters
  ----------
  startpath: Union[str, Path]
    The filepath at which to start.
  max_depth: int
    The maximum depth of nested directories to explore.
  quick_glance: Optional[int]
    If specified, limits exploration to the first however-many files and dirs.
  _current_depth: int
    So that we can track our depth as we call the function recursively.
  """
  
  if _current_depth==0:
    print(startpath)
  else:
    print(f'{"--"*_current_depth} {[d for d in startpath.split(os.sep) if d][-1]}')
    
  _current_depth += 1
  
  if _current_depth > max_depth:
    return None
  else:
    ls = os.listdir(startpath)
    files = [f for f in ls if os.path.isfile(os.path.join(startpath,f))]
    dirs = [d for d in ls if os.path.isdir(os.path.join(startpath,d))]
    
    if quick_glance:
      files = files[:quick_glance]
      dirs = dirs[:quick_glance]

    [print(f'{".."*_current_depth}{f}') for f in files]

    [ptree(os.path.join(startpath, d), max_depth, quick_glance, _current_depth)
      for d in dirs]
    
    return None

ptree('D:',2)