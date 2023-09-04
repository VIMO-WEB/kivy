[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mykivyapp

# (str) Source code where the main.py lives
source.dir = .

# (list) Application requirements
requirements = python3==3.7.6,hostpython3==3.7.6,kivy,pillow

# (str) Version of your application
version = 1.0.0  # Replace with your desired version number

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (str) Path to build artifact storage, absolute or relative to the spec file
# build_dir = ./.buildozer

# (str) Path to build python (if different from the system)
# build_dir = /usr/bin/python3
osx.python_version = 3

[android]

# (str) Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
arch = armeabi-v7a

# (str) Android API to use, default is the latest available
# target = android-28

# (int) Minimum API required (8, 9, 14, 21, ..)
minapi = 21

# (int) Android NDK version to use
android.ndk = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True
