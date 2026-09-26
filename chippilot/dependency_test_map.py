from pathlib import Path

def map_tests(root='benchmark/cases'):
    root=Path(root); mapping={}
    for p in root.glob('*_tb.sv'):
        name=p.stem
        mapping.setdefault(name,[]).append(str(p))
    return mapping

def prioritize_tests(graph,changed_modules,test_map):
    direct=set(changed_modules); dependent=set()
    for owner,children in graph.get('edges',{}).items():
        if any(c in direct for c in children): dependent.add(owner)
    ordered=[]
    for key,tests in test_map.items():
        score=2 if any(m.lower() in key.lower() for m in direct) else (1 if any(m.lower() in key.lower() for m in dependent) else 0)
        if score: ordered.extend((score,t) for t in tests)
    return [t for _,t in sorted(ordered,key=lambda x:x[0],reverse=True)]
