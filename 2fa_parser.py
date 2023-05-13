import re

input_file = "2fa.txt"
output_file = "results.txt"

try:
    with open(input_file, "r") as f:
        contents = f.read()

    pattern = r"otpauth://totp/CoinList:[^?]*\?secret=([^&]*)"
    secrets = re.findall(pattern, contents)

    with open(output_file, "w") as f:
        for secret in secrets:
            f.write(secret + "\n")

    print(f"Successfully extracted {len(secrets)} secret keys.")

except FileNotFoundError:
    print(f"Error: {input_file} not found.")

except:
    print("An error occurred while processing the file.")
