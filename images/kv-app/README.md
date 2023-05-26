# rust-chariott kv-app Container

Container image used to build rust-chariott kv-app  

[Key-Value Store Application aka kv-app](https://github.com/eclipse-chariott/chariott/tree/main/examples/applications/kv-app) is a chariott utility with capability to read and write an in-memory key-value store. 

_The kv-app container needs rust-chariott running, in order to properly connect and create the channel registration_
  
## Building the Container Image

Build the chariott container:
```bash
podman build -f images/kv-app/Containerfile -t rust-kv-app:fed38-latest .
```
  
By default the image will built with a frozen static hashcommit. However is possible to build
with other version by specifying the `VERSION` variable during the build, e.g:  

```bash
podman build -f images/kv-app/Containerfile --build-arg VERSION=main -t rust-kv-app:fed38-latest .
```
_The above command will build the kv-app container using the `main` branch from the [chariott github project.](https://github.com/eclipse-chariott/chariott)_

## Running the Container

_Running the local built container image_
```bash
podman run --name kv-app --rm -p 50064:50064 localhost/rust-kv-app:fed38-latest
```
