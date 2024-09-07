# Python Sample: Hello, World!

This guide shows you how to stand up a sample Hello World application, built with [Flask](https://flask.palletsprojects.com/en/3.0.x/), that connects to EventStoreDB.

The sample exposes a simple HTTP endpoint `http://localhost:8080/hello-world?visitor={visitor}` that shows how to append to and read from a stream in EventStoreDB.

When a visitor says hello via `hello-world?visitor={visitor}`, an event is appended to a stream to record the fact they have been greeted.

The stream is then read from beginning to end to return the full log of visitors on each call to `/hello-world?visitor={visitor}`.

You can see how this is done in the source code [here](./main.py).

## Getting Started

## Software requirements

- Docker Desktop 4.34.0 or newer

- Python 3.12 or newer

Note: This tutorial was updated on macOS 14.6.1.

## Running The Sample

1. Clone the repository:

   ```
   git clone https://github.com/conradwt/eventstore-using-python-client-from-docker-compose.git
   cd eventstore-using-python-client-from-docker-compose
   ```

2. create development.env file

   ```zsh
   cp development.env.example development.env
   ```

3. Run the application and database using Docker Compose:

   ```
   docker compose up -d
   ```

4. Verify the containers are up and running:

   ```zsh
   docker compose ps
   ```

   The results should look something like the following:

   ```text
    NAME               IMAGE                                        COMMAND                  SERVICE            CREATED          STATUS                    PORTS
    eventstore-using-python-client-from-docker-compose-app-1   esdb-sample-python                           "gunicorn -w 4 -b 0.…"   app                2 minutes ago   Up About a minute        0.0.0.0:8080->8080/tcp
    node1.eventstore   eventstore/eventstore:24.6.0-alpha-arm64v8   "/opt/eventstore/Eve…"   node1.eventstore   11 seconds ago   Up 10 seconds (healthy)   1112-1113/tcp, 0.0.0.0:2111->2113/tcp
    node2.eventstore   eventstore/eventstore:24.6.0-alpha-arm64v8   "/opt/eventstore/Eve…"   node2.eventstore   11 seconds ago   Up 10 seconds (healthy)   1112-1113/tcp, 0.0.0.0:2112->2113/tcp
    node3.eventstore   eventstore/eventstore:24.6.0-alpha-arm64v8   "/opt/eventstore/Eve…"   node3.eventstore   11 seconds ago   Up 10 seconds (healthy)   1112-1113/tcp, 0.0.0.0:2113->2113/tcp
   ```

5. Test the application:

   Say hello as `Ouro`:

   ```zsh
   curl "localhost:8080/hello-world?visitor=Ouro"
   ```

   The results should look something like the following:

   ```text
   1 visitors have been greeted, they are: [Ouro]
   ```

   Say hello as `YourName`:

   ```zsh
   curl "localhost:8080/hello-world?visitor=YourName"
   ```

   The results should look something like the following:

   ```text
   2 visitors have been greeted, they are: [Ouro, YourName]
   ```

6. To stop and remove the containers, use:

   ```zsh
   docker compose down
   ```

## Additional Information

For more in-depth and detailed examples of using EventStoreDB and the Python Client, refer to:

- EventStoreDB: [Getting Started With EventStoreDB](https://developers.eventstore.com/clients/grpc/)
- Python Client: [Python Client Samples](https://github.com/pyeventsourcing/esdbclient/tree/1.0)
