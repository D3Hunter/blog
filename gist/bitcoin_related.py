#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import hashlib
import sys


def sha256(str):
    sha = hashlib.sha256();
    sha.update(str)
    return sha.digest()

def import bitcoin_related(hex_str):
    """
    1. sha256(sha256(str))
    2. reverse previous result
    """
    sha = hashlib.sha256();
    bytes = bytearray.fromhex(hex_str)
    reverse_double_hash = sha256(sha256(bytes))[::-1]
    return binascii.hexlify(reverse_double_hash)
