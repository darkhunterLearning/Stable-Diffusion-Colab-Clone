import os
os.chdir("/content/stable-diffusion-webui")
os.system("python launch.py --listen --xformers --enable-insecure-extension-access --theme dark --gradio-queue --multiple --ckpt-dir /content/drive/MyDrive/AI-Model-2022/ --no-half-vae --disable-nan-check")