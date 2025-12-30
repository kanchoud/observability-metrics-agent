from datadog import initialize, statsd
from agent.exporters.base import Exporter

class DogStatsDExporter(Exporter):

    def __init__(self, host="localhost", port=8125):
        initialize(statsd_host=host, statsd_port=port)

    def send(self, metrics):
        for m in metrics:
            if m.type == "gauge":
                statsd.gauge(m.name, m.value, tags=m.tags)
            elif m.type == "counter":
                statsd.increment(m.name, m.value, tags=m.tags)
