import requests

def fetch_agent_utilization(api_token):
    # ... (same as before)

def fetch_queue_data(api_token, agent_id):
    # ... (same as before)

def analyze_queues(queue_data):
    # ... (same as before)

if __name__ == '__main__':
    # Replace 'YOUR_API_TOKEN' with your actual ThousandEyes API token
    api_token = 'YOUR_API_TOKEN'

    # Set the agent utilization threshold (in percentage)
    utilization_threshold = 90  # Users can adjust this value as needed

    # Step 1: Fetch agent utilization data
    agent_utilization_data = fetch_agent_utilization(api_token)

    if agent_utilization_data:
        # Iterate through all agents and analyze their utilization
        for agent in agent_utilization_data:
            if agent['utilization'] > utilization_threshold:
                agent_id = agent['agentId']
                queue_data = fetch_queue_data(api_token, agent_id)
                if queue_data:
                    potential_causes = analyze_queues(queue_data)
                    if potential_causes:
                        print(f"Agent ID: {agent_id} - High Utilization: {agent['utilization']}%")
                        for cause in potential_causes:
                            print(f"  Potential Queue: {cause['queueName']}, Tests: {cause['numTests']}")
    else:
        print("Failed to fetch agent utilization data.")

