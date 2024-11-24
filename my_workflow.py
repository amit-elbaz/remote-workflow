
import mlrun
from kfp import dsl
from kfp.dsl import ContainerOp


@dsl.pipeline()
def kfpipeline():
    project = mlrun.get_current_project()
    func = project.get_function("func")
    func.with_node_selection(node_selector={"app.iguazio.com/node-group": "added-spot"})
    func.save()
    # step = func.run().set_retry(policy="Always",num_retries=1)
    # Put the kfp pod on a constant node
    
    step = mlrun.run_function(name="step1", function="func")
    # step.node_selector={"app.iguazio.com/node-group": "added-ondemand"}
    
    
