from component import print_op

import kfp.dsl as dsl


@dsl.pipeline(
    name="mnist_pipeline",
    description="mnist_pipeline with pv and pvc"
)
def mnist_pipeline(epochs):
    registry = 'ckwlsgur20'
    img_name = 'mnist'
    img_ver = '4.0v'

    train_test_step = dsl.ContainerOp(
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

    baseline = 0.99
    with dsl.Condition(train_test_step.outputs['accuracy'] > baseline):
        print_op('accuracy is higher than {}'.format(baseline))
    with dsl.Condition(train_test_step.outputs['accuracy'] <= baseline):
        print_op('accuracy is lower than {}'.format(baseline))
