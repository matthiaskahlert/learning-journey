---

### **Checklist: Installation and Development Environment**

#### **1. Download and Install Flutter SDK**
- **Check System Requirements**:
  - 2.5 GB free disk space
  - Git installed
  - Platform-specific requirements:
    - **Windows**: Windows 7 SP1+, PowerShell 5.0+, Git for Windows
    - **macOS**: macOS 10.14+, Xcode
    - **Linux**: 64-bit distribution, additional packages (e.g., libGLU)
- **Download SDK**:
  - Official website: [flutter.dev](https://flutter.dev)
  - Alternatively: `git clone https://github.com/flutter/flutter.git -b stable`
- **Installation**:
  - Extract ZIP (e.g., `C:\flutter`)
  - Choose a path without spaces/special characters

#### **2. Configure System Path**
- **Windows**:
  - System Settings → Environment Variables → Edit `Path`
  - Add `C:\flutter\bin`
- **macOS/Linux**:
  - Edit shell configuration file (`~/.bashrc`, `~/.zshrc`):
    ```bash
    export PATH="$PATH:/path/to/flutter/bin"
    ```
- **Verify Installation**:
  ```bash
  flutter --version
  ```

#### **3. Set Up IDE**
- **Recommended IDEs**:
  - Android Studio (incl. IntelliJ IDEA)
  - Visual Studio Code
- **Install Flutter Plugin**:
  - Android Studio: Preferences → Plugins → Search "Flutter" → Install
  - VS Code: Extensions → Search "Flutter" → Install
- **Configure SDK Path**:
  - Android Studio: Prompted after restart
  - VS Code: Command Palette → "Flutter: Configure SDK Path"

#### **4. Additional VS Code Extensions**
- **Dart Data Class Generator**: Automates data class creation
- **Flutter Widget Snippets**: Code snippets for widgets
- **Awesome Flutter Snippets**: More useful snippets
- **Error Lens**: Highlights errors/warnings in code
- **GitLens**: Advanced Git features
- **Material Icon Theme**: Icons for Flutter/Dart

#### **5. First Steps**
- **Create a Project**:
  ```bash
  flutter create my_project
  cd my_project
  flutter run
  ```
- **Perform Updates**:
  ```bash
  flutter upgrade
  ```

#### **6. Platform-Specific Setup**
- **Windows**:
  - Install Android Studio
  - Android SDK components (e.g., Emulator, Platform-Tools)
- **macOS**:
  - Install Xcode, accept license
  - Xcode Command Line Tools:
    ```bash
    sudo xcode-select --switch /Applications/Xcode.app/Contents/Developer
    sudo xcodebuild -runFirstLaunch
    ```
- **Linux**:
  - Install additional packages:
    ```bash
    sudo apt-get install clang cmake ninja-build pkg-config libgtk-3-dev liblzma-dev
    ```

#### **7. Android Studio Installation**

Android Studio is recommended for Flutter development, especially for Android apps. Follow these steps to install and configure it:

1. **Download and Install Android Studio**:
   - Visit the [official Android Studio website](https://developer.android.com/studio).
   - Download the latest version for your operating system.
   - Follow the installation instructions provided on the website.

2. **Install Flutter Plugin**:
   - Open Android Studio.
   - Navigate to `Preferences` → `Plugins`.
   - Search for "Flutter" in the Marketplace.
   - Click "Install" (the Dart plugin will be installed automatically).
   - Restart Android Studio when prompted.

3. **Configure Flutter SDK Path**:
   - After restarting, you may be prompted to configure the Flutter SDK path.
   - Select the folder where Flutter is installed (e.g., `C:\flutter\flutter`).

4. **Install Android SDK Components**:
   - Open Android Studio.
   - Navigate to `Configure` → `SDK Manager`.
   - Ensure the following components are installed:
     - Android SDK Platform (latest stable version)
     - Android SDK Command-line Tools
     - Android SDK Build-Tools
     - Android Emulator
     - Android SDK Platform-Tools

5. **Verify Installation**:
   - Open a terminal and run:
     ```bash
     flutter doctor
     ```
   - Ensure there are no issues related to the Android toolchain.