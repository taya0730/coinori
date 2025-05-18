"""
업비트 API 예외 클래스
"""

class UpbitAPIError(Exception):
    """업비트 API 관련 기본 예외 클래스"""
    pass

class UpbitAPIKeyError(UpbitAPIError):
    """API 키 관련 예외"""
    pass

class UpbitAPIRequestError(UpbitAPIError):
    """API 요청 관련 예외"""
    pass

class UpbitAPIResponseError(UpbitAPIError):
    """API 응답 관련 예외"""
    pass 