__author__ = 'Shravan Papanaidu'

# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
#
# extra_end('Hello') ? 'lololo'
# extra_end('ab') ? 'ababab'
# extra_end('Hi') ? 'HiHiHi'

def extra_end (str):
    length = len(str)
    extra = str[length-2:] #Alternatively, you can use str[-2:]
    return extra*3

print extra_end("momim")