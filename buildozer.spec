[app]
title = ماشین حساب
package.name = calculator
package.domain = org.mbb
source.dir = .
source.include_exts = ttf,txt,py,kv,jpg,png,mp3,json
version = 3.0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0   ; جلوگیری از خطای root

[android]
android.api = 33          ; نسخه پایدارتر برای SDK
android.minapi = 21
android.ndk = 23b
android.ndk_api = 21
android.permissions = READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True   ; جلوگیری از خطای لایسنس
