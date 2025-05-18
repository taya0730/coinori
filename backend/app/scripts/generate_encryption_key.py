"""
암호화 키 생성 스크립트
"""

from app.core.security import CryptoUtils

def main():
    # 새로운 암호화 키 생성
    encryption_key = CryptoUtils.generate_key()
    print("\n=== 암호화 키 생성 완료 ===")
    print(f"생성된 키: {encryption_key}")
    print("\n이 키를 .env 파일의 ENCRYPTION_KEY 값으로 설정하세요.")
    print("예: ENCRYPTION_KEY=your-generated-key-here")

if __name__ == "__main__":
    main() 