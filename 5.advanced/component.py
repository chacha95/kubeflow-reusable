import kfp.dsl as dsl


def print_op(msg):
    return dsl.ContainerOp(
        name='Print',
        image='alpine:3.6',
        command=['echo', msg],
    )


def train_test_op(registry, img_name, img_ver, epochs):
    return dsl.ContainerOp(
        name="train and test",
        image="{}/{}:{}".format(registry, img_name, img_ver),
        arguments=[
            "epochs", epochs,
        ],
        file_outputs={
            'accuracy': '/accuracy.json',
            'mlpipeline-metrics': '/mlpipeline-metrics.json'
        },
        pvolumes={
            "/mnt": dsl.PipelineVolume(pvc="kubeflow")
        },
    )
