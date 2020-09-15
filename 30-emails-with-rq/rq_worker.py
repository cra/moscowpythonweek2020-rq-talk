#!/usr/bin/env python
import os
import sys

import django

from rq import Connection, Worker

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mailsender.settings')
    django.setup()

    with Connection():
        qs = sys.argv[1:] or ['default']

        w = Worker(qs)
        w.work()
