'''
DCP #17

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the maxim (number of characters) absolute path to a file within our file system. For example, in the second example above, the maxim absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the maxim absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''

from collections import defaultdict
class Solution:
    def checkFile(self, name):
        """
        it will either start with dot, as in contain no name only .ext
        or it will have a name an an extension, just atleast one dot
        """
        if(name[0]=='.'):
            return True
        if(len(name.split('.'))>=2):
            return True
        return False
    #THIS IS CORRECT AND CLEARS ALL TEST CASES
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxim = 0
        prev_tab_count = 0
        # store tuples (name, level)
        stack = []
        s = input.split('\n')
        
        for ss in s:
            ss_tab_count = 0
            while ss.startswith('\t'):
                ss_tab_count += 1
                # \t only takes one character
                ss = ss[1:]
            
            while len(stack) and stack[-1][1] >= ss_tab_count:
                stack.pop()
            stack.append((ss, ss_tab_count))
            #print(stack) #DEBUG
            if self.checkFile(ss):
                maxim = max(maxim, len('/'.join(map(lambda x: x[0], stack))))
        return maxim
    #THIS FAILS FOR SOME TEST CASES, NO STACK USED HERE
    def lengthLongestPath___FAILS(self, input):
        """
        :type input: str
        :rtype: int
        """
        maxim = 0
        if(len(input)==0):
            return 0
        rec = defaultdict(int)
        inputs = input.split('\n')
        for item in inputs:
            item_tab_count = 0
            while item.startswith('\t'):
                item_tab_count += 1
                # \t only takes one character
                item = item[1:]
            if(self.checkFile(item)):
                if(item_tab_count>0):
                    maxim = max(maxim, rec[item_tab_count-1]+len(item)+1)
                else:
                    maxim = max(maxim, rec[item_tab_count-1]+len(item))
            oldval = rec[item_tab_count]
            if(item_tab_count==0):
                rec[item_tab_count] = max(len(item),oldval)
            else:
                
                rec[item_tab_count] = max(oldval, len(item)+rec[item_tab_count-1]+1)
        return maxim

assert Solution().lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")==32
assert Solution().lengthLongestPath("rzzmf\nv\n\tix\n\t\tiklav\n\t\t\ttqse\n\t\t\t\ttppzf\n\t\t\t\t\tzav\n\t\t\t\t\t\tkktei\n\t\t\t\t\t\t\thhmav\n\t\t\t\t\t\t\t\tbzvwf.txt")==47
assert Solution().lengthLongestPath("a")==0
assert Solution().lengthLongestPath("a.txt")==5