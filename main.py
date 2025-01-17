import asyncio
import json
import websockets
import os

async def relay_events(source_relay_url, target_relay_url):
    async with websockets.connect(source_relay_url) as source_ws, \
               websockets.connect(target_relay_url) as target_ws:
        # Subscribe to all events from the source relay
        subscription_message = json.dumps(["REQ", "subscription_id", {"kinds": [1]}])
        await source_ws.send(subscription_message)

        while True:
            try:
                # Receive event from the source relay
                event_message = await source_ws.recv()
                event = json.loads(event_message)

                print(f"Received event: ")
                print(event)
                print("----------------")

                # Check if the message is an EVENT type
                if event[0] == "EVENT":
                    # Publish the event to the target relay
                    publish_message = json.dumps(["EVENT", event[2]])
                    await target_ws.send(publish_message)

            except websockets.ConnectionClosed:
                print("Connection closed. Reconnecting...")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                break

if __name__ == "__main__":
    source_relay_url = os.getenv('SOURCE_RELAY_URL', "wss://relay.nostr.band")
    target_relay_url = os.getenv('TARGET_RELAY_URL', "ws://localhost:7777")
    
    while True:
        try:
            asyncio.run(relay_events(source_relay_url, target_relay_url))
        except Exception as e:
            print(f"An error occurred in relay_events: {e}")
        print("Reconnecting in 5 seconds...")
        asyncio.sleep(5)