#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import logging
import stalker

# ================================ PART 0: LOGGING THINGS =================================
if __name__ == '__main__':
    levels = ['info', 'debug', 'error', 'warning', 'critical']
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--level', dest='level', default='info',
                        choices=['info', 'debug', 'error', 'warning', 'critical'])
    args = parser.parse_args()
    logging.basicConfig(format='%(message)s', level=getattr(logging, args.level.upper()))


stalker.stalk()
