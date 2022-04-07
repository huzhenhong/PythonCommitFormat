## 安装

- 安装 pre-commit 环境
  ```python
  pip install pre-commit
  pre-commit --version
  ```
  
  
  
- 当前项目安装/卸载 pre-commit 

  ```python
  # 项目根目录下执行以下命令
  pre-commit install
  pre-commit uninstall
  ```
  
  

## 项目配置 pre-commit

根目录下添加 .pre-commit-config.yaml文件, 内容如下

#### python项目

```python
fail_fast: false

repos:
-   repo: https://github.com/psf/black
    rev: 22.1.0
    hooks:
    -   id: black
        additional_dependencies: ['click==8.0.4']

-   repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
    -   id: flake8
        # additional_dependencies: [flake8-docstrings]
```

尝试手动检测全部文件

```python
pre-commit run --all-files
```

遇到的问题

- ValueError: check_hostname requires server_hostname

  pip要求你检查host name，说明主机地址有问题，关闭系统代理即可

- pre-commit 执行 black 时报错：ImportError: cannot import name '_unicodefun' from 'click'

  click库的版本太高了，可以手动指定click的版本

  ```yaml
  additional_dependencies: ['click==8.0.4']
  ```



##### 格式化演示

格式化前

```python
import imp
import cv2
import os

img=cv2.imread("circle.png")

img= cv2.resize(img,               
 (256, 256))

replicate = cv2.copyMakeBorder(img, 
20, -20, 20, 20, 
cv2.BORDER_REPLICATE)       
```

尝试提交

```shell
git add .
git commit -m 'say something'
```

输出如下，错误一目了然

```tex
PS D:\Job\FormatAndCommit> git add .
PS D:\Job\FormatAndCommit> git commit -m 'say something'
black....................................................................Failed
- hook id: black
- files were modified by this hook

reformatted main.py

All done! \u2728 \U0001f370 \u2728
1 file reformatted.

flake8...................................................................Failed
- hook id: flake8
- exit code: 1

main.py:1:1: F401 'imp' imported but unused
main.py:3:1: F401 'os' imported but unused
```

同时 black 已经原地对源代码进行了修改，修改后的源代码如下

```python
import imp
import cv2
import os

img = cv2.imread("circle.png")

img = cv2.resize(img, (256, 256))

replicate = cv2.copyMakeBorder(img, 20, -20, 20, 20, cv2.BORDER_REPLICATE)
```

此时我们移除

```python
import imp
import os
```

然后再次尝试提交，提交成功

```tex
PS D:\Job\FormatAndCommit> git add .
PS D:\Job\FormatAndCommit> git commit -m 'say something'
black....................................................................Passed
flake8...................................................................Passed
[master bb6e62b] say something
 3 files changed, 22 insertions(+), 74 deletions(-)
 rewrite .pre-commit-config.yaml (84%)
 delete mode 100644 circle.png
 rewrite main.py (85%)
```
