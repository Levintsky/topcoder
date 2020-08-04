# Job Management (Bolt)

## Bolt
- Artifacts: ckpt
- Logs:
- Metrics:

## Create a Task
- A folder containing: my_code.py, run.py, config.yaml
	- Example of config:
```python
name: 'Learning Rate Experiment'
description: 'This will train all of the things'
tags: ['a', 'b']
priority: 1
is_parent: True
setup_command: 'bash setup.sh'
command: 'python run.py'
arguments:
  - training_set: '/my_data/train.txt'
parameters:
  learning_rate: [0.01, .1, 1.0]
environment: "my_team_env"
environment_variables:
  'PATH': "something:$PATH"
permissions:
  owners: 'team-admins'
  viewers: 'interns'
resources:
  cluster: simcloud-mr2.apple.com
  group: "org-name:group-name"
  num_gpus: 4
  ports: ["TENSORBOARD_PORT", "OTHER_PORT"]
```
	- Example of run.py
```python
import turibolt as bolt
import my_code

# Run an experiment across different parameter values
for l2 in [0.01, .1, 1.0]:

    # Update model and compute validation loss
    rmse = my_code.train_and_evaluate(l2)

    bolt.send_metrics({
      'l2': l2,
      'rmse': rmse
    })
```
- Running:
	- Check credential;
	- Check priority (affect preemption order);
	- Setup: setup.sh
	- Run job: python run.py

## Submit a Job
- Two ways: cli, by program;
- 1. cli:
```sh
bolt task submit --tar . --max-retries 3
bolt task submit --config local.yaml --tar my_code --exclude file1.txt
bolt task submit --config local.yaml --tar my_code --interactive
```
- 2. program: bolt.submit
```python
import turibolt as bolt

config = bolt.get_current_config()

# Describe the command we want to execute
config['command'] = 'python train.py'

# Launch a task for each learning_rate (asynchronously)
for learning_rate in [0.01, 0.1, 0.5]:
    config['parameters']['learning_rate'] = learning_rate

    # Submit the task to be executed
    bolt.submit(config, max_retries=3)

# Wait for all tasks to finish
bolt.wait()
```

## Check Status
- All tasks:
```sh
bolt task ls
```
- Check status
```sh
bolt task show [task-id]
```
- Resume
```sh
bolt task ssh [task_id]
```

## Metrics
- bolt.send_metics()
```python
import turibolt as bolt
config = bolt.get_current_config()
learning_rate = config['parameters']['learning_rate']

# Placeholder for model training/validation
def get_valid_loss(learning_rate):
    return 1.0 / epoch

num_epochs = 20
for epoch in range(1, num_epochs):

    # Update model and compute validation loss
    loss = get_valid_loss(learning_rate)

    bolt.send_metrics({
      'Valid Loss': loss
    })
```

## Misc
- Retry
- Reproduce:
```sh
bolt task clone a35bd61a --dest my_task
```