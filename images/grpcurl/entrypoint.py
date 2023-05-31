#!/usr/bin/env python3
"""
    This is a small entrypoint script to test chariott with the kv provider.
    It will write and read the fixed Key Value "Hello World" in kv-app provider using chariott
"""

import subprocess
import time

proto_path = "proto"
runtime_proto = "proto/chariott/runtime/v1/runtime.proto"


def runtime_call(method, key, value):
    """
        Execute the grpcurl command with the specified arguments.
    
        Args:
            method (str): The method can be ["read"|"write"]
            key (str): A string will be used to ["write"|"read"] the key in chariott
            value (str): A string will be used as value to be written in chariott key
    
        Returns:
            None
    """
    if method == "write":
        json_parsed = f'{{"namespace":"sdv.kvs","intent":{{"write":{{"key": "{key}","value":{{"string":"{value}"}}}}}}}}'
    else:
        json_parsed = f'{{"namespace":"sdv.kvs","intent":{{"read":{{"key":"{key}"}}}}}}'

    cmd = [
            'grpcurl',
            '-import-path', proto_path,
            '-proto', runtime_proto,
            '-plaintext',
            '-d', json_parsed
            ,
            '0.0.0.0:4243', 'chariott.runtime.v1.ChariottService/Fulfill'
            ]
    try:
        subprocess.run(cmd,check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while calling grpcurl:", e)

while True:
    print("Writing the \"hello\" key with the value \"world\" in chariott kv")
    runtime_call("write","hello", "world")
    
    print("Reading the \"hello\" key from chariott kv")
    runtime_call("read","hello","world")
    time.sleep(5)
