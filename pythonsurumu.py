# -*- coding: utf-8 -*-
import sys

_2x_metni = u""" 
Python'ın 2.x sürümlerinden birini kullanıyorsunuz.
Programı çalıştırabilmek için sisteminizde python'ın 3.x sürümlerinden
biri kurulu olmalı."""

_3x_metni = u"Programa hoşgeldiniz!"

if sys.version_info.major < 3:
    print(_2x_metni)
else:
    print(_3x_metni)
