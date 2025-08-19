# AI新闻生成脚本 - 强化版

## 📋 功能特性

### ✅ 核心功能
1. **智能新闻获取**：从Hacker News API获取最新的AI相关新闻
2. **健壮错误处理**：网络请求失败时自动切换到本地备用内容
3. **本地备用系统**：使用预置的AI关键词和新闻模板生成内容
4. **时间戳记录**：自动添加更新时间戳
5. **成功状态反馈**：清晰的控制台输出和状态信息

### 🔧 技术特性
- **多源数据获取**：Hacker News API + 本地备用内容
- **智能分类系统**：自动对新闻进行分类（大语言模型、计算机视觉等）
- **模板化生成**：使用多种新闻模板确保内容多样性
- **错误恢复机制**：确保网站永远有内容更新

## 🚀 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行脚本
```bash
python news_generator.py
```

### 3. 查看输出
脚本会生成 `ai_news.json` 文件，包含最新的AI新闻数据。

## 📊 输出格式

生成的JSON文件格式如下：
```json
{
  "update_time": "2024-01-15 14:30",
  "total_news": 5,
  "news": [
    {
      "title": "OpenAI发布GPT-5预览版，性能大幅提升",
      "summary": "最新研究显示，GPT-5技术在多个基准测试中表现优异...",
      "url": "https://example.com/news/123",
      "score": 150,
      "time": 1705312200,
      "category": "大语言模型"
    }
  ]
}
```

## 🔄 工作流程

1. **尝试获取Hacker News数据**
   - 获取最新50个故事
   - 筛选AI相关新闻
   - 生成摘要和分类

2. **备用内容生成**
   - 如果网络请求失败
   - 使用本地AI关键词库
   - 应用新闻模板生成内容

3. **数据保存**
   - 添加时间戳
   - 保存为JSON格式
   - 显示成功信息

## 🛠️ 自定义配置

### 修改AI关键词
在 `ai_keywords` 列表中添加或修改关键词：
```python
self.ai_keywords = [
    'GPT', 'LLM', 'Computer Vision', 'Machine Learning',
    # 添加更多关键词...
]
```

### 添加新闻模板
在 `news_templates` 中添加新的模板：
```python
{
    "title_template": "新的{keyword}模板",
    "summary_template": "新的摘要模板，包含{keyword}信息"
}
```

### 修改公司列表
在 `companies` 列表中添加更多公司：
```python
self.companies = [
    "OpenAI", "Google", "Microsoft",
    # 添加更多公司...
]
```

## 📈 使用场景

### 1. 网站内容更新
- 定期运行脚本更新网站新闻
- 确保网站始终有新鲜内容

### 2. 内容管理系统
- 集成到CMS系统中
- 自动生成新闻内容

### 3. 数据分析
- 收集AI行业新闻数据
- 进行趋势分析

## 🔧 故障排除

### 常见问题

1. **网络连接失败**
   - 脚本会自动切换到本地备用内容
   - 检查网络连接和防火墙设置

2. **依赖包安装失败**
   ```bash
   pip install --upgrade pip
   pip install requests
   ```

3. **权限问题**
   ```bash
   chmod +x news_generator.py
   ```

### 日志信息
脚本会显示详细的执行信息：
- 🔍 正在获取新闻
- ✅ 成功获取数据
- ⚠️ 警告信息
- ❌ 错误信息

## 📝 更新日志

### v1.0.0 (2024-01-15)
- ✅ 初始版本发布
- ✅ 支持Hacker News API
- ✅ 本地备用内容系统
- ✅ 时间戳功能
- ✅ 错误处理机制

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个脚本！

## 📄 许可证

MIT License
