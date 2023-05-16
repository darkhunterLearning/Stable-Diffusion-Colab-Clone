import os

linux_commands = [
        "git clone https://github.com/hnmr293/sd-webui-cutoff /content/stable-diffusion-webui/extensions/sd-webui-cutoff",
]

for command in linux_commands:
  os.system(command)
