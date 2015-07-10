import os

def find_module(module):
    result = []
    for paths in os.sys.path:
        try:
            
            a = os.listdir(paths)
        except OSError:
            continue
        if (module in a):
            result.append(paths)
            
    return result
    
            

if __name__ == '__main__':
    result = find_module('site.py')
    print result