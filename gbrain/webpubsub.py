from azure.messaging.webpubsubservice import WebPubSubServiceClient
from azure.identity import DefaultAzureCredential

##
hub = "myHub1"
service_client = WebPubSubServiceClient(
    endpoint="<endpoint>", credential=DefaultAzureCredential(), hub=hub
)

token = service_client.get_client_access_token(user_id="user1")

service_client.send_to_all("<message>", content_type="text/plain")

service_client.send_to_group("group1", "Hello, Group!", content_type="text/plain")

service_client.user_exists("user1")
