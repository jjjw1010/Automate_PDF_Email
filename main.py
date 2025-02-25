import subprocess

def main():
    print("Get pdf...")
    subprocess.run(["python", "get_pdf.py"])

    print("Send Email...")
    subprocess.run(["python", "send_email.py"])

if __name__ == "__main__":
    main()
