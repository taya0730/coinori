"""
업비트 API 연동 클래스
"""

import pyupbit
from typing import Optional, Dict, Any
from .exceptions import UpbitAPIError

class UpbitAPI:
    def __init__(self, access_key: str, secret_key: str):
        """
        업비트 API 클라이언트 초기화
        
        Args:
            access_key (str): 업비트 API 액세스 키
            secret_key (str): 업비트 API 시크릿 키
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.client = pyupbit.Upbit(access_key, secret_key)
    
    def get_balance(self, ticker: str = "KRW") -> float:
        """
        잔고 조회
        
        Args:
            ticker (str): 화폐 종류 (기본값: KRW)
            
        Returns:
            float: 잔고
        """
        try:
            return self.client.get_balance(ticker)
        except Exception as e:
            raise UpbitAPIError(f"잔고 조회 실패: {str(e)}")
    
    def get_current_price(self, ticker: str) -> float:
        """
        현재가 조회
        
        Args:
            ticker (str): 티커 (예: KRW-BTC)
            
        Returns:
            float: 현재가
        """
        try:
            return pyupbit.get_current_price(ticker)
        except Exception as e:
            raise UpbitAPIError(f"현재가 조회 실패: {str(e)}")
    
    def place_market_order(self, ticker: str, side: str, volume: Optional[float] = None, price: Optional[float] = None) -> Dict[str, Any]:
        """
        시장가 주문
        
        Args:
            ticker (str): 티커 (예: KRW-BTC)
            side (str): 주문 종류 (bid: 매수, ask: 매도)
            volume (float, optional): 주문량
            price (float, optional): 주문 가격
            
        Returns:
            Dict[str, Any]: 주문 결과
        """
        try:
            if side == "bid":
                return self.client.buy_market_order(ticker, price)
            else:
                return self.client.sell_market_order(ticker, volume)
        except Exception as e:
            raise UpbitAPIError(f"주문 실패: {str(e)}") 