# rust-chariott Container

Container images used to build rust-chariott

## Building the Container

Build the chariott container:
```bash
podman build -f images/chariott/Containerfile -t rust-chariott:fed38-latest .
```
  
By default the image will built with a frozen static hashcommit. However is possible to build
with other version by specifying the `VERSION` variable during the build, e.g:  

```bash
podman build -f images/chariott/Containerfile --build-arg VERSION=main -t rust-chariott:fed38-latest .
```
_The above command will build the container using the `main` branch from the [chariott github project.](https://github.com/eclipse-chariott/chariott)_
