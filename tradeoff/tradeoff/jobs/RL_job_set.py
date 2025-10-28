from tradeoff.jobs.continuous_job_generation import ContinuousJobGeneration
import tradeoff.jobs.job_manager as job_manager

"""
Create a file with jobs of the same distribution that was used to train the RL model
"""
job_generator = ContinuousJobGeneration("job_config/rl_train_continuous_js1.txt")
jobs = job_generator.generate_bounded_jobs(0)

job_manager.jobs_to_file(jobs, "job_sets/js2.txt")