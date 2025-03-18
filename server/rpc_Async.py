from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from socketserver import ThreadingMixIn
import os

UPLOAD_DIR = "server_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

def upload_file(filename, file_data):
    """Asynchronous file upload."""
    with open(os.path.join(UPLOAD_DIR, filename), "wb") as f:
        f.write(file_data.data)
    return f"File '{filename}' uploaded successfully."

server = ThreadedXMLRPCServer(("localhost", 8000), requestHandler=SimpleXMLRPCRequestHandler)
server.register_function(upload_file, "upload_file")

print("Asynchronous XML-RPC Server running on port 8000...")
server.serve_forever()
