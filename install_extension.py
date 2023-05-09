import os

linux_commands = [
  "apt -y update -qq",
  "wget http://launchpadlibrarian.net/367274644/libgoogle-perftools-dev_2.5-2.2ubuntu3_amd64.deb",
  "wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/google-perftools_2.5-2.2ubuntu3_all.deb",
  "wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/libtcmalloc-minimal4_2.5-2.2ubuntu3_amd64.deb",
  "wget https://launchpad.net/ubuntu/+source/google-perftools/2.5-2.2ubuntu3/+build/14795286/+files/libgoogle-perftools4_2.5-2.2ubuntu3_amd64.deb",
  "apt install -qq libunwind8-dev",
  "dpkg -i *.deb",
  "env LD_PRELOAD=libtcmalloc.so",
  "ls /content/",
  "rm *.deb",
  "pip install -q torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1+cu118 torchtext==0.15.1 torchdata==0.6.0 --extra-index-url https://download.pytorch.org/whl/cu118 -U",
  "apt -y install -qq aria2 libcairo2-dev pkg-config python3-dev",
  "pip install -q xformers==0.0.19 triton==2.0.0 -U",
  "git clone -b v2.2 https://github.com/camenduru/stable-diffusion-webui",
  "wget https://raw.githubusercontent.com/camenduru/stable-diffusion-webui-scripts/main/run_n_times.py -O /content/stable-diffusion-webui/scripts/run_n_times.py",
  "git clone https://github.com/AlUlkesh/stable-diffusion-webui-images-browser /content/stable-diffusion-webui/extensions/stable-diffusion-webui-images-browser",
  "git clone https://github.com/KohakuBlueleaf/a1111-sd-webui-locon  /content/stable-diffusion-webui/extensions/a1111-sd-webui-locon",
  "git clone https://github.com/camenduru/stable-diffusion-webui-huggingface /content/stable-diffusion-webui/extensions/stable-diffusion-webui-huggingface",
  "git clone -b v2.0 https://github.com/camenduru/sd-civitai-browser /content/stable-diffusion-webui/extensions/sd-civitai-browser",
  "git clone https://github.com/kohya-ss/sd-webui-additional-networks /content/stable-diffusion-webui/extensions/sd-webui-additional-networks",
  "git clone https://github.com/Mikubill/sd-webui-controlnet /content/stable-diffusion-webui/extensions/sd-webui-controlnet",
  "git clone https://github.com/camenduru/openpose-editor /content/stable-diffusion-webui/extensions/openpose-editor",
  "git clone https://github.com/jexom/sd-webui-depth-lib /content/stable-diffusion-webui/extensions/sd-webui-depth-lib",
  "git clone https://github.com/hnmr293/posex /content/stable-diffusion-webui/extensions/posex",
  "git clone https://github.com/camenduru/sd-webui-tunnels /content/stable-diffusion-webui/extensions/sd-webui-tunnels",
  "git clone https://github.com/etherealxx/batchlinks-webui /content/stable-diffusion-webui/extensions/batchlinks-webui",
  "git clone https://github.com/hnmr293/sd-webui-cutoff /content/stable-diffusion-webui/extensions/sd-webui-cutoff",
  "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg /content/stable-diffusion-webui/extensions/stable-diffusion-webui-rembg",
  "git clone https://github.com/adieyal/sd-dynamic-prompts /content/stable-diffusion-webui/extensions/sd-dynamic-prompts",
  "git clone https://github.com/hako-mikan/sd-webui-regional-prompter /content/stable-diffusion-webui/extensions/sd-webui-regional-prompter",
  "git clone https://github.com/deforum-art/sd-webui-deforum /content/stable-diffusion-webui/extensions/deforum",
  "git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111 /content/stable-diffusion-webui/extensions/ultimate-upscale-for-automatic1111"
]

for command in linux_commands:
  os.system(command)

os.chdir("/content/stable-diffusion-webui/")
os.system("git reset --hard")
