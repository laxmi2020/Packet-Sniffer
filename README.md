Packet Sniffer
This project is a Packet Sniffer program written in Python. A packet sniffer is a tool that captures and analyzes data that travels over a network. It helps you understand what information is being sent and received over the internet.

What is a Packet Sniffer?
When you use the internet, your computer sends and receives lots of data. This data travels in small pieces called packets. A packet sniffer listens to the network traffic and records these packets. This can help you:

Troubleshoot problems: If your internet is slow, a packet sniffer can help you figure out what's happening.
Learn about network activity: You can see what kinds of data are being sent and where it's going.
What You Will Need
To use this packet sniffer, you will need:

Python: A programming language that allows you to run the program.
Scapy: A special tool (library) for Python that makes it easy to capture and analyze packets.
Npcap: A packet capture library for Windows that allows Scapy to capture packets.
How to Get Started
Here are the steps to set everything up:

1. Install Python
Go to python.org.
Download the version that matches your computer (Windows, Mac, or Linux).
Follow the instructions to install Python on your computer.
2. Install Npcap
Go to the Npcap website.
Click on the "Download" button to get the latest version of Npcap.
Run the installer and make sure to check the box that says "Install Npcap in WinPcap API-compatible Mode."
Follow the installation instructions to complete the setup.
3. Install Scapy
Once you have Python installed, you need to install Scapy. Here's how:

Open your command prompt (on Windows) or terminal (on Mac/Linux).

Type the following command and hit Enter:

pip install scapy

This command tells your computer to download and install the Scapy library.

4. Download the Packet Sniffer Script
Go to this GitHub repository where the Packet Sniffer code is stored.
Click on the green "Code" button and select "Download ZIP" to get all the files.
Unzip the downloaded file to a folder on your computer.
How to Run the Program
Now that you have everything set up, you can run the packet sniffer. Follow these steps:

1. Open the Command Prompt or Terminal
On Windows, search for "Command Prompt" in the Start menu.
On Mac, open "Terminal" from the Applications folder.
2. Navigate to the Folder
You need to tell your command prompt or terminal where your Packet Sniffer script is located. You can do this using the cd command (which stands for "change directory").

For example, if your Packet Sniffer is in a folder called "Packet-Sniffer" on your Desktop, you would type:

C:\Users\LENOVO> Packet-Sniffer

3. Run the Program
Now, you can start the Packet Sniffer! Type the following command and press Enter:

python Packet-Sniffer.py

The program will start running, and you will see messages about the packets it captures.

4. Stop the Program
To stop the packet sniffer, simply press Ctrl + C on your keyboard. This will end the program.

What You Will See
When the program is running, it will show you information about the packets it captures. For example, you might see:

Packet Type (UDP or TCP): This tells you what kind of packet it is.
Source and Destination IP Addresses: These show where the packet came from and where it is going.
For example:



Packet: UDP 192.168.1.34 --> 224.0.0.251
This means a UDP packet was sent from the address 192.168.1.34 to the address 224.0.0.251.

Important Notes
Administrator Permissions: You might need to run the program as an administrator, especially on Windows. Right-click the Command Prompt icon and select "Run as administrator."
Permission to Sniff: Make sure you have permission to capture packets on the network you are using. Using a packet sniffer without permission can be illegal.
Questions or Help
If you have any questions or need help using the packet sniffer, please open an issue in the Issues section of this repository. I’ll do my best to assist you!


