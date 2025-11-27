#!/usr/bin/env python3
"""
系統快速啟動腳本
"""

import os
import sys
import subprocess
from pathlib import Path

def check_system():
    """檢查系統狀態"""
    print("🔍 檢查系統狀態...")
    
    # 檢查必要目錄
    required_dirs = ['core', 'utils', 'configs']
    for dir_name in required_dirs:
        if not (Path(__file__).parent / dir_name).exists():
            print(f"❌ 缺失目錄: {dir_name}")
            return False
            
    # 檢查必要檔案
    required_files = ['main.py', 'configs/system_config.yaml']
    for file_name in required_files:
        if not (Path(__file__).parent / file_name).exists():
            print(f"❌ 缺失檔案: {file_name}")
            return False
            
    print("✅ 系統檢查通過")
    return True

def install_missing_dependencies():
    """安裝缺失的依賴"""
    print("📦 檢查依賴套件...")
    
    try:
        # 讀取 requirements.txt
        requirements_file = Path(__file__).parent / 'requirements.txt'
        if requirements_file.exists():
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', str(requirements_file)])
            print("✅ 依賴套件安裝完成")
        else:
            print("⚠️  未找到 requirements.txt")
            
    except subprocess.CalledProcessError:
        print("❌ 依賴套件安裝失敗")
        return False
        
    return True

def start_system():
    """啟動系統"""
    print("🚀 啟動車牌辨識系統...")
    
    try:
        main_file = Path(__file__).parent / 'main.py'
        subprocess.run([sys.executable, str(main_file)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 系統啟動失敗: {e}")
        return False
    except KeyboardInterrupt:
        print("\n🛑 系統已手動停止")
        
    return True

def main():
    """主函數"""
    print("=" * 50)
    print("   車牌辨識系統 - 快速啟動")
    print("=" * 50)
    print()
    
    # 檢查系統
    if not check_system():
        print("\n請先運行 setup_system.py 安裝系統")
        return
        
    # 安裝依賴
    if not install_missing_dependencies():
        return
        
    # 啟動系統
    start_system()

if __name__ == "__main__":
    main()
