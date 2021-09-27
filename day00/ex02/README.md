Hard links reference the physical location of the original file, on the other hand,
soft links only  points to the original file, thus, moving or deleting the original file will
make the soft link point to a non existing file, Oppositely, the hard link will remain linked
even if the original file is moved.
Hard links cannot be created for special files or directories, soft links can. 
