# Base64隐写加解密工具
> 说明：目前版本暂未实现加密

## 用法说明
```text
usage: b64steg.py [-h] [-f FILE] [-s SAVE]

Base64 steganography solver v1.0

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Chose input file
  -s SAVE, --save SAVE  Save the result(optional)
```

## 使用示例
> 题目地址: [攻防世界(base64stego36)](https://adworld.xctf.org.cn/task/answer?type=misc&number=1&grade=0&id=5107&page=1)

使用方式：
```bash
→  ~ b64steg.py -f stego.txt -s output.txt
Base_sixty_four_point_five
```