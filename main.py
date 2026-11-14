import socket # module that provides network communication
import time
from pip._internal.resolution.resolvelib import found_candidates

def calculateResponseTime():
    start_time = time.perf_counter()
    end_time = time.perf_counter()
    response_time = (end_time - start_time)*1000
    return response_time

def hostnameResolved(target_address):

    if not target_address.strip():#target validation
        print("\n[SYSTEM ERROR] No target was entered.")
    else:
        print(f"\n[OK] Target received:\t{target_address}\n//SYSTEM MESSAGE: NIGHTWATCH is ready//")

        print(
            f"\n\n[INFO] Preparing network diagnostics for: {target_address}\n\n//SYSTEM MESSAGE: DNS INVESTIGATION LOADING...//")

        try:  # Attempts DNS lookup
            hostname, aliases, ip_addresses = socket.gethostbyname_ex(target_address)

            print(f"\n[OK] DNS Resolution successful!\n[INFO] Hostname: {hostname}\n\nIP addresses:")

            ip_addresses_total = 0

            for address in ip_addresses:  # IP addresses counter assiocated with the target
                print(f"[OK] {address}")
                ip_addresses_total += 1

            print(f"[INFO] Total IP addresses: {ip_addresses_total}\n")

            print("\n[INFO] Total aliases found:", len(aliases))

            if aliases:
                print(f"\nAliases: {len(aliases)}\n")
                for alias in aliases:
                    print(f"\t[OK] {alias}")
            else:
                print("\t[INFO] No aliases were found in the target hostname.\n")

        except socket.gaierror:  # Deals with DNS failure
            print(f"\n[ERROR] DNS resolution failed.\n[INFO] Couldn't locate IP address for {target_address}")

    print(f"\n\t[INFO] Total Response Time: {calculateResponseTime()} ms")

    print("\n\n====================\n\n\t\tINVESTIGATION COMPLETE\n\n====================")


#Program title + intro
print ("//SYSTEM LOADING...//\n\n====================\n\n\t\tNIGHTWATCH v1.0\n\t\tNETWORK DIAGNOSTICS\n\n====================")

print("\n//SYSTEM MESSAGE:Welcome to NIGHTWATCH! (^u ^)//\nInitialising diagnostics system...")

target_address = input("\nEnter a hostname or IP address:\t")

hostnameResolved(target_address)



