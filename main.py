import socket # module that provides network communication

#Program title + intro
print ("//SYSTEM LOADING...//\n\n====================\n\n\t\tNIGHTWATCH v1.0\n\t\tNETWORK DIAGNOSTICS\n\n====================")

print("\n//SYSTEM MESSAGE:Welcome to NIGHTWATCH! (^u ^)//\nInitialising diagnostics system...")

target_address = input("\nEnter a hostname or IP address:\t")

#target validation
if not target_address.strip():
    print("\n[SYSTEM ERROR] No target was entered.")
else:
    print(f"\n[OK] Target received:\t{target_address}\n//SYSTEM MESSAGE: NIGHTWATCH is ready//")

    print(f"\n\n[INFO] Preparing network diagnostics for: {target_address}\n\n//SYSTEM MESSAGE: DNS INVESTIGATION LOADING...//")
    try:
        hostname, aliases, ip_addresses = socket.gethostbyname_ex(target_address)

        print(f"\n[OK] DNS Resolution successful!\n[INFO] Hostname: {hostname}\n\nIP addresses:")

        for address in ip_addresses:
            print(f"[OK] {address}")

    except socket.gaierror:
        print(f"\n[ERROR] DNS resolution failed.\n[INFO] Couldn't locate IP address for {target_address}")

print ("\n\n====================\n\n\t\tINVESTIGATION COMPLETE\n\n====================")
