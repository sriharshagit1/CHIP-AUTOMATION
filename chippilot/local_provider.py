import json

class LocalRuleProvider:
    """Credential-free provider for pipeline tests; not an AI benchmark."""
    def generate(self,messages,tools):
        text='\n'.join(m.get('content','') for m in messages)
        if 'width_mismatch.sv' in text:
            data={'action':'FINAL','arguments':{'category':'width/truncation','module':'width_mismatch','root_cause':'narrow output is assigned from a wider value without explicit slicing','file':'width_mismatch.sv','old':'nibble = data;','new':'nibble = data[3:0];','rationale':'Use the intended low four bits explicitly.'}}
        else:
            data={'action':'FINAL','arguments':{'category':'unknown','module':'','root_cause':'insufficient evidence','file':'','old':'','new':'','rationale':'No safe patch proposed.'}}
        return json.dumps(data)
