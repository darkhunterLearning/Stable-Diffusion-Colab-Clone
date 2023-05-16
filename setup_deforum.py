import os 

linux_commands = [
  "git clone https://github.com/deforum-art/sd-webui-deforum /content/stable-diffusion-webui/extensions/deforum"
]

for command in linux_commands:
  os.system(command)
