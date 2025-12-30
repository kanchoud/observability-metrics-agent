import psutil
from agent.collectors.base import Collector
from agent.models import Metric

class CpuCollector(Collector):

    def collect(self):
        return [
            Metric(
                name="custom.system.cpu.usage",
                value=psutil.cpu_percent(),
                type="gauge",
                tags=["unit:percent"]
            )
        ]
