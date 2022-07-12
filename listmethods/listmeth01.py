#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
print("First Item: "+proto[0])
proto.extend("dns")
print(proto)
