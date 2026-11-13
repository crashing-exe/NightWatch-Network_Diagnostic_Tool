#Program title + intro
print ("//SYSTEM LOADING...//\n\n====================\n\nNIGHTWATCH v1.0\nNETWORK DIAGNOSTICS\n\n====================")

print("\n//SYSTEM MESSAGE:Welcome to NIGHTWATCH! (^u ^)//\nInitialising diagnostics system...")

target_address = input("\nEnter a hostname or IP address:\t")

#target validation
if not target_address.strip():
    print("\n[SYSTEM ERROR] No target was entered.")
else:
    print(f"\n[OK] Target received:\t{target_address}\n//SYSTEM MESSAGE: NIGHTWATCH is ready//")

print(f"\n\n[INFO] Preparing network diagnostics for: {target_address}")