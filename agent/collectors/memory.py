import psutil
from agent.collectors.base import Collector
from agent.models import Metric


class MemoryCollector(Collector):

    def collect(self):
        vm = psutil.virtual_memory()
        sm = psutil.swap_memory()

        return [
            Metric(
                name="custom.system.memory.total",
                value=vm.total,
                type="gauge",
                tags=["unit:bytes"]
            ),
            Metric(
                name="custom.system.memory.used",
                value=vm.used,
                type="gauge",
                tags=["unit:bytes"]
            ),
            Metric(
                name="custom.system.memory.available",
                value=vm.available,
                type="gauge",
                tags=["unit:bytes"]
            ),
            Metric(
                name="custom.system.memory.usage",
                value=vm.percent,
                type="gauge",
                tags=["unit:percent"]
            ),
            Metric(
                name="custom.system.swap.total",
                value=sm.total,
                type="gauge",
                tags=["unit:bytes"]
            ),
            Metric(
                name="custom.system.swap.used",
                value=sm.used,
                type="gauge",
                tags=["unit:bytes"]
            ),
            Metric(
                name="custom.system.swap.usage",
                value=sm.percent,
                type="gauge",
                tags=["unit:percent"]
            ),
        ]
