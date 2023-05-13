# 2FA Parser

This Python script reads data from a file `2fa.txt` which contains OTPAuth URLs of the form `otpauth://totp/CoinList:qegwyycel%40rambler.ru?secret=d2ykiw6ajflnskjhdjzwehls&issuer=CoinList`. The script parses this data and saves all the secret keys to a separate file `results.txt` in the same order.

## Usage

1. Clone the repository to your local machine.

2. Make sure you have Python 3 installed on your system.

3. Place your OTPAuth URLs in a file called `2fa.txt`, with each URL on a separate line.

4. Run the `2fa_parser.py` script using the command `python 2fa_parser.py`.

5. The secret keys will be saved to a file called `results.txt` in the same directory.

## Error Handling

The script checks for the following errors:

- If the input file `2fa.txt` does not exist or is empty.
- If the input URLs are not in the correct format.
- If the `results.txt` file cannot be created or written to.

If any of these errors occur, the script will display an appropriate error message and exit.

## Output

The `results.txt` file contains only the secret keys extracted from the OTPAuth URLs in the `2fa.txt` file, in the same order.
## Disclaimer
Use at your own risk. The author of this script is not responsible for any loss or damage caused by the use of this script.

## Author

- [@p38iO](https://t.me/p38iO) you can say THX by USDT TRC-20: TUzywR3QV2oyy3NVdsLruAdS5vWd5Tv7c7

