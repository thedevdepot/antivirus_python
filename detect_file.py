import os

print("UT1 complete")

def isFileMalicious(file_path, malicious_signature): 
    try:
        with open(file_path, "rb") as file:
            print("UT2 complete")
            fileContent = file.read()
            if malicious_signature in fileContent:
                return True
            return False
    except FileNotFoundError:
        print("File not found")
        return False


if __name__ == "__main":
    malicious_signature = b"tH1s_!ZaT36T"
    file_path = r"/signatures/test_signature.txt"

    if isFileMalicious(file_path, malicious_signature):
        print("Potential malicious file detected")
    else:
        print("No malicious file detected")
        
