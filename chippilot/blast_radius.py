import re

def extract_modules(rtl):
    return re.findall(r'\bmodule\s+([A-Za-z_][A-Za-z0-9_]*)',rtl)

def extract_instantiations(rtl):
    return re.findall(r'\b([A-Za-z_][A-Za-z0-9_]*)\s+[A-Za-z_][A-Za-z0-9_]*\s*\(',rtl)

def analyze_blast_radius(rtl,changed_file,dependent_files=None):
    modules=extract_modules(rtl)
    inst=extract_instantiations(rtl)
    return {'changed_file':changed_file,'modules':modules,'instantiated_types':inst,'dependent_files':dependent_files or [],'risk':'REVIEW_REQUIRED' if len(inst)>0 else 'LOCAL','instruction':'Run targeted verification first, then regression covering dependents before accepting the patch.'}
