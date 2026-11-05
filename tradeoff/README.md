# Tradeoff Research: Online Scheduling in Serverless Systems

Research code for studying the tradeoff between infrastructure cost and job response time in serverless computing systems. The project implements scheduling policies and a discrete-event simulator for comparing how those policies perform under different workloads and parameter settings.

**Associated publication:** Grady Thompson, Mohammad Shahrad, and Sathish Gopalakrishnan, *Job Scheduling in Serverless Systems: Cost and Response Time Tradeoffs*, ICDCN 2026. [Paper (DOI)](https://doi.org/10.1145/3772290.3772308).

## Research question

Activating more containers can reduce the time jobs spend waiting, but increases infrastructure cost. Using fewer containers saves resources, but may increase response times. The associated paper develops and analyzes online scheduling algorithms for managing this tradeoff and establishes theoretical performance guarantees.

This repository provides a simulation environment for exploring the behavior of different scheduling policies. It models job releases, execution durations, container startup delays, job assignments, container activation and termination, and the resulting cost and delays. Theoretical proofs are contained in the paper rather than in this repository.

## Implementation

The main components are:

| Location | Purpose |
| --- | --- |
| [`tradeoff/schedulers/`](tradeoff/schedulers/) | Implementations of FIFO, KJD1, KJD2, UJD1, and UJD2 scheduling policies |
| [`tradeoff/system/controller.py`](tradeoff/system/controller.py) | Coordinates the discrete-event simulation |
| [`tradeoff/system/simulated_system.py`](tradeoff/system/simulated_system.py) | Simulates container execution and associated costs |
| [`tradeoff/results/`](tradeoff/results/) | Tools for recording and analyzing simulation results |
| [`model_config/`](model_config/) | Scheduler configurations and parameter settings |
| [`job_sets/`](job_sets/) | Input workloads |
| [`result_data/`](result_data/) | Stored outputs from simulation experiments |
| [`tests/`](tests/) | Existing test inputs, expected outputs, and test scripts |

The repository also includes an exploratory reinforcement-learning scheduling component. This is separate from the online scheduling algorithms studied in the associated publication.

## Running a simulation

The project uses Python 3.11+ and Poetry. From the directory containing `pyproject.toml`, install dependencies:

```bash
poetry install
```

On **Windows**, an example invocation is:

```bash
poetry run python -m tradeoff.run FIFO_c10 js2 1
```

This selects the FIFO configuration (`model_config/FIFO_c10.txt`), job set (`job_sets/js2.txt`), and startup duration (`1`). The output is written to `result_data/FIFO_c10_js2.txt`.

**Portability note:** The current entry point, `tradeoff/run.py`, constructs paths using Windows-style backslashes. Running this command on macOS or Linux may require adapting those paths. The command above has not been independently verified in every environment.

## Evaluating results

For each workload and policy configuration, the simulator records total container cost and job-level queue delays. Container cost represents cumulative active-container time; queue delay is calculated from a job's completion time, release time, and execution duration.

These outputs make it possible to compare policies under consistent workload assumptions and investigate how policy parameters affect cost and responsiveness. The repository contains example results and plotting utilities. Simulation results complement, but do not establish, the theoretical guarantees proved in the paper.

## Scope

This is academic research software, not a production scheduling system. The code was written to support exploration and experimental evaluation of scheduling policies. For formal model assumptions, theoretical guarantees, and proofs, see the associated publication.
