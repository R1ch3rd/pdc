import os
from xmlrpc.server import SimpleXMLRPCServer

# Directory where files will be stored
UPLOAD_DIR = "server_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def list_files():
    """Returns a list of files in the server directory."""
    return os.listdir(UPLOAD_DIR)

import os

UPLOAD_DIR = "server_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure upload directory exists

def upload_file(filepath, file_data):
    """Saves the uploaded file to the server_files directory."""
    filename = os.path.basename(filepath)  # Extract only the filename
    file_path = os.path.join(UPLOAD_DIR, filename)  # Store in server_files/

    with open(file_path, "wb") as f:
        f.write(file_data.data)

    print(f"File saved at: {file_path}")  # Debugging info
    return f"File '{filename}' uploaded successfully at {file_path}."



def download_file(filename):
    """Returns file data for downloading."""
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return f.read()
    return f"File '{filename}' not found."

def delete_file(filename):
    """Deletes a file from the server."""
    file_path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return f"File '{filename}' deleted successfully."
    return f"File '{filename}' not found."

# Start XML-RPC Server
server = SimpleXMLRPCServer(("0.0.0.0", 8000))
server.register_function(list_files, "list_files")
server.register_function(upload_file, "upload_file")
server.register_function(download_file, "download_file")
server.register_function(delete_file, "delete_file")

print("Remote File Management RPC Server is running on port 8000...")
server.serve_forever()