import riemann_client.client
from riemann_client.transport import TCPTransport
import time

def send_event():
    with riemann_client.client.Client(TCPTransport("127.0.0.1", 5555)) as client:
        # Create an event
        event = client.event(
            service="webapp",
            state="ok",
            description="Web application is running",
            metric_f=5,
            ttl=60 
        )
        try:
            client.transport.send(event)
            print("Event sent successfully.")
        except Exception as e:
            print(f"Failed to send event: {e}")

if __name__ == "__main__":
    send_event()
