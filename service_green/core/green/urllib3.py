#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

from eventlet import patcher
from eventlet.green import ssl
from eventlet.green import time
from eventlet.green import http
from eventlet.green import socket
from eventlet.green.http import client
from eventlet.green.http import cookies
from eventlet.green.http import cookiejar

from . import pjson

patcher.inject(
    'urllib3', globals(),
    # 注入http  到当前命名空间
    ('http', http), ('client', client), ('cookies', cookies), ('cookiejar', cookiejar),
    # 注入socket到当前命名空间
    ('socket', socket),
    # 注入ssl   到当前命名空间
    ('ssl', ssl),
    # 注入time  到当前命名空间
    ('time', time),
    # 注入json  到当前命名空间
    ('json', pjson)
)
del patcher
