python

# instance_manager.py

from google.cloud import compute_v1

def list_instances(project, zone):
    instance_client = compute_v1.InstancesClient()
    request = compute_v1.ListInstancesRequest(project=project, zone=zone)
    response = instance_client.list(request=request)

    for instance in response:
        print(f"Instance: {instance.name} | Status: {instance.status}")

def start_instance(project, zone, instance_name):
    instance_client = compute_v1.InstancesClient()
    operation = instance_client.start_unary(project=project, zone=zone, instance=instance_name)
    operation.result()
    print(f"✅ Started instance: {instance_name}")

def stop_instance(project, zone, instance_name):
    instance_client = compute_v1.InstancesClient()
    operation = instance_client.stop_unary(project=project, zone=zone, instance=instance_name)
    operation.result()
    print(f"🛑 Stopped instance: {instance_name}")
