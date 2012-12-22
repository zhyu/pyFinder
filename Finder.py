# -*- coding: utf-8 -*-

import os

def kmp(text, pattern):
    m = len(pattern)
    shifts = [None] * (m + 1)
    shift = 1
    for pos in xrange(m+1):
	while shift < pos and pattern[pos-1] != pattern[pos-shift-1]:
	    shift += shifts[pos-shift-1]
	shifts[pos] = shift
    startPos, matchLen = 0, 0
    for c in text:
	while matchLen >= 0 and pattern[matchLen] != c:
	    startPos += shifts[matchLen]
	    matchLen -= shifts[matchLen]
	matchLen += 1
	if matchLen == m:
	    return startPos
 
def bm(text, pattern):
    n, m = len(text), len(pattern)
    if m > n: return -1
    skip = []
    for k in xrange(256): skip.append(m)
    for k in xrange(m-1): skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
	i, j = k, m - 1
	while j >= 0 and text[i] == pattern[j]:
	    j -= 1
	    i -= 1
	if j == -1: return i + 1
	k += skip[ord(text[k])]
    return -1
    
def Find(files, keywords, flag):
    pass
    
