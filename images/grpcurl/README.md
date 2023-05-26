# grpcurl Container

Container file to a build a container image used as toolbox to play with chariott using grpcurl 

## Building the Container Image

Build the chariott container:
```bash
podman build -f images/grpcurl/Containerfile -t grpcurl:fed38-latest .
```
  
## Running the Container

_Running and attaching into the local built container image_
```bash
podman run --name grpcurl -it --rm  localhost/grpcurl:fed38-latest bash
```

Once `chariott` container and `kv-app` is running, use the `grpcurl` command as demonstrated:
https://github.com/eclipse-chariott/chariott/tree/main/examples/applications/kv-app  
  
e.g:  

```bash
grpcurl -plaintext -d @ 0.0.0.0:4243 chariott.runtime.v1.ChariottService/Fulfill <<EOF
{
  "namespace": "sdv.kvs",
  "intent": {
    "write": {
      "key": "date-time",
      "value": {
        "string": "$(date)"
      }
    }
  }
}
EOF
```

Read a value key with:  

```bash
grpcurl -plaintext -d @ 0.0.0.0:4243 chariott.runtime.v1.ChariottService/Fulfill <<EOF
{
  "namespace": "sdv.kvs",
  "intent": {
    "read": {
      "key": "date-time"
    }
  }
}
EOF
```
