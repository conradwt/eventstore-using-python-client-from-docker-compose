import json
import os
from flask import Flask, request
from dataclasses import dataclass
from esdbclient import EventStoreDBClient, NewEvent, StreamState
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

def get_ca_certificate(certificate_path: str) -> str:
  current_dir = os.getcwd()

  ca_cert_path = os.path.join(current_dir, certificate_path)

  # print(ca_cert_path, flush=True)

  with open(ca_cert_path, "rt") as f:
    return f.read()

event_store = EventStoreDBClient(
  uri=os.getenv('EVENTSTORE_URL'),
  root_certificates=get_ca_certificate('/certs/ca/ca.crt')
)

visitors_stream = 'visitors-stream'

@app.route('/hello-world')
def hello_world():
  @dataclass
  class VisitorGreeted:
    visitor: str

  visitor = request.args.get('visitor', 'Visitor')
  visitor_greeted = VisitorGreeted(visitor=visitor)

  event_data = NewEvent(
    type='VisitorGreeted',
    data=json.dumps(visitor_greeted.__dict__).encode('utf-8')
  )

  append_result = event_store.append_to_stream(
    stream_name=visitors_stream,
    current_version=StreamState.ANY,
    events=[event_data],
  )

  event_stream = event_store.get_stream(
    stream_name=visitors_stream,
    stream_position=0,
  )

  visitors_greeted = []
  for event in event_stream:
    visitors_greeted.append(VisitorGreeted(**json.loads(event.data)).visitor)

  return f"{len(visitors_greeted)} visitors have been greeted, they are: [{','.join(visitors_greeted)}]"

# serve(app, host='0.0.0.0', port=8080)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
