#coding:utf8
'''

'''
import os

paths = os.environ['path']
os.environ.setdefault('abc', 'abcccc')

print 'type:',type(paths)

for p in paths.split(';'):
    print p

print '--------',os.environ['abc']
