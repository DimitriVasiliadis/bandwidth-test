import psutil
import time

def bytes_to_human_readable(n):
    """Convert bytes to a human-readable format."""
    step_unit = 1024
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if n < step_unit:
            return f"{n:.2f} {unit}"
        n /= step_unit

# Get initial bytes received
initial_bytes = psutil.net_io_counters().bytes_recv

input("Recording bandwidth. Press Enter to stop...")

# Get final bytes received
final_bytes = psutil.net_io_counters().bytes_recv

# Calculate used bandwidth
used_bytes = final_bytes - initial_bytes

# Convert to human-readable format
human_readable_used = bytes_to_human_readable(used_bytes)
print(f"{human_readable_used} of bandwidth used.")