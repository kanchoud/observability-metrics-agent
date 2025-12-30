# Observability Metrics Agent

A **modular, Python-based observability agent for collecting and exporting custom metrics**, built for scalable observability pipelines.

---

## ✨ Features

- 🔌 **Pluggable exporters** (Datadog, Prometheus, OpenTelemetry, and more)
- 🧩 **Modular collectors** (CPU, memory, custom business metrics)
- ⚙️ **Config-driven** using YAML
- 🚀 **Production-ready architecture**
- 🛡 **Fault-tolerant** (collector/exporter failures don’t crash the agent)
- 📈 **Self-observability ready**
- 🐍 **Pure Python**, minimal dependencies
- 🔓 **Vendor-neutral design**

---

## 🏗 Architecture Overview




## 📦 Installation

### Requirements
- Python **3.9+**
- Optional:
  - Datadog Agent (for DogStatsD)
  - Prometheus (for scraping)
  - OpenTelemetry Collector

### Install dependencies
```bash
pip install -r requirements.txt
```

## 🚀Running the Agent

```bash
python -m agent.main
```

## 🗺 Roadmap

- [ ] Async scheduler for high-throughput environments  
- [ ] Metric batching and backpressure handling  
- [ ] Agent self-observability metrics  
- [ ] Kubernetes deployment manifests  
- [ ] Remote configuration support  
- [ ] Integration-style checks  

---

## 📜 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## 🤝 Contributing

Contributions are welcome and encouraged.

Guidelines:
- Follow clean, modular architecture  
- Keep implementations vendor-neutral  
- Run linting and formatting before submitting PRs  

Please open an issue or pull request for any improvements or fixes.
