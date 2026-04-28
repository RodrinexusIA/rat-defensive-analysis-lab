"""
Sanitized RAT Behavior Demo

This file is intentionally safe:
- no reverse shell
- no keylogger
- no persistence
- no payload generation
- no remote command execution
"""

from datetime import datetime

def simulate_event(event_type, detail):
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event_type": event_type,
        "detail": detail,
        "safe_demo": True
    }

if __name__ == "__main__":
    events = [
        simulate_event("network_indicator", "Suspicious outbound connection pattern"),
        simulate_event("persistence_indicator", "Startup registry key observed in analysis notes"),
        simulate_event("collection_indicator", "Screenshot/keylogging capability documented, not implemented")
    ]

    for event in events:
        print(event)
