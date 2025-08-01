import sys

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')
print("Exit")


print(sys.version)
print(sys.platform)


print(sys.path)
print(sys.argv)
print(sys.executable)
print(sys.modules)
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())
print(sys.getrecursionlimit())
print(sys.getrefcount('a'))
print(sys.getsizeof('a'))
print(sys.getwindowsversion())
# print(sys.getdlopenflags())
print(sys.get_int_max_str_digits())

print(sys.getallocatedblocks())
# print(sys.gettotalrefcount())
# print(sys.getcheckinterval())
print(sys.getswitchinterval())
print(sys.getprofile())