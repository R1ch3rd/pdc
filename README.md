# Remote File Management System (RPC-Based)

This is a **Remote File Management System** built using **Python and XML-RPC**, allowing users to **upload, download, list, and delete files** on a remote server.

## 🚀 Features
- 📤 **Upload files** to the remote server.
- 📥 **Download files** from the remote server.
- 📂 **List all files** stored on the server.
- 🗑️ **Delete files** from the server.
- 🔄 **Client runs in a loop** until the user exits.
- **Files get saved in server_files**
---

## 📌 Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/pdc.git
cd pdc
```
### **2️⃣ Start Client and Server**
```sh
cd server
python rpc_server.py
```
```sh
cd client
python rpc_client.py
```
