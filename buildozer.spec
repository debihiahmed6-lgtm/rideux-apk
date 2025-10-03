[app]
# اسم التطبيق
title = RideuxCalculator
package.name = rideuxcalculator
package.domain = org.debihi
source.dir = .
source.include_exts = py,png,jpg,kv,txt
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
# النسخة التي تريد أن تكون مستهدفة على Android
android.arch = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
# مسار المجلد المؤقت أثناء البناء
build_dir = ./build
# المسار النهائي للـ APK
bin_dir = ./bin

[android]
# إعدادات متقدمة إن احتجت لتغييرها لاحقاً
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
