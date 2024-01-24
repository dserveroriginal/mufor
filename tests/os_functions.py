import errno
import os

def try_rm(filename):
    """Try to remove a file."""
    
    try:
        os.remove(filename)
    except OSError as ose:
        if ose.errno != errno.ENOENT:
            raise
        
def exist(filename):
    """Check if a file exists."""
    
    return os.path.exists(filename)

def fl_gen(name):
    """Generate a filename."""
    
    filename=os.path.join(os.path.dirname(__file__), 'data', name)
    return filename

def write_json(data,filename):
    """Write json to a file."""
    
    import json
    with open(filename, 'w') as file:
        json.dump(data, file)
    return filename