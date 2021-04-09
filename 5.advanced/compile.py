from datetime import datetime
from pipeline import mnist_pipeline

import kfp
import kfp.compiler as compiler


if __name__ == "__main__":
    pipeline_func = mnist_pipeline
    ExpName = '5.advanced'
    Args = {"epochs": 10}

    # compile pipeline
    runtime = '{}'.format(datetime.now().strftime("%Y%m%d %H%M%S"))
    run_name = pipeline_func.__name__ + ' run ' + runtime
    kfp.compiler.Compiler().compile(pipeline_func, '{}.zip'.format(ExpName))
