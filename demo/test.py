#coding:utf8
'''

'''
import os

paths = os.environ['path']

print 'type:',type(paths)

for p in paths.split(';'):
    print p


