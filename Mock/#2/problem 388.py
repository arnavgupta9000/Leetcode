def solve(input):
    # Dictionary to store the cumulative length of paths at each depth
    depth_to_length = {0: 0}  # Base depth 0 has no characters
    max_length = 0

    # Split the input by lines
    for line in input.split("\n"):
        # Determine the depth based on the number of leading '\t'
        depth = line.count('\t')
        # Remove the '\t' characters to get the actual name
        name = line.lstrip('\t')
        
        if '.' in name:  # It's a file
            # Calculate the absolute path length
            current_length = depth_to_length[depth] + len(name)
            # Update the maximum path length if this is the longest
            max_length = max(max_length, current_length)
        else:  # It's a directory
            # Update the cumulative length for the next depth
            depth_to_length[depth + 1] = depth_to_length[depth] + len(name) + 1  # +1 for the '/' separator

    return max_length

print(solve("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")

'''
this one I couldnt figure out... the problem itself was somewhat easy to grasp once you knew what you were doing but before that it was really hard, and even after you knew what you were doing it was still basically impossible for me to see it

lstrip('\t'): Removes only the leading tab characters from the line (those at the start). This is what we need because the tabs at the beginning of the line represent the depth (level of nesting) in the file system. The rest of the line (the name of the file or directory) should remain intact.

strip('\t'): Removes all tab characters from both the beginning and the end of the line. If a file or directory name contained a tab character (e.g., "file\tname.ext"), strip('\t') would incorrectly remove it, altering the name.


2. Why are we storing at position depth + 1?
This relates to how we track cumulative path lengths for directories:

depth refers to the depth (level) of the current line.
A file or directory at depth depth is a child of a parent directory at depth depth - 1.
When we encounter a directory, we compute the cumulative path length for the next depth level (depth + 1), since any child files or directories of this directory will exist at depth + 1.
Example:

Copy code
dir
\tsubdir
\t\tfile.ext
At "dir", depth = 0. We compute the cumulative length for its children at depth + 1 = 1.
At "subdir", depth = 1. We compute the cumulative length for its children at depth + 1 = 2.

'''