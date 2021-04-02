import kfp
import kfp.dsl as dsl
import kfp.compiler as compiler


def print_op(msg):
    return dsl.ContainerOp(
        name='Print',
        image='alpine:3.6',
        command=['echo', msg],
    )


@dsl.pipeline(
    name="mnist_pipeline",
    description="mnist_pipeline with pv and pvc"
)
def mnist_pipeline():
    train_test_step = dsl.ContainerOp(
        name="train and test",
        image="ckwlsgur20/mnist:2.5v",
        arguments=[
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


if __name__ == "__main__":
    from datetime import datetime
    # hyper-parameters
    pipeline_func = mnist_pipeline
    experiment_name = '4.pytorch-mnist'
    arguments = {}
    RUN_NUM = '{}'.format(datetime.now().strftime("%Y%m%d %H%M%S"))

    # compile pipeline
    run_name = pipeline_func.__name__ + ' run ' + RUN_NUM
    kfp.compiler.Compiler().compile(pipeline_func, '{}.zip'.format(experiment_name))

    # Submit pipeline to kubeflow server directly
    client = kfp.Client(host='pipelines-api.kubeflow.svc.cluster.local:8888',
                        namespace='kubeflow')
    run_result = client.create_run_from_pipeline_func(pipeline_func,
                                                      experiment_name=experiment_name,
                                                      run_name=run_name,
                                                      arguments=arguments)
