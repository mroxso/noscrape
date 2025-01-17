# noscrape

noscrape is a tool for scraping events from a Nostr relay and relaying them to another Nostr relay. It uses websockets to connect to both the source and target relays and transfers events in real-time.

## Features

- Connects to a source Nostr relay and subscribes to all events.
- Relays received events to a target Nostr relay.
- Configurable source and target relay URLs via environment variables.
- Dockerized for easy deployment.

## Requirements

- Python 3.11
- `websockets` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/noscrape.git
    cd noscrape
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Set the environment variables for the source and target relay URLs:
    ```sh
    export SOURCE_RELAY_URL=wss://relay.nostr.band
    export TARGET_RELAY_URL=ws://localhost:7777
    ```

2. Run the application:
    ```sh
    python main.py
    ```

## Docker

You can also run the application using Docker and Docker Compose.

1. Build and start the Docker containers:
    ```sh
    docker-compose up --build
    ```

2. The application will connect to the source relay and start relaying events to the target relay.

## Configuration

The strfry.conf file contains the configuration for the target relay. You can modify this file to change the relay settings.