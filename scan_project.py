#!/usr/bin/env python3
import os
import shutil

# مسار المشروع الحالي
project_path = os.getcwd()

# المجلد الجديد لحفظ الملفات المهمة
output_folder = os.path.join(project_path, "project_files")
os.makedirs(output_folder, exist_ok=True)

# امتدادات الملفات المهمة
important_exts = [".py", ".kv", ".spec", ".txt"]

# البحث ونسخ الملفات المهمة
print("📂 البحث عن الملفات المهمة داخل المشروع...\n")
found_files = []

for root, dirs, files in os.walk(project_path):
    for file in files:
        if any(file.endswith(ext) for ext in important_exts):
            full_path = os.path.join(root, file)
            found_files.append(full_path)
            # نسخ الملف إلى مجلد project_files مع الاحتفاظ بالمسار النسبي
            rel_path = os.path.relpath(root, project_path)
            dest_dir = os.path.join(output_folder, rel_path)
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy2(full_path, os.path.join(dest_dir, file))

# عرض النتائج
if found_files:
    print("✅ الملفات المهمة التي تم العثور عليها:")
    for f in found_files:
        print(f" - {f}")
    print(f"\n📁 تم نسخ الملفات المهمة إلى: {output_folder}")
else:
    print("⚠️ لم يتم العثور على أي ملفات مهمة.")
