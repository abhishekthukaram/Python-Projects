# 1. "/a/b/c/.." -> "/a/b"
# 2.  "/a/b/c/../d/e/../f" ->"/a/b/d/f"
# 3.  "/a/b/c/../.." ->"/a"
# 4.  "/a/../../.." ->"/"

def functionparse(input_string):
    compare = input_string.split("/")
    stack = []
    path = '/'
    for i in compare:
        if i != "..":
            if i.isalpha():
                stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()
    if len(stack) == 0:
        return path
    else:
        addpath = [path + element for element in stack]
        result = ''.join(addpath)
    return result

print(functionparse("/a/../../"))
print(functionparse("/a/b/c/.."))
print(functionparse("/a/b/c/../.."))
print(functionparse("/a/b/c/../d/e/../f"))
print(functionparse("/a/b/c/../../../../../d/e/../f"))