import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from .debug_pipeline import debug

class Handler(BaseHTTPRequestHandler):
    def _send(self,status,payload):
        body=json.dumps(payload,indent=2).encode()
        self.send_response(status); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(body))); self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        if self.path=='/health': self._send(200,{'status':'ok','service':'chippilot'})
        elif self.path=='/': self._send(200,{'service':'ChipPilot','endpoint':'POST /investigate'})
        else: self._send(404,{'error':'not found'})
    def do_POST(self):
        if self.path!='/investigate': return self._send(404,{'error':'not found'})
        try:
            n=int(self.headers.get('Content-Length','0')); data=json.loads(self.rfile.read(n))
            required=['log_path','rtl_path','tb_path']
            if any(k not in data for k in required): return self._send(400,{'error':'log_path, rtl_path and tb_path are required'})
            result=debug(data['log_path'],data['rtl_path'],data['tb_path'])
            self._send(200,result.to_dict())
        except Exception as e: self._send(500,{'error':str(e)})

def serve(host='127.0.0.1',port=8000):
    HTTPServer((host,port),Handler).serve_forever()

if __name__=='__main__': serve()
