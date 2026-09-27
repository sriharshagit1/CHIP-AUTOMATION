from .regression_cluster import cluster_failures
from .temporal_failures import parse_timestamped_failures, primary_candidates

def triage_regression(failures):
    clusters=cluster_failures(failures)
    events=parse_timestamped_failures(failures)
    return {'clusters':clusters,'primary_candidates':primary_candidates(events),'instruction':'Prioritize early failures and large clusters for investigation, but require causal evidence and verification before declaring a root cause.'}
