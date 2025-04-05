

<p align="center">
SalesCub 是一个开源的智能数字销售员。它集成了智能代理（Agent）能力、工作流管道、销售自动化流程、模型管理、可观测性功能等，帮助企业快速从销售原型验证到大规模落地，实现高效、智能的销售转化。
</p>

# 👋 SalerScub


用 Salerscub 开启你的智能体之旅吧！


## 项目演示

[![OpenManus演示视频](https://github.com/salerscub/salerscub/blob/main/scub.png)](https://www.bilibili.com/video/BV1UyZSYuEmK/?vd_source=555d4d06d76dfcceeb83a9e9c3717834)

点击上面的截图观看 salerscub 演示视频。

主站：http://salerscub.agiexe.com/

## 安装指南

我们提供两种安装方式。推荐使用方式二（uv），因为它能提供更快的安装速度和更好的依赖管理。

### 方式一：使用 conda

1. 创建新的 conda 环境：

```bash
conda create -n salerscub python=3.12
conda activate salerscub
```

2. 克隆仓库：

```bash
git clone https://github.com/salerscub/salerscub.git
cd OpenManus
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

### 方式二：使用 uv

1. 安装 uv：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. 克隆仓库：

```bash
git clone https://github.com/salerscub/salerscub.git
cd OpenManus
```

3. 创建并激活虚拟环境：

```bash
uv venv
source .venv/bin/activate  # Unix/macOS 系统

# Windows 系统使用：
# .venv\Scripts\activate
```

4. 安装依赖：

```bash
uv pip install -r requirements.txt
```

## 配置说明

Salerscub 需要配置使用的 LLM API，请按以下步骤设置：

1. 在 `config` 目录创建 `config.toml` 文件（可从示例复制）：

```bash
cp config/config.example.toml config/config.toml
```

2. 编辑 `config/config.toml` 添加 API 密钥和自定义设置：

```toml
# 全局 LLM 配置
[llm]
model = "deepseek-r1-250120"
base_url = "https://ark.cn-beijing.volces.com/api/v3"
api_key = "d5d9437dd7-xxxxxxxxxxxxxxxx"
max_tokens = 8192
temperature = 0.4

# 可选特定 LLM 模型配置
[llm.vision]
model = "deepseek-r1-250120"
base_url = "https://ark.cn-beijing.volces.com/api/v3"
api_key = "d5d9437dd7-xxxxxxxxxxxxx"

# 服务配置
[server]
host = "0.0.0.0"
port = 5172
```

## 快速启动

一行命令运行 Salerscub：

```bash
python appy.py
```

如需体验开发中版本，可运行：

```bash
python main.py
```
或
```bash
python run_flow.py
```

## 致谢

特别感谢：
饼干哥、可可、CC、Steffens

