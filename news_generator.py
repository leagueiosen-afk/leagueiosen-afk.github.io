#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI新闻生成脚本 - 强化版
功能：从Hacker News获取AI相关新闻，失败时使用本地备用内容
作者：AI前沿团队
"""

import requests
import json
import random
from datetime import datetime
import time
from typing import List, Dict, Optional

class NewsGenerator:
    def __init__(self):
        # Hacker News API配置
        self.hn_api_url = "https://hacker-news.firebaseio.com/v0"
        self.max_retries = 3
        self.timeout = 10
        
        # 本地备用AI关键词和新闻模板
        self.ai_keywords = [
            'GPT', 'LLM', 'Computer Vision', 'Machine Learning', 'Deep Learning',
            'Neural Networks', 'Natural Language Processing', 'AI Ethics',
            'Quantum Computing', 'Robotics', 'Autonomous Vehicles', 'AI Safety',
            'Generative AI', 'Transformers', 'Reinforcement Learning',
            'Computer Vision', 'Speech Recognition', 'AI Governance',
            'Edge AI', 'Federated Learning', 'AI Hardware', 'AI Research'
        ]
        
        self.news_templates = [
            {
                "title_template": "{keyword}技术取得重大突破",
                "summary_template": "最新研究显示，{keyword}技术在多个领域展现出前所未有的潜力。专家表示，这一突破将为相关行业带来革命性变化。"
            },
            {
                "title_template": "{keyword}在商业应用中获得成功",
                "summary_template": "多家企业开始采用{keyword}技术，在提升效率和降低成本方面取得显著成效。市场分析师预测该技术将迎来快速增长。"
            },
            {
                "title_template": "{keyword}研究获得重要进展",
                "summary_template": "学术界在{keyword}领域的研究取得重要进展，相关论文已在顶级期刊发表。这一成果为后续研究奠定了坚实基础。"
            },
            {
                "title_template": "{keyword}在医疗领域的应用前景广阔",
                "summary_template": "医疗行业开始探索{keyword}技术的应用，在疾病诊断和治疗方案制定方面显示出巨大潜力。"
            },
            {
                "title_template": "{keyword}技术标准化进程加速",
                "summary_template": "国际标准化组织开始制定{keyword}技术的相关标准，这将有助于技术的推广和应用。"
            }
        ]
        
        # AI相关关键词用于过滤新闻
        self.ai_filter_keywords = [
            'ai', 'artificial intelligence', 'machine learning', 'deep learning',
            'neural network', 'gpt', 'llm', 'transformer', 'computer vision',
            'nlp', 'natural language', 'robotics', 'automation', 'algorithm',
            'data science', 'big data', 'quantum', 'blockchain', 'iot',
            'autonomous', 'chatbot', 'recommendation', 'prediction'
        ]

    def get_current_timestamp(self) -> str:
        """获取当前时间戳"""
        return datetime.now().strftime("%Y-%m-%d %H:%M")

    def make_request_with_retry(self, url: str) -> Optional[requests.Response]:
        """带重试的网络请求"""
        for attempt in range(self.max_retries):
            try:
                print(f"正在尝试请求 {url} (第{attempt + 1}次)")
                response = requests.get(url, timeout=self.timeout)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                print(f"请求失败 (第{attempt + 1}次): {e}")
                if attempt < self.max_retries - 1:
                    wait_time = 2 ** attempt  # 指数退避
                    print(f"等待 {wait_time} 秒后重试...")
                    time.sleep(wait_time)
                else:
                    print(f"所有重试都失败了: {url}")
                    return None
        return None

    def fetch_top_stories(self) -> Optional[List[int]]:
        """获取Hacker News热门故事ID列表"""
        url = f"{self.hn_api_url}/topstories.json"
        response = self.make_request_with_retry(url)
        if response:
            try:
                return response.json()[:20]  # 只取前20个
            except json.JSONDecodeError as e:
                print(f"JSON解析失败: {e}")
                return None
        return None

    def fetch_story_details(self, story_id: int) -> Optional[Dict]:
        """获取单个故事的详细信息"""
        url = f"{self.hn_api_url}/item/{story_id}.json"
        response = self.make_request_with_retry(url)
        if response:
            try:
                return response.json()
            except json.JSONDecodeError as e:
                print(f"故事详情JSON解析失败: {e}")
                return None
        return None

    def is_ai_related(self, title: str, text: str = "") -> bool:
        """判断新闻是否与AI相关"""
        content = (title + " " + text).lower()
        return any(keyword in content for keyword in self.ai_filter_keywords)

    def generate_local_news(self, count: int = 5) -> List[Dict]:
        """生成本地备用AI新闻"""
        print("使用本地备用内容生成AI新闻...")
        
        news_list = []
        used_keywords = set()
        
        for i in range(count):
            # 选择未使用的关键词
            available_keywords = [k for k in self.ai_keywords if k not in used_keywords]
            if not available_keywords:
                used_keywords.clear()  # 重置已使用关键词
                available_keywords = self.ai_keywords
            
            keyword = random.choice(available_keywords)
            used_keywords.add(keyword)
            
            # 选择新闻模板
            template = random.choice(self.news_templates)
            
            # 生成新闻
            news = {
                "id": f"local_{i+1}",
                "title": template["title_template"].format(keyword=keyword),
                "summary": template["summary_template"].format(keyword=keyword),
                "url": f"#local-news-{i+1}",
                "score": random.randint(50, 200),
                "time": int(time.time()),
                "by": "AI前沿编辑",
                "type": "local_news",
                "category": self.get_category_for_keyword(keyword)
            }
            news_list.append(news)
        
        return news_list

    def get_category_for_keyword(self, keyword: str) -> str:
        """根据关键词确定新闻分类"""
        category_mapping = {
            'GPT': '大语言模型',
            'LLM': '大语言模型',
            'Computer Vision': '计算机视觉',
            'Machine Learning': '机器学习',
            'Deep Learning': '深度学习',
            'Neural Networks': '神经网络',
            'Natural Language Processing': '自然语言处理',
            'AI Ethics': 'AI伦理',
            'Quantum Computing': '量子计算',
            'Robotics': '机器人技术',
            'Autonomous Vehicles': '自动驾驶',
            'AI Safety': 'AI安全',
            'Generative AI': '生成式AI',
            'Transformers': 'Transformer模型',
            'Reinforcement Learning': '强化学习',
            'Speech Recognition': '语音识别',
            'AI Governance': 'AI治理',
            'Edge AI': '边缘AI',
            'Federated Learning': '联邦学习',
            'AI Hardware': 'AI硬件',
            'AI Research': 'AI研究'
        }
        return category_mapping.get(keyword, 'AI技术')

    def fetch_hn_news(self) -> List[Dict]:
        """从Hacker News获取AI相关新闻"""
        print("正在从Hacker News获取AI相关新闻...")
        
        # 获取热门故事ID
        story_ids = self.fetch_top_stories()
        if not story_ids:
            print("无法获取Hacker News热门故事列表")
            return []

        # 获取故事详情
        ai_news = []
        for story_id in story_ids:
            story = self.fetch_story_details(story_id)
            if story and story.get('type') == 'story':
                title = story.get('title', '')
                text = story.get('text', '')
                
                if self.is_ai_related(title, text):
                    news_item = {
                        "id": story.get('id'),
                        "title": title,
                        "summary": self.generate_summary(title, text),
                        "url": story.get('url', f"https://news.ycombinator.com/item?id={story_id}"),
                        "score": story.get('score', 0),
                        "time": story.get('time', 0),
                        "by": story.get('by', 'unknown'),
                        "type": "hn_news",
                        "category": self.categorize_news(title)
                    }
                    ai_news.append(news_item)
                    
                    if len(ai_news) >= 5:  # 只取前5条
                        break

        return ai_news

    def generate_summary(self, title: str, text: str = "") -> str:
        """生成新闻摘要"""
        if text:
            # 如果有正文，取前100个字符作为摘要
            summary = text[:100].strip()
            if len(text) > 100:
                summary += "..."
            return summary
        else:
            # 如果没有正文，基于标题生成摘要
            return f"关于{title}的最新动态和详细分析。"

    def categorize_news(self, title: str) -> str:
        """根据标题对新闻进行分类"""
        title_lower = title.lower()
        
        if any(word in title_lower for word in ['gpt', 'llm', 'language', 'text']):
            return '大语言模型'
        elif any(word in title_lower for word in ['vision', 'image', 'photo', 'video']):
            return '计算机视觉'
        elif any(word in title_lower for word in ['robot', 'automation']):
            return '机器人技术'
        elif any(word in title_lower for word in ['quantum']):
            return '量子计算'
        elif any(word in title_lower for word in ['ethics', 'safety', 'governance']):
            return 'AI伦理'
        elif any(word in title_lower for word in ['hardware', 'chip', 'gpu']):
            return 'AI硬件'
        else:
            return 'AI技术'

    def generate_news_data(self) -> Dict:
        """生成完整的新闻数据"""
        print("开始生成AI新闻数据...")
        
        # 尝试从Hacker News获取新闻
        hn_news = self.fetch_hn_news()
        
        if hn_news:
            print(f"成功从Hacker News获取到 {len(hn_news)} 条AI相关新闻")
            news_list = hn_news
        else:
            print("Hacker News获取失败，使用本地备用内容")
            news_list = self.generate_local_news(5)
        
        # 添加时间戳
        news_data = {
            "update_time": self.get_current_timestamp(),
            "total_news": len(news_list),
            "source": "hn_news" if hn_news else "local_backup",
            "news": news_list
        }
        
        return news_data

    def save_news_data(self, data: Dict, filename: str = "ai_news_data.json") -> bool:
        """保存新闻数据到JSON文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"新闻数据已保存到 {filename}")
            return True
        except Exception as e:
            print(f"保存文件失败: {e}")
            return False

    def print_success_info(self, data: Dict):
        """打印成功信息"""
        print("\n" + "="*50)
        print("🎉 AI新闻生成成功！")
        print("="*50)
        print(f"📅 更新时间: {data['update_time']}")
        print(f"📊 新闻总数: {data['total_news']} 条")
        print(f"📡 数据来源: {data['source']}")
        print("\n📰 最新新闻预览:")
        
        for i, news in enumerate(data['news'][:3], 1):
            print(f"{i}. {news['title']}")
            print(f"   分类: {news['category']}")
            print(f"   热度: {news['score']}")
            print()
        
        print("✅ 所有操作已完成，网站内容已更新！")
        print("="*50)

def main():
    """主函数"""
    print("🚀 启动AI新闻生成脚本...")
    
    # 创建新闻生成器实例
    generator = NewsGenerator()
    
    try:
        # 生成新闻数据
        news_data = generator.generate_news_data()
        
        # 保存数据
        if generator.save_news_data(news_data):
            # 打印成功信息
            generator.print_success_info(news_data)
        else:
            print("❌ 保存数据失败")
            
    except Exception as e:
        print(f"❌ 脚本执行失败: {e}")
        print("🔄 尝试使用本地备用内容...")
        
        try:
            # 使用本地备用内容
            backup_data = {
                "update_time": generator.get_current_timestamp(),
                "total_news": 5,
                "source": "local_backup_emergency",
                "news": generator.generate_local_news(5)
            }
            
            if generator.save_news_data(backup_data):
                generator.print_success_info(backup_data)
            else:
                print("❌ 备用内容保存也失败了")
                
        except Exception as backup_error:
            print(f"❌ 备用内容生成失败: {backup_error}")

if __name__ == "__main__":
    main()
