import os 

linux_commands = [
  "aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/embed/upscale/resolve/main/4x-UltraSharp.pth -d /content/stable-diffusion-webui/models/ESRGAN -o 4x-UltraSharp.pth",
  "cp -r /content/drive/MyDrive/SD_FILE/config/*.json /content/stable-diffusion-webui",
  "sed -i -e '''/    prepare_environment()/a\    os.system\(f\"\"\"sed -i -e ''\"s/dict()))/dict())).cuda()/g\"'' /content/stable-diffusion-webui/repositories/stable-diffusion-stability-ai/ldm/util.py\"\"\")''' /content/stable-diffusion-webui/launch.py",
  "sed -i -e 's/\\\"sd_model_checkpoint\\\"\\,/\\\"sd_model_checkpoint\\,sd_vae\\,CLIP_stop_at_last_layers\\\"\\,/g' /content/stable-diffusion-webui/modules/shared.py",
  "sed -i -e 's/fastapi==0.90.1/fastapi==0.89.1/g' /content/stable-diffusion-webui/requirements_versions.txt"
]

for command in linux_commands:
  os.system(command)