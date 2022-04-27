# Create Blockchain
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:05:08 2022

@author: Kamel.BOUYACOUB
"""
import datetime;
import hashlib;
import json;
from flask import Flask, jsonify;

# Build a blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
    
    def create_block(self, proof,  previous_hash):
        block = {'index': len(self.chain) + 1 ,
                 'timestamp': datetime.datetime.now(), 
                 'proof': proof,
                 'previous_hash': previous_hash};
        
        self.chain.append(block);
        return block;