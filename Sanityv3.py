import requests

def fetch_thousandeyes_tests(api_token):
    url = 'https://api.thousandeyes.com/tests.json'
    headers = {'Authorization': f'Bearer {api_token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        tests_data = response.json()
        return tests_data.get('test')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching tests: {e}")
        return None

def fetch_test_details(api_token, test_id):
    url = f'https://api.thousandeyes.com/tests/{test_id}.json'
    headers = {'Authorization': f'Bearer {api_token}'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        test_details = response.json()
        return test_details
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching details for test {test_id}: {e}")
        return None

def extract_enabled_tests(tests):
    # Filter out tests that are not enabled
    return [test for test in tests if test.get('enabled')]

def analyze_enabled_tests(enabled_tests, api_token):
    for test in enabled_tests:
        test_id = test.get('testId')
        test_name = test.get('testName')
        
        print(f"\nAnalyzing Enabled Test: {test_name} (ID: {test_id})")

        # Step 1: Fetch detailed information for the enabled test
        test_details = fetch_test_details(api_token, test_id)
        if test_details:
            # Extract relevant details
            test_type = test_details.get('type')
            interval = test_details.get('interval')
            url = test_details.get('url')

            print(f"Test Details:")
            print(f"  Type: {test_type}")
            print(f"  Interval: {interval}")
            print(f"  URL: {url}")

            # Fetch alert rules
            alert_rules = test_details.get('alertRules')
            if alert_rules:
                print("Alert Rules:")
                for rule in alert_rules:
                    rule_id = rule.get('ruleId')
                    expression = rule.get('expression')

                    print(f"  Rule ID: {rule_id}")
                    print(f"  Expression: {expression}")
            else:
                print("No Alert Rules found for this test.")
        else:
            print(f"Failed to fetch details for test {test_id}")

if __name__ == '__main__':
    api_token = 'be3c0eca-369a-4b85-9396-8300372f9038:'

    tests = fetch_thousandeyes_tests(api_token)
    if tests:
        enabled_tests = extract_enabled_tests(tests)
        if enabled_tests:
            analyze_enabled_tests(enabled_tests, api_token)
        else:
            print("No enabled tests found.")

