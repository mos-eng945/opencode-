# FastAPI 学习项目

这是一个FastAPI学习项目，包含多个示例文件。

## 项目结构

```
fastapi-1/
├── .vscode/              # VSCode配置
│   ├── settings.json     # 编辑器设置
│   ├── launch.json       # 调试配置
│   └── extensions.json   # 推荐扩展
├── data/                 # 数据文件
├── main.py              # 主文件
├── main02.py - main11.py # 其他示例文件
├── requirements.txt     # 依赖包
├── pyproject.toml      # 项目配置
└── README.md           # 项目说明
```

## 快速开始

### 1. 安装Python
确保已安装Python 3.8+

### 2. 创建虚拟环境
```bash
python -m venv venv
```

### 3. 激活虚拟环境
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### 4. 安装依赖
```bash
pip install -r requirements.txt
```

### 5. 运行项目
```bash
python main.py
```

访问 http://localhost:8000

## VSCode配置

### 推荐扩展
1. **Python** (Microsoft) - Python语言支持
2. **Pylance** - Python语言服务器
3. **Black Formatter** - 代码格式化
4. **GitLens** - Git增强功能

### 调试配置
按F5启动调试，选择"Python: FastAPI"配置

### 代码格式化
保存时自动格式化（Black）

## API示例

### 路径参数
```python
@app.get("/args/{id}")
def path_arg_1(id):
    return {"message": f"id {id}"}
```

### 类型化路径参数
```python
@app.get("/args4/{id}/{name}")
def path_arg_2(id: int, name: str):
    return {"message": f"id {id}, name {name}"}
```

## 开发

### 代码风格
- 使用Black格式化代码
- 使用isort排序导入
- 行长度限制：88字符

### 测试
```bash
pytest
```

## 许可证
MIT