import os

linux_commands = [
        "git clone https://github.com/volotat/SD-CN-Animation /content/stable-diffusion-webui/extensions/SD-CN-Animation",
]

for command in linux_commands:
  os.system(command)
