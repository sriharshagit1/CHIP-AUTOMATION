
def extract_changed_files(diff_text):
    files=[]
    for line in diff_text.splitlines():
        if line.startswith('+++ b/'): files.append(line[6:])
    return list(dict.fromkeys(files))

def build_change_context(history,diff):
    return {'recent_commits':history,'changed_files':extract_changed_files(diff),'diff':diff,'instruction':'Treat recent changes as hypotheses, not proof of causality. Confirm with current failure evidence.'}
