import os
import sys

from scrapy.cmdline import execute

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    execute(['scrapy', 'crawl', 'itcast'])

'''
185.199.108.153 assets-cdn.github.com
185.199.109.153 assets-cdn.github.com
185.199.110.153 assets-cdn.github.com
185.199.111.153 assets-cdn.github.com
199.232.5.194   github.global.ssl.fastly.net
'''