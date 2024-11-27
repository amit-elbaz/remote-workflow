
import mlrun
from kfp import dsl
from kfp.dsl import ContainerOp


@dsl.pipeline()
def kfpipeline(preemption_mode=None, node_selector=None):
    project = mlrun.get_current_project()
    func = project.get_function("my-func")
    if preemption_mode:
        func.with_preemption_mode(str(preemption_mode))
    if node_selector:
        func.with_node_selection(node_selector=dict(node_selector))
    func.save()
    # step = func.run().set_retry(policy="Always",num_retries=1)
    # Put the kfp pod on a constant node
    
    step = mlrun.run_function(name="step1", function="my-func")
    # step = func.run()
    # step.node_selector={"app.iguazio.com/node-group": "added-ondemand"}
    
    
