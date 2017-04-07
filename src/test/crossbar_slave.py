#!/usr/bin/env python

"""crossbar_slave.py: learning crossbar"""

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

__author__ = "Wesley Soo-Hoo"
__license__ = "MIT"


class Component(ApplicationSession):

    @inlineCallbacks
    def onJoin(self, details):
        print("session attached")
        self.received = 0

        def on_event(arg):
            print("Got event: {}".format(arg))

        yield self.subscribe(self.on_event, u"com.wsh32.test")
        print("Subscribed to com.wsh32.test")

    def onDisconnect(self):
        print("disconnected")
        if reactor.running:
            reactor.stop()


if __name__ == '__main__':
    runner = ApplicationRunner(url=u"ws://localhost:8080/ws", realm=u"realm1")
    runner.run(Component)
