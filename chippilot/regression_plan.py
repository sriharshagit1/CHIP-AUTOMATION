def build_regression_plan(blast,available_tests):
    dependents=set(blast.get('dependent_files',[]))
    tests=list(available_tests)
    targeted=[t for t in tests if any(d in t for d in dependents)]
    return {'targeted_tests':targeted,'full_regression_required':True,'risk':blast.get('risk','REVIEW_REQUIRED'),'gating_rule':'A patch is accepted only when required regression checks pass.'}
