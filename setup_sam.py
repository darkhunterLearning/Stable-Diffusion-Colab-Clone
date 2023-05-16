import os

linux_commands = [
        "git clone https://github.com/continue-revolution/sd-webui-segment-anything /content/stable-diffusion-webui/extensions/sd-webui-segment-anything",
        "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/Wang-Dong/SAM-vit-h/resolve/main/sam_vit_h_4b8939.pth -d /content/stable-diffusion-webui/extensions/sd-webui-segment-anything/models/sam -o sam_vit_h_4b8939.pth\n"
]

for command in linux_commands:
  os.system(command)
