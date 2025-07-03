# Dump-The-Dump

> **TriggerServerEvent Grabber for FiveM Server Dumps**


![Showcase]((https://i.imgur.com/9fcwRES.gif)




Dump-The-Dump is a Python tool that scans a FiveM server dump folder and automatically extracts all `TriggerServerEvent` calls used in the server’s Lua scripts. It can process an entire dump in just a few seconds, generating a list of discovered triggers useful for developers, reverse engineering, or building scripts for executors.

---

## ✨ Features

✅ Fast scanning of large dump folders  
✅ Extracts all `TriggerServerEvent` lines from `.lua` files  
✅ Automatically filters duplicates  
✅ Saves results to a text file (`grabbed.txt`)  
✅ Simple command-line interface  

---

## ⚙️ How It Works

- Provide a path to a dump folder.
- The script scans all `.lua` files (even in subfolders).
- It finds lines containing `TriggerServerEvent`.
- Cleans and formats those lines.
- Saves unique triggers to `grabbed.txt`.

Example output in `grabbed.txt`:
TriggerServerEvent("esx_taxijob:success")
TriggerServerEvent('gg_lootcases:rewardPlayer')



---

## 💻 Requirements

- Python 3.x

No additional libraries required.

---

## ⚠️ Disclaimer

This tool is provided for **educational and research purposes only.** Usage of this tool on servers you do not own or have permission to analyze **may violate laws or terms of service.** The author is not responsible for misuse of this software.

---

## 📄 License

MIT License

---

Made with ❤️ by [@iAvra](https://github.com/iavrash)
