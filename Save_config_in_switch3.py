from netmiko import ConnectHandler  
from getpass import getpass
class SSH2():
    def __init__(self,user,password,ip):
        self.username = user
        self.password = password
        self.ip = ip
    
    def save_config(self):
        switch1 = { "host": self.ip,
			    "username": self.username,
			    "password": self.password,
			    "device_type": "cisco_ios",}
        for device in device_list:
            device_connect = ConnectHandler(**device)
            print(device_connect.find_prompt())
            command = "copy run start"
            output1 = device_connect.send_command(command)
            print(output1)
            device_connect.disconnect()
                
        with open('config_save.txt','w+') as config_save:
            config_save.write(output1)
            
    def sh_run(self):
        switch1 = { "host": self.ip,
			    "username": self.username,
			    "password": self.password,
			    "device_type": "cisco_ios",}
        device_connect = ConnectHandler(**switch1)
        print(device_connect.find_prompt())
        command = "sh run"
        output1 = device_connect.send_command(command)
        print(output1)
        device_connect.disconnect()
                
        with open('config_save.txt','w+') as config_save:
            config_save.write(output1)
            
            
class Config():
    def __init__(self,user,password):
        self.username = user
        self.password = password
    def create_vlan(self):
        switch1 = { "host": '192.168.0.253',
			    "username": self.username,
			    "password": self.password,
			    "device_type": "cisco_ios",}
        switch2 = { "host": '192.168.0.254',
			    "username": self.username,
			    "password": self.password,
			    "device_type": "cisco_ios",}
        device_list = [switch1,switch2]
        for device in device_list:
            device_connect = ConnectHandler(**device)
            print(device_connect.find_prompt())
            for i in range(2,5):
                command = ["vlan " + str(i), "name vlan" + str(i)]
                send_command = device_connect.send_config_set(command)
                print(send_command)
            device_connect.disconnect()
            
        
#x = SSH2('admin','Jaskaran12','192.168.0.253')
#x.sh_run()

y = Config('admin','Jaskaran12')
y.create_vlan()
#c.device_list()