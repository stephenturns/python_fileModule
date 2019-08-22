"""
fileModule contains a list of file functions
--> import fileModule
--> filemodule.<functionname>([params])
"""

import os 

def file_exist(strFileName):
    """
    file_exist returns true if a file exists.
    file_exist(<filename>) 
    """
    if os.access(strFileName, os.F_OK):
        return True
    else:
        return False

def file_readable(strFileName):
    """
    file_readable returns true if a file is readable.
    file_readable(<strFileName>)
    """
    if os.access(strFileName, os.R_OK):
        return True
    else:
        return False

def file_writable(strFileName):
    """
    file_writable returns true if a file is writable.
    file_writable(<strFileName>)
    """
    if os.access(strFileName, os.W_OK):
        return True
    else:
        return False

def file_executable(strFileName):
    """
    file_executable returns true if a file is executable.
    file_executable(<strFileName>)
    """
    if os.access(strFileName, os.X_OK):
        return True
    else:
        return False
