import os 

linux_commands = [
  "mkdir /content/stable-diffusion-webui/models/hypernetworks/",
  "mkdir /content/stable-diffusion-webui/models/Lora/",
  "cp -r /content/drive/MyDrive/SD_FILE/embedding/*.pt /content/stable-diffusion-webui/embeddings/",
  "cp -r /content/drive/MyDrive/SD_FILE/embedding/*.safetensors /content/stable-diffusion-webui/embeddings/",
  "cp -r /content/drive/MyDrive/SD_FILE/hypernet/*.pt /content/stable-diffusion-webui/models/hypernetworks/",
  "cp -r /content/drive/MyDrive/SD_FILE/vae/*.pt /content/stable-diffusion-webui/models/VAE/",
  "cp -r /content/drive/MyDrive/SD_FILE/vae/*.ckpt /content/stable-diffusion-webui/models/VAE/",
  "cp -r /content/drive/MyDrive/SD_FILE/lora/*.safetensors /content/stable-diffusion-webui/models/Lora/",
  "cp -r /content/drive/MyDrive/SD_FILE/embedding/*.png /content/stable-diffusion-webui/embeddings/",
  "cp -r /content/drive/MyDrive/SD_FILE/hypernet/*.png /content/stable-diffusion-webui/models/hypernetworks/",
  "cp -r /content/drive/MyDrive/SD_FILE/lora/*.png /content/stable-diffusion-webui/models/Lora/",
  "cp -r /content/drive/MyDrive/AI-Model-2022/*.png /content/stable-diffusion-webui/models/Stable-diffusion/"
]

for command in linux_commands:
  os.system(command)