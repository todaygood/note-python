

(venv) [root@pcentos eagleeye]# pip3 install werkzeug==
Looking in indexes: https://mirrors.aliyun.com/pypi/simple/
ERROR: Could not find a version that satisfies the requirement werkzeug== (from versions: 0.1, 0.2, 0.3, 0.3.1, 0.4, 0.4.1, 0.5, 0.5.1, 0.6, 0.6.1, 0.6.2, 0.7, 0.7.1, 0.7.2, 0.8, 0.8.1, 0.8.2, 0.8.3, 0.9, 0.9.1, 0.9.2, 0.9.3, 0.9.4, 0.9.5, 0.9.6, 0.10, 0.10.1, 0.10.2, 0.10.4, 0.11, 0.11.1, 0.11.2, 0.11.3, 0.11.4, 0.11.5, 0.11.6, 0.11.7, 0.11.8, 0.11.9, 0.11.10, 0.11.11, 0.11.12, 0.11.13, 0.11.14, 0.11.15, 0.12, 0.12.1, 0.12.2, 0.13, 0.14, 0.14.1, 0.15.0, 0.15.1, 0.15.2, 0.15.3, 0.15.4, 0.15.5, 0.15.6, 0.16.0, 0.16.1, 1.0.0rc1, 1.0.0, 1.0.1, 2.0.0rc1, 2.0.0rc2, 2.0.0rc3, 2.0.0rc4, 2.0.0rc5, 2.0.0, 2.0.1, 2.0.2, 2.0.3, 2.1.0, 2.1.1, 2.1.2, 2.2.0a1, 2.2.0, 2.2.1, 2.2.2, 2.2.3, 2.3.0, 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.3.6, 2.3.7, 3.0.0, 3.0.1)
ERROR: No matching distribution found for werkzeug==
WARNING: You are using pip version 21.1.1; however, version 23.3.1 is available.
You should consider upgrading via the '/root/eagleeye/venv/bin/python3 -m pip install --upgrade pip' command.
(venv) [root@pcentos eagleeye]# 



ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'OpenSSL 1.0.2k-fips  26 Jan 2017'. See: https://github.com/urllib3/urllib3/issues/2168