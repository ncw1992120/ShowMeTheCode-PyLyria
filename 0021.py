#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright 2016 PyLyria nichengwei120@163.com
# CreateTime: 2016-06-20 16:49:41
import os
from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    if salt is None:
        salt = os.urandom(8)

    assert 8 == len(salt)
    assert isinstance(salt, bytes)

    if isinstance(password, str):
        password = password.encode('utf-8')

    assert isinstance(password, bytes)

    result = password
    for i in range(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result

def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])

if __name__ == '__main__':
    while True:
        #输入密码并加密
        hashed = encrypt_password(input('Password:'))
        print(hashed)
        #验证密码是否正确
        password = input('Password Again:')
        assert validate_password(hashed, password)
