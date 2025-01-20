import requests

def check_directory_traversal(url):
    payloads = [
        "../", 
        "..\\", 
        "%2e%2e%2f",  
        "%2e%2e%5c",  
        "/etc/passwd", 
        "C:\\Windows\\System32\\drivers\\etc\\hosts"  
    ]
    
    for payload in payloads:
        response = requests.get(url + payload)
        
        if "Permission denied" in response.text or "404 Not Found" not in response.text:
            print(f"[+] Directory Traversal vulnerability found at: {url} with payload: {payload}")
            break
