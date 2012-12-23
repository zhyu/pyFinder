# -*- coding: utf-8 -*-

import chardet, os

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
    n = len(text)
    m = len(pattern)
    
    rightMostIndexes = {}
    for i in xrange(m-1, -1, -1):
	c = pattern[i]
	if c not in rightMostIndexes: rightMostIndexes[c] = i

    alignedAt = 0
    while alignedAt + (m - 1) < n:
	for indexInPattern in xrange(m-1, -1, -1):
	    indexInText = alignedAt + indexInPattern
	    x = text[indexInText]
	    y = pattern[indexInPattern]
	    if indexInText >= n: break
	    if x != y:
		r = rightMostIndexes.get(x)
		if x not in rightMostIndexes:
		    alignedAt = indexInText + 1
		else:
		    shift = indexInText - (alignedAt + r)
		    alignedAt += (shift > 0 and shift or 1)
		break
	    elif indexInPattern == 0: return alignedAt

def find(text, pattern, flag):
    if(flag == 0): return pattern in text
    if(flag == 1): return kmp(text, pattern) != None
    if(flag == 2): return bm(text, pattern) != None

def Find(files, keywords, flag):
    result = {}    
    for filePath in files:
        fileName = os.path.split(filePath)[1]
        result[fileName] = []
        data = open(filePath).read()
        encoding = chardet.detect(data)['encoding']
	data = data.decode(encoding)
	for keyword in keywords:
	    if find(data, keyword, flag):
		result[fileName].append(keyword)
    return result
		