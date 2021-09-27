There are 3 types of users that can get permissions: owner, members of the owning group and other users.
The first character of the permission's string indicates the file type: "-" for file, "d" for directory, "i" for link.
After the first character, there is a group of three characters, these are permissions assigned to the owner, the second group of three is assigned to the members of the group owning the file, and the last group of three characters are assigned to other users. 
r is for Read, w is for Write, and x is for Execute
There are many methods to modify permissions. I personally use the numerical one, for example: chmod 777 test1, with which I give all permissions to every user. 0 = none, 1 = x, 2 = w, 3 = w and x, 4 = r, 5 = r and x, 6 = r and w, 7 = r, w and x.
