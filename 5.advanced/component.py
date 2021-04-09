import kfp.dsl as dsl


def print_op(msg):
    return dsl.ContainerOp(
        name='Print',
        image='alpine:3.6',
        command=['echo', msg],
    )
