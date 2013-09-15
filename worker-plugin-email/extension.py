#!/usr/bin/env python
import logging

class Email(object):
    def __init__(self):
        self.logger = logging.getLogger('email')

    def run(self, document):
        self.logger.info('run')
        self.logger.info('document: %r', document)
