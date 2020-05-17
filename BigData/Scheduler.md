# Resource Scheduler for Cluster Workloads

## Scheduler
- Google: Borg (not open <source src="" type="">)
- YARN
	- a batch scheduler for Hadoop with no or very limited support for stateless, stateful, and daemon jobs.
- Mesos
- Kubernetes
	- Similar to Michelangelo?
	- Automate scheduling of different container;
- Uber: Michelangelo
	- https://eng.uber.com/michelangelo-machine-learning-platform/
	- Michelangelo enables internal teams to seamlessly build, deploy, and operate machine learning solutions at Uber's scale.
	- It is designed to cover the end-to-end ML workflow: manage data, train, evaluate, and deploy models, make predictions, and monitor predictions.
	- The system also supports traditional ML models, time series forecasting, and deep learning.
- Uber: Peloton
	- https://eng.uber.com/resource-scheduler-cluster-management-peloton/
	- Stateless jobs are long-running services without persistent states.
	- Stateful jobs are long-running services, such as those from Cassandra, MySQL, and Redis, that have persistent state on local disks.
	- Batch jobs typically take a few minutes to a few days to run to completion. There is a broad category of batch jobs for data analytics, machine learning, maps, and autonomous vehicles-related processing, emanating from software such as Hadoop, Spark, and TensorFlow. These jobs are preemptible by nature and less sensitive to short-term performance fluctuations due to cluster resource shortages.
	- Daemon jobs are agents running on each host for infrastructure components, such as Apache Kafka, HAProxy, and M3 Collector.
