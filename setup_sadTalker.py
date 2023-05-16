import os 

linux_commands = [
  "git clone -b dev https://github.com/camenduru/SadTalker /content/stable-diffusion-webui/extensions/SadTalker",
  "mkdir /content/stable-diffusion-webui/extensions/SadTalker/checkpoints/",
  "git -C /content/stable-diffusion-webui/extensions/SadTalker/checkpoints clone https://huggingface.co/camenduru/SadTalker"
]

for command in linux_commands:
  os.system(command)
