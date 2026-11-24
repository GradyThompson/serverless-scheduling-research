# Serverless Scheduling Research

Research on online scheduling algorithms, competitive
analysis, and reinforcement learning for serverless
computing systems.

## Overview

Serverless computing introduces a fundamental tradeoff
between resource costs and job response times. Maintaining
active computing resources incurs costs, while shutting
them down introduces cold-start delays for subsequent jobs.

This research investigates scheduling policies that
balance these competing objectives without requiring
advance knowledge of future job arrivals.

## Research Contributions

- Development of two online scheduling algorithms
  with provable performance guarantees.
- Cost within $(1+\epsilon)$ of optimal and worst-case
  response time within $O(1/\epsilon)$ of optimal.
- Competitive-ratio upper bounds and lower bounds
  on achievable online performance.
- Reinforcement learning for scheduling decisions
  using Proximal Policy Optimization (PPO).
- Experimental comparison of learned and
  algorithmic scheduling policies.

## Reinforcement Learning

The reinforcement learning approach uses:

- Stable-Baselines3 and PPO.
- A custom Gymnasium simulation environment.
- State representations and reward functions
  designed for scheduling decisions.
- Over 400,000 simulation timesteps per model.

## Publication

Grady Thompson, Mohammad Shahrad, and Sathish Gopalakrishnan.

**Job Scheduling in Serverless Systems:
Cost and Response Time Tradeoffs.**

27th International Conference on Distributed Computing
and Networking (ICDCN), 2026, pp. 62–70.

[Read the paper](https://doi.org/10.1145/3772290.3772308)

## Citation

```bibtex
@inproceedings{thompson2026scheduling,
  title={Job Scheduling in Serverless Systems:
         Cost and Response Time Tradeoffs},
  author={Thompson, Grady and Shahrad, Mohammad
          and Gopalakrishnan, Sathish},
  booktitle={Proceedings of the 27th International
             Conference on Distributed Computing
             and Networking},
  pages={62--70},
  year={2026},
  doi={10.1145/3772290.3772308}
}
```

## Repository

Research implementation and experimental code
are located in the `tradeoff/` directory.
