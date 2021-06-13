#!/usr/bin/env python
import os, unicodecsv as csv

IDs = {}
i = 0
csvFileName = 'lesson_names.csv'
rangeStart = 123
rangeEnd = 129
prefix = 'lesson'
fileType = '.mp4'

with open(csvFileName,'rb') as csvfile:
    timeReader = csv.reader(csvfile, delimiter = ',')
    # build dictionary with associated IDs
    for row in timeReader:
        i = i+1
        IDs[i] = row[0]

# Directories
# 1. `txt_orig`: Original Folder with Files to be renamed
# 2. `txt_tmp`:  Destination Folder where original files are moved with with prefix from CSV
path = 'txt_orig/'
tmpPath = 'txt_final/'


for id in range(rangeStart, rangeEnd + 1):
    os.rename(os.path.join(path, prefix + str(id) + fileType), os.path.join(tmpPath, prefix + str(id) +  '-' +IDs[id]) + fileType)




