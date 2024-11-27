
import mlrun
from kfp import dsl
from kfp.dsl import ContainerOp


# @dsl.pipeline()
# def kfpipeline(preemption_mode=None, node_selector=None):
#     project = mlrun.get_current_project()
#     func = project.get_function("my-func")
#     if preemption_mode:
#         func.with_preemption_mode(str(preemption_mode))
#     if node_selector:
#         func.with_node_selection(node_selector=dict(node_selector))
#     func.save()
#     # step = func.run().set_retry(policy="Always",num_retries=1)
#     # Put the kfp pod on a constant node
    
#     step = mlrun.run_function(name="step1", function="my-func")
#     # step = func.run()
#     # step.node_selector={"app.iguazio.com/node-group": "added-ondemand"}

@dsl.pipeline()
def kfpipeline():
    project = mlrun.get_current_project()
    func_allow = project.get_function("my-func-allow")
    func_prevent = project.get_function("my-func-prevent")
    func_constrain = project.get_function("my-func-constrain")
    
    func_allow.with_preemption_mode("allow")
    func_prevent.with_preemption_mode("prevent")
    func_constrain.with_preemption_mode("constrain")
    
    func_allow.save()
    func_prevent.save()
    func_constrain.save()
    
    allow_step = mlrun.run_function(name="allow_func", function="my-func-allow")
    prevent_step = mlrun.run_function(name="prevent_func", function="my-func-prevent")
    constrain_step = mlrun.run_function(name="constrain_func", function="my-func-constrain")
    
