from chippilot.evidence import EvidenceStore, VerificationEvidence

def test_evidence_id_is_deterministic():
    e=VerificationEvidence("r1","cover","c1","smoke","sim",("x",),"PASS",0)
    assert e.evidence_id==VerificationEvidence("r1","cover","c1","smoke","sim",("x",),"PASS",0).evidence_id

def test_store_persists(tmp_path):
    e=VerificationEvidence("r1","cover","c1","smoke","sim",("x",),"PASS",0)
    assert EvidenceStore(tmp_path).save(e).exists()
