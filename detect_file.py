import os

def is_file_malicious(file_path, malicious_signature): 
    try:
        with open(file_path, "rb") as file:
            fileContent = file.read()
            if malicious_signature in fileContent:
                return True
            return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False


if __name__ == "__main__":
    malicious_signature = b"tH1s_!ZaT36T"
    file_path = r"./signatures/test_signature.txt"

    if is_file_malicious(file_path, malicious_signature):
        print("Potential malicious file detected")
    else:
        print("No malicious file detected")
        
