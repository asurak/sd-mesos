"""
Mesos Server Density plugin
Mesos
https://github.com/asurak/sd-mesos/
Version: 1.0.0
"""

import json
import urllib2

class Mesos (object):
    def __init__(self, agentConfig, checksLogger, rawConfig):
        self.agentConfig = agentConfig
        self.checksLogger = checksLogger
        self.rawConfig = rawConfig

    def run(self):
        try:
            ip = self.rawConfig['Mesos'].get(
                'ip','127.0.0.1')
            port = self.rawConfig['Mesos'].get(
                'port',5050)
            #self.checksLogger.info(self.rawConfig)
            metrics = urllib2.urlopen("http://%s:%s/metrics/snapshot" % (ip, port)).read()
            #self.checksLogger.info(metrics)
            data = json.loads(metrics)
            return data
        except:
            return {}
