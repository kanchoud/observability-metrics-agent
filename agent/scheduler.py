import time
import logging

logger = logging.getLogger(__name__)

class Scheduler:

    def __init__(self, collectors, exporter, interval):
        self.collectors = collectors
        self.exporter = exporter
        self.interval = interval

    def run(self):
        while True:
            all_metrics = []

            for collector in self.collectors:
                try:
                    all_metrics.extend(collector.collect())
                except Exception:
                    logger.exception("Collector failed")

            try:
                self.exporter.send(all_metrics)
            except Exception:
                logger.exception("Exporter failed")

            time.sleep(self.interval)
