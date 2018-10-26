#!/usr/bin/python
#coding:utf-8
#Filename:test.py
#The Program Is Used To Test.

import IPLocate

test = IPLocate.IP()
test.load_dat("IP_basic_2018W42_single_WGS84.dat")

while True:
    ip = raw_input("Input IP: ")
    result = test.locate_ip(ip)
    print("|".join(result))
