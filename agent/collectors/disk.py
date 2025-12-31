import psutil
from agent.collectors.base import Collector
from agent.models import Metric


class DiskCollector(Collector):

    def collect(self):
        usage = psutil.disk_usage("/")

        return [
            Metric(
                name="custom.system.disk.total",
                value=usage.total,
                type="gauge",
                tags=["unit:bytes"]
            ),
            Metric(
                name="custom.system.disk.used",
                value=usage.used,
                type="gauge",
                tags=["unit:bytes"]
            ),
            Metric(
                name="custom.system.disk.free",
                value=usage.free,
                type="gauge",
                tags=["unit:bytes"]
            ),
            Metric(
                name="custom.system.disk.usage",
                value=usage.percent,
                type="gauge",
                tags=["unit:percent"]
            ),
        ]
