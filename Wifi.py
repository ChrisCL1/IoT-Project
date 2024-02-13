"""import os
import threading

def search(ip_address):
    command = "ping -c 1 " + ip_address
    print(command)
    response = os.popen(command).read()
    if "1 received" in response:  # Adjust this string based on your ping output
        print("Found at: ", ip_address)

for ip in range(1, 254):
    current_ip = "192.168.5.178" + str(ip)  # Correct IP concatenation
    # print("Analyzing IP: ", current_ip)

    # Ensure args is a tuple by adding a comma
    run = threading.Thread(target=search, args=(current_ip,))
    run.start()
"""
# Import necessary libraries
import os
import threading

# Define a function to search for an active IP address using ping
def search(ip_address):
    # Construct the ping command with 1 packet
    command = "ping -c 1 " + ip_address
    # Print the command to show what is being executed
    print(command)
    # Execute the command and read the output
    response = os.popen(command).read()
    # Check if the ping was successful (based on the string "1 received")
    if "1 received" in response:  # Adjust this string based on your ping output
        # If successful, print the IP address
        print("Found at: ", ip_address)

# Loop through a range of numbers to construct IP addresses
for ip in range(1, 254):
    # Construct the IP address string with the current number in the loop
    # Note: The original IP "192.168.5.178" seems incorrect for a range iteration. It might be intended to be "192.168.5."
    current_ip = "192.168.5." + str(ip)  # Corrected IP concatenation for range iteration
    # Uncomment the line below if you want to see the IP being analyzed
    # print("Analyzing IP: ", current_ip)

    # Create a thread to run the search function for the current IP address
    # This allows multiple searches to be conducted in parallel
    run = threading.Thread(target=search, args=(current_ip,))
    # Start the thread
    run.start()
    