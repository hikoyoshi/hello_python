#!-*-coding:utf-8 -*-

#星星的層數
star = 5
'''
第一種星星排法
 *
 **
 ***
 ****
 *****
'''

for i in range(star):
    print '*'*(i+1)

'''
第二種星星排法
     *
    **
   ***
  ****
 *****
'''
for i in range(star):
    print ' '*(star-i)+'*'*(i+1)
    
'''
第三種星星排法
 
     *
    ***
   *****
  *******
 *********
'''

for i in range(star):
    print ' '*(star-i) + '*'*(2*i+1)