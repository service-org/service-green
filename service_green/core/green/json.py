#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

try:
    import ujson as fast_json
except:
    import json as fast_json

for name in dir(fast_json):
    globals()[name] = getattr(fast_json, name)

del fast_json
