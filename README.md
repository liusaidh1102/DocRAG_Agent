# DocRAG Agent - 智扫通机器人智能客服

一个基于 LangChain ReAct Agent 和 RAG（检索增强生成）技术的智能客服系统，专注于扫地机器人领域的问答服务。

## 📋 目录

- [项目简介](#项目简介)
- [核心功能](#核心功能)
- [技术栈](#技术栈)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [配置说明](#配置说明)
- [使用说明](#使用说明)
- [开发指南](#开发指南)

## 项目简介

DocRAG Agent 是一个智能客服机器人系统，结合了 ReAct Agent 推理框架和 RAG 技术，能够为用户提供专业的扫地机器人相关咨询服务。系统支持多轮对话、文档检索、外部数据查询等功能，并提供流式响应以提升用户体验。

## 核心功能

- **智能问答**：基于 RAG 技术，从专业文档中检索相关信息并生成准确回答
- **ReAct Agent**：采用推理-行动循环，智能选择工具完成任务
- **流式响应**：实时展示 AI 思考过程，提升交互体验
- **多工具集成**：支持天气查询、用户位置获取、外部数据访问等多种工具
- **会话管理**：自动维护对话历史，支持上下文理解
- **报告生成**：根据用户使用记录生成个性化报告

## 技术栈

- **前端框架**：Streamlit
- **AI 框架**：LangChain
- **向量数据库**：ChromaDB
- **大语言模型**：通过 model/factory.py 配置的聊天模型
- **配置文件**：YAML 格式配置
- **日志系统**：自定义日志处理器

## 项目结构

```
DocRAG_Agent/
├── agent/                      # Agent 核心模块
│   ├── tools/                  # 工具集
│   │   ├── agent_tools.py      # 自定义工具实现，定义了一些外部调用的工具
│   │   └── middleware.py       # 中间件（监控、日志等）
│   └── react_agent.py          # ReAct Agent 主类
├── rag/                        # RAG 检索增强生成模块
│   ├── vector_store.py         # 向量存储服务，将文档向量化并存储到chromaDB
│   └── rag_service.py          # RAG 总结服务，将rag生成的匹配的文档进行总结，交给大模型
├── model/                      # 模型工厂
│   └── factory.py              # 聊天模型初始化
├── config/                     # 配置文件
│   ├── agent.yml               # Agent 配置
│   ├── chroma.yml              # ChromaDB 配置
│   ├── prompts.yml             # 提示词配置
│   └── rag.yml                 # RAG 配置
├── prompts/                    # 提示词模板
│   ├── main_prompt.txt         # 主提示词
│   ├── rag_summarize.txt       # RAG 总结提示词
│   └── report_prompt.txt       # 报告生成提示词
├── data/                       # 数据文件
│   ├── external/               # 外部数据
│   │   └── records.csv         # 用户记录
│   ├── 扫地机器人100问.pdf     # 知识库文档
│   ├── 扫地机器人100问2.txt    # 知识库文档
│   ├── 扫拖一体机器人100问.txt # 知识库文档
│   ├── 故障排除.txt            # 故障排除指南
│   ├── 维护保养.txt            # 维护保养指南
│   └── 选购指南.txt            # 选购指南
├── chroma_db/                  # ChromaDB 向量数据库存储
├── logs/                       # 日志文件
├── utils/                      # 工具类
│   ├── config_handler.py       # 配置处理器
│   ├── file_handler.py         # 文件处理器
│   ├── logger_handler.py       # 日志处理器
│   ├── path_tool.py            # 路径工具
│   └── prompt_loader.py        # 提示词加载器
├── app.py                      # Streamlit 应用入口
└── README.md                   # 项目说明文档
```

### 目录说明

- **agent/**: 包含 ReAct Agent 的核心实现和工具集
  - `react_agent.py`: 定义 Agent 的行为、工具和中间件
  - `tools/agent_tools.py`: 实现各种可调用的工具函数
  - `tools/middleware.py`: 提供工具监控、日志记录等中间件功能

- **rag/**: RAG 检索增强生成相关功能
  - `vector_store.py`: 向量数据库的初始化和检索器管理
  - `rag_service.py`: 文档检索和总结服务

- **model/**: 模型管理层
  - `factory.py`: 统一管理和初始化聊天模型

- **config/**: YAML 格式的配置文件，便于修改系统参数

- **prompts/**: 各类提示词模板，控制 AI 的行为和输出风格

- **data/**: 知识库文档和外部数据源

- **utils/**: 通用工具类，提供配置读取、文件操作、日志记录等功能

## 快速开始

### 环境要求

- Python 3.8+
- pip 包管理器

### 安装依赖

```bash
pip install streamlit langchain chromadb
# 其他依赖根据实际需求安装
```

### 运行应用

```bash
streamlit run app.py
```

应用将在浏览器中自动打开，默认地址为 `http://localhost:8501`

## 配置说明

### 主要配置文件

1. **config/agent.yml**: Agent 相关配置
   - `external_data_path`: 外部数据文件路径

2. **config/chroma.yml**: ChromaDB 向量数据库配置

3. **config/prompts.yml**: 提示词配置

4. **config/rag.yml**: RAG 相关配置

### 提示词模板

所有提示词模板位于 `prompts/` 目录下，可根据需求自定义修改：
- `main_prompt.txt`: 系统主提示词，定义 Agent 的基本行为
- `rag_summarize.txt`: RAG 检索后的总结提示词
- `report_prompt.txt`: 生成用户报告的提示词

## 使用说明

### 基本对话

1. 启动应用后，在聊天输入框中输入问题
2. 系统会自动检索相关知识库文档
3. AI 助手会生成流式响应，实时显示回答内容
4. 对话历史会自动保存，支持上下文理解

### 示例问题

- "小户型适合哪些扫地机器人？"
- "扫地机器人如何维护保养？"
- "给我生成我的使用报告"
- "扫地机器人常见故障有哪些？"

## 开发指南

### 添加新工具

在 `agent/tools/agent_tools.py` 中定义新工具函数，然后在 `react_agent.py` 中注册：

```python
from agent.tools.agent_tools import your_new_tool

# 在 ReactAgent.__init__ 中添加
tools=[..., your_new_tool]
```

### 自定义提示词

1. 在 `prompts/` 目录下创建新的提示词文件
2. 在 `utils/prompt_loader.py` 中添加加载逻辑
3. 在配置文件中引用新提示词

### 扩展知识库

将新的文档放入 `data/` 目录，支持以下格式：
- PDF 文件
- TXT 文本文件
- CSV 数据文件

系统会自动处理并向量化这些文档。

### 日志查看

所有运行日志保存在 `logs/` 目录下，按日期命名：
- `agent_YYYYMMDD.log`

## 许可证

本项目仅供学习和研究使用。
