#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import hashlib
import sys
import struct


def sha256(str):
    sha = hashlib.sha256();
    sha.update(str)
    return sha.digest()

def get_bitcoin_hash(hex_str):
    """
    1. sha256(sha256(str))
    2. reverse previous result
    """
    sha = hashlib.sha256();
    bytes = bytearray.fromhex(hex_str)
    reverse_double_hash = sha256(sha256(bytes))[::-1]
    return binascii.hexlify(reverse_double_hash)

def le_hex_2_long(hex_str):
    return struct.unpack("<Q", binascii.unhexlify(hex_str))[0]
