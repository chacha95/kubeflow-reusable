import kfp.dsl as dsl


def build_dockerfile(dockerfile_dir='/mnt/docker/Dockerfile', registry='ckwlsgur20', img_name='test', ver='1.0v'):
    command = "docker build -t {}:{} {}".format(img_name, ver, dockerfile_dir)

    return dsl.ContainerOp(
        name='build image and push to registry',
        image='docker:dind',
        command=command,
        pvolumes={
            "/mnt": dsl.PipelineVolume(pvc="kubeflow")
        },
    )
