import boto3.ec2
conn=boto3.resource('ec2',region_name='us-east-1')
ec2_client=boto3.client('ec2')
Ami_list = ['Amazon_linux', 'Redhat', 'SUSE Linux Enterprise', 'ubuntu server', 'windows']
Ami_dict={'Amazon_linux':'ami-22ce4934','Redhat':'ami-b63769a1','SUSE Linux Enterprise':'ami-fde4ebea','ubuntu server':'ami-f4cc1de2','windows':'ami-b6af04a0'}
Instance_types=['t2.nano','t2.micro','t2.small','t2.medium']
min_count=1
max_count=1
num=1
def creation():
        Ami_selection=int(input('Select the instances you would like to launch \n 1.Amazon linux \n 2.Redhat \n 3.SUSE Linux Enterprise \n 4.ubuntu server \n 5.Windows \n'))
        Type_selection=int(input('Select the instance type \n 1. t2.nano\n 2. t2.micro \n 3.t2.small \n 4.t2.medium \n'))
        min_count=int(input('Enter the min count: \n'))
        max_count = int(input('Enter the max count: \n'))
        conn.create_instances(ImageId=Ami_dict[Ami_list[Ami_selection-1]],MinCount=min_count,
                              MaxCount=max_count, InstanceType=Instance_types[Type_selection-1])
        waiter=ec2_client.get_waiter('instance_running')
        instances = conn.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        for instance in instances:
            print('instance details', instance.image_id, instance.id, instance.instance_type, instance.kernel_id,instance.architecture,instance.platform)
 


def stop():
    list1=[]
    list2=[]
    num=1
    instances_1 = conn.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances_1:
        list1.append(instance.id)
    print('select the instance ID you want to stop \n')
    for x in list1:
        print(str(num) + '.' + x + '\n')
        num = int(num) + 1
    value_stop=int(input('Enter the number here: \n'))
    list2.append(list1[value_stop-1])
    conn.instances.filter(InstanceIds=list2).stop()
def terminate():
    num=1
    list1=[]
    list2=[]
    instances_2 = conn.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    for instance in instances_2:
        list1.append(instance.id)
    print('select the instance ID you want to stop \n')
    for x in list1:
        print(str(num) + '.' + x + '\n')
        num = int(num) + 1
    value_stop=int(input('Enter the number here: \n'))
    list2.append(list1[value_stop-1])
    conn.instances.filter(InstanceIds=list2).stop()

def userchoice():
    choice = input(
        'Select your desired operation: \n 1.Create instances \n 2.stop instances \n 3.Terminate instances \n')
    if (choice == 1):
        creation()
    elif (choice == 2):
        stop()
        instances = conn.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
        for instance in instances:
            print('instance details', instance.image_id, instance.id, instance.instance_type, instance.kernel_id,instance.architecture,instance.platform)
    elif (choice == 3):
        terminate()
        instances = conn.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['terminated']}])
        for instance in instances:
            print('instance details', instance.image_id, instance.id, instance.instance_type, instance.kernel_id,
                  instance.architecture, instance.platform)
userchoice()
'''flag='NO'



flag=input('Do you want to continue?: \n YES \n NO')
while(flag=='YES'):
    userchoice()
    
#flag=input('Do you want to continue?')
print('this is instance status',ec2_client.describe_instance_status())
#waiter=ec2_client.get_waiter('instance_running')
#time.sleep(10)
instances = conn.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
for instance in instances:
   print('instance details',instance.image_id,instance.id, instance.instance_type,instance.kernel_id,instance.architecture,instance.platform)
'''