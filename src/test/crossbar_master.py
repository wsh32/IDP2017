#!/usr/bin/env python

"""crossbar_master.py: learning crossbar"""

from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

__author__ = "Wesley Soo-Hoo"
__license__ = "MIT"


class Component(ApplicationSession):
    """
    An application component that publishes an event every second.
    """

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        counter = 0
        while True:
            self.publish(u'com.wsh32.test', counter)
            print("Sending: {}".format(counter))
            counter += 1
            yield sleep(1)


if __name__ == '__main__':
    runner = ApplicationRunner(url = u"ws://localhost:8080/ws", realm = u"realm1")
    runner.run(Component)
