
import mlrun
from kfp import dsl
from kfp.dsl import ContainerOp

@dsl.pipeline()
def kfpipeline():
    # project = mlrun.get_current_project()
    error_step = mlrun.run_function(name="error_func", function="my-func-error")
    
    
