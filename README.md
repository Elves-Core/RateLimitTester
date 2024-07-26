
# Elves Core RateLimitTester

This Python script tests for a Lack of Resources & Rate Limiting vulnerability (CWE-770) in the `email_change` endpoint of a web application. The script sends multiple requests to the endpoint to check if it is properly rate-limited.

## Description

The `email_change` endpoint is used to send email change requests. If not properly rate-limited, attackers can exploit this endpoint to send a large number of emails, leading to resource exhaustion and potential denial of service (DoS).

## Usage

### Requirements

- Python 3.x
- `requests` library

Install the `requests` library using pip if you don't have it installed:

\`\`\`bash
pip install requests
\`\`\`

### Configuration

Update the following variables in the script:

- `url`: The URL of the `email_change` endpoint.
- `payload`: The JSON payload containing the target email address.
- `number_of_requests`: The total number of requests to send.
- `concurrent_threads`: The number of concurrent threads to use.

### Running the Script

Run the script using Python:

\`\`\`bash
python rate_limit_tester.py
\`\`\`

The script will send the specified number of requests to the `email_change` endpoint and print the status code and response for each request.

## Disclaimer

This script is intended for educational purposes and authorized testing only. Do not use it to target systems without proper authorization. Misuse of this script may result in legal consequences.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
