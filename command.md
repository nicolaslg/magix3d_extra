```shell
podman pull ghcr.io/lihpc-computational-geometry/spack-magix3d:latest
```

```shell
podman run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --device /dev/dri ghcr.io/lihpc-computational-geometry/spack-magix3d:latest
```

=========================
```shell
# to mount the magix3d_extra located in the current directory at mount point /magix3d_extra
# replace the $PWD by the path of your choice if needed
podman run -v $PWD/magix3d_extra:/magix3d_extra -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --device /dev/dri ghcr.io/lihpc-computational-geometry/spack-magix3d:latest
```

=========================
```shell
# to change the entrypoint
podman run --entrypoint "/bin/bash" -it -v $PWD/magix3d_extra:/magix3d_extra -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --device /dev/dri ghcr.io/lihpc-computational-geometry/spack-magix3d:latest
```

```shell
# then magix3d can be launched using
/spack/opt/spack/linux-ubuntu22.04-x86_64/gcc-11.4.0/magix3d-2.3.3-z57amcgvwdwfppmmgxrqrev2yenzmvwu/bin/Magix3D
```
