#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试AI新闻生成脚本
"""

import json
from news_generator import NewsGenerator

def test_local_news_generation():
    """测试本地新闻生成功能"""
    print("🧪 测试本地新闻生成功能...")
    
    generator = NewsGenerator()
    local_news = generator.generate_local_news(3)
    
    print(f"生成了 {len(local_news)} 条本地新闻:")
    for i, news in enumerate(local_news, 1):
        print(f"{i}. {news['title']}")
        print(f"   摘要: {news['summary']}")
        print(f"   分类: {news['category']}")
        print()

def test_timestamp():
    """测试时间戳功能"""
    print("🧪 测试时间戳功能...")
    
    generator = NewsGenerator()
    timestamp = generator.get_current_timestamp()
    print(f"当前时间戳: {timestamp}")

def test_news_data_structure():
    """测试新闻数据结构"""
    print("🧪 测试新闻数据结构...")
    
    generator = NewsGenerator()
    news_data = generator.generate_news_data()
    
    # 检查必需字段
    required_fields = ['update_time', 'total_news', 'source', 'news']
    for field in required_fields:
        if field in news_data:
            print(f"✅ {field}: {news_data[field]}")
        else:
            print(f"❌ 缺少字段: {field}")
    
    # 检查新闻项目结构
    if news_data['news']:
        first_news = news_data['news'][0]
        news_fields = ['id', 'title', 'summary', 'url', 'score', 'time', 'by', 'type', 'category']
        for field in news_fields:
            if field in first_news:
                print(f"✅ 新闻字段 {field}: {first_news[field]}")
            else:
                print(f"❌ 新闻缺少字段: {field}")

def main():
    """主测试函数"""
    print("🚀 开始测试AI新闻生成脚本...\n")
    
    try:
        test_timestamp()
        print()
        
        test_local_news_generation()
        print()
        
        test_news_data_structure()
        print()
        
        print("✅ 所有测试完成！")
        
    except Exception as e:
        print(f"❌ 测试失败: {e}")

if __name__ == "__main__":
    main()
