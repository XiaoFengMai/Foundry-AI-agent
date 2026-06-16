# Before running the sample:
#    pip install azure-ai-projects>=2.1.0

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://xiaofengmai-foundry-pro-resource.services.ai.azure.com/api/projects/xiaofengmai-foundry-project"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "computing-history"
my_version = "1"

openai_client = project_client.get_openai_client()

while True:
    user_prompt = input("Enter a prompt for the agent (or type 'quit' to exit): ").strip()

    if user_prompt.lower() == "quit":
        break

    response = openai_client.responses.create(
        input=[{"role": "user", "content": user_prompt}],
        extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
    )

    print(f"Response output: {response.output_text}")



