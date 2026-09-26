import re
from collections import defaultdict
from .failure_context import normalize_log

def signature(log):
    ctx=normalize_log(log)
    files=tuple(sorted(x['file'] for x in ctx['files']))
    cats=tuple(sorted(ctx['categories']))
    return cats,files

def cluster_failures(failures):
    buckets=defaultdict(list)
    for item in failures:
        buckets[signature(item.get('log',''))].append(item)
    clusters=[]
    for key,items in buckets.items():
        clusters.append({'signature':{'categories':list(key[0]),'files':list(key[1])},'members':items,'count':len(items),'shared_root_cause_hypothesis':len(items)>1})
    return sorted(clusters,key=lambda x:x['count'],reverse=True)

def summarize_clusters(clusters):
    return {'clusters':len(clusters),'failures':sum(c['count'] for c in clusters),'largest_cluster':max((c['count'] for c in clusters),default=0)}
