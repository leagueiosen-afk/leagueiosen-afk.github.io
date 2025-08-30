# Google AdSense 和 Search Console 配置指南

## 第一步：GitHub Pages 部署

1. 确保所有文件都已提交到GitHub仓库
2. 在GitHub仓库设置中启用GitHub Pages
3. 选择main分支作为源分支
4. 等待部署完成（通常需要几分钟）

## 第二步：Google Search Console 验证

1. 访问 [Google Search Console](https://search.google.com/search-console)
2. 添加属性：`https://leagueiosen-afk.github.io`
3. 选择"HTML标记"验证方法
4. 复制验证代码：`google67eab7b3e906ad8d`
5. 验证代码已添加到 `index.html` 的 `<head>` 部分
6. 点击"验证"按钮

## 第三步：Google AdSense 配置

### 3.1 添加网站到AdSense
1. 访问 [Google AdSense](https://adsense.google.com)
2. 进入"Sites"部分
3. 点击"+ New site"
4. 添加网站URL：`https://leagueiosen-afk.github.io`
5. 等待审核（通常需要几天到几周）

### 3.2 配置ads.txt文件
- ads.txt文件已创建并包含正确内容
- 确保文件可通过 `https://leagueiosen-afk.github.io/ads.txt` 访问
- 内容：`google.com, pub-5063571290810407, DIRECT, f08c47fec0942fa0`

### 3.3 创建广告单元
1. 在AdSense中创建新的广告单元
2. 获取广告位ID
3. 将广告位ID替换到 `index.html` 中的 `data-ad-slot` 属性

## 第四步：SEO优化

### 4.1 结构化数据
- 已添加Schema.org标记
- 网站类型：NewsMediaOrganization

### 4.2 内容优化
- 确保内容在页面加载时立即可见
- 避免完全依赖JavaScript加载内容

### 4.3 技术SEO
- robots.txt 已正确配置
- sitemap.xml 已创建
- 所有必要的meta标签已添加

## 第五步：验证和测试

### 5.1 测试ads.txt访问
访问：`https://leagueiosen-afk.github.io/ads.txt`
应该显示：`google.com, pub-5063571290810407, DIRECT, f08c47fec0942fa0`

### 5.2 测试robots.txt访问
访问：`https://leagueiosen-afk.github.io/robots.txt`
确保文件正确显示

### 5.3 测试sitemap.xml访问
访问：`https://leagueiosen-afk.github.io/sitemap.xml`
确保XML格式正确

## 第六步：监控和优化

### 6.1 Google Search Console
- 监控索引状态
- 检查移动端可用性
- 查看核心网页指标

### 6.2 Google AdSense
- 监控网站状态
- 检查ads.txt状态
- 查看收入报告

## 常见问题解决

### 问题1：ads.txt显示"Not found"
**解决方案：**
1. 确保ads.txt文件在根目录
2. 检查文件内容是否正确
3. 等待GitHub Pages部署完成
4. 清除浏览器缓存

### 问题2：Google Search Console验证失败
**解决方案：**
1. 检查验证代码是否正确添加
2. 确保网站可以正常访问
3. 等待DNS传播完成

### 问题3：AdSense审核被拒绝
**解决方案：**
1. 确保网站有原创内容
2. 检查网站是否符合AdSense政策
3. 确保网站有足够的流量
4. 等待重新审核

## 重要提醒

1. **耐心等待**：Google的审核和索引需要时间
2. **内容质量**：确保网站有高质量、原创的内容
3. **合规性**：遵守Google AdSense和Search Console的政策
4. **定期检查**：定期监控网站状态和性能指标

## 联系信息

如有问题，请参考：
- [Google Search Console 帮助](https://support.google.com/webmasters/)
- [Google AdSense 帮助](https://support.google.com/adsense/)
- [GitHub Pages 文档](https://pages.github.com/)
