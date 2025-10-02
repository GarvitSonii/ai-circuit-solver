from PIL import Image
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
train_dir = os.path.join(base_dir, 'split_data\\val')
print(base_dir)
print(train_dir)

list_ = []
for cls in os.listdir(train_dir):
    cls_path = os.path.join(train_dir, cls)
    print(cls_path)
    for f in os.listdir(cls_path):
        if f.lower().endswith('.bmp'):
            img_path = os.path.join(cls_path, f)
            img = Image.open(img_path)
            img.save(os.path.join(cls_path, f.split('.')[0]+'.png'))
            img.close()
            list_.append(img_path)

for _ in list_:
    os.remove(_)

print("✅ Done! Converted .bmp to .png.")