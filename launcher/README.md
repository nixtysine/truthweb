# TruthWeb Launcher

A comprehensive Minecraft server management tool with advanced features for server administrators and developers.

## Features

- **Multi-Server Management** - Create and organize unlimited server profiles
- **Live Console** - Real-time server output monitoring with RCON support
- **Version Control** - Automatic detection of Minecraft versions and mod loaders (Fabric, Forge, NeoForge, OptiFine)
- **System Tray Integration** - Run servers in the background
- **Multi-Language Support** - Extensible translation system
- **Server Conflict Detection** - Automatically detects and manages running servers

## Requirements

- Windows 10/11
- Java Runtime Environment

## Installation

1. Download the latest release
2. Extract to your desired location
3. Run `twlauncher.exe`

## Quick Start

1. Launch the application
2. Click `Servers` → `+` to add your first server
3. Browse to your server folder and configure settings
4. Select your server and click "Launch"

### Server Management
- Add servers by browsing to server folders containing the Minecraft server `.jar` files
- Edit server properties (IP, port, MOTD, description)
- Automatic version and mod loader detection
- Safe server deletion (moved to recycle bin)

### Console Features
- Real-time server output with auto-scroll
- Send commands via RCON or stdin
- Graceful server start/stop
- Optional log file output in settings

### Settings
- Language selection with completion status
- Color schemes
- UI theme selection
- Advanced server logging options

## Troubleshooting

**Java not found**: This error occurs when the launcher cannot locate a Java Runtime Environment on your system. To resolve this, download and install the latest Java JRE from Oracle's official website or use OpenJDK. After installation, ensure Java is properly added to your system's PATH environment variable. You can verify the installation by opening a command prompt and typing `java -version`. If you still encounter issues, try reinstalling Java with administrator privileges or manually adding the Java installation directory to your PATH.

**Server won't start**: When servers fail to launch, the most common causes are insufficient folder permissions or Java configuration issues. First, ensure the launcher has read/write access to your server directory - try running the launcher as administrator if necessary. If you have an extrenal drive or network drive, check hardware and/or connectivity. Verify that your server JAR file is not corrupted and that you have sufficient system resources (RAM/CPU) available. Check that no other processes are using the same port as your server. If the problem persists, examine the server console output for specific error messages that can help identify the root cause.

**Translation issues**: Language display problems typically stem from corrupted or incomplete translation files. Navigate to the Settings menu and verify your selected language shows a complete translation percentage. If issues persist, try switching to English (which is always 100% complete) temporarily, then back to your preferred language. You can also check the application's language files directory for any missing or damaged files. Restart the launcher after making language changes to ensure proper loading of translation resources.

## Support

- Website: [1truth.me](https://1truth.me/)
- Discord: [TruthWeb](https://discord.gg/jZDPPrV)
- GitHub (Here): [nixtysine](https://github.com/nixtysine)

## License

Copyright (c) 2017-2024 1Truth - All rights reserved.

This software is proprietary. Unauthorized copying or distribution is prohibited.
