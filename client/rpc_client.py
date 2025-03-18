import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000/")

def upload_file():
    file_path = input("Enter file path to upload: ").strip()
    try:
        with open(file_path, "rb") as f:
            file_data = xmlrpc.client.Binary(f.read())
        filename = file_path.split("/")[-1] if "/" in file_path else file_path.split("\\")[-1]
        response = server.upload_file(filename, file_data)
        print(response)
    except FileNotFoundError:
        print("Error: File not found.")

def download_file():
    filename = input("Enter filename to download: ").strip()
    try:
        file_data = server.download_file(filename)
        with open(filename, "wb") as f:
            f.write(file_data.data)
        print(f"File '{filename}' downloaded successfully.")
    except Exception as e:
        print(f"Error: {e}")

def list_files():
    try:
        files = server.list_files()
        if files:
            print("Files on server:")
            for f in files:
                print(f"- {f}")
        else:
            print("No files found on server.")
    except Exception as e:
        print(f"Error: {e}")

def delete_file():
    filename = input("Enter filename to delete: ").strip()
    try:
        response = server.delete_file(filename)
        print(response)
    except Exception as e:
        print(f"Error: {e}")

while True:
    print("\nRemote File Management System")
    print("1. Upload File")
    print("2. Download File")
    print("3. List Files")
    print("4. Delete File")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        upload_file()
    elif choice == "2":
        download_file()
    elif choice == "3":
        list_files()
    elif choice == "4":
        delete_file()
    elif choice == "5":
        print("Exiting client...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
