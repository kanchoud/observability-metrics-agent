import logging
from agent.scheduler import Scheduler
from agent.collectors.cpu import CpuCollector
from agent.exporters.dogstatsd import DogStatsDExporter

logging.basicConfig(level=logging.INFO)

def main():
    collectors = [CpuCollector()]
    exporter = DogStatsDExporter()
    scheduler = Scheduler(collectors, exporter, interval=10)
    scheduler.run()

if __name__ == "__main__":
    main()
