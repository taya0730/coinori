from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Text, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relations
    api_keys = relationship("APIKey", back_populates="user")
    trades = relationship("Trade", back_populates="user")
    settings = relationship("TradingSetting", back_populates="user")


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exchange = Column(String)  # "binance" or "upbit"
    api_key = Column(String)
    api_secret = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relations
    user = relationship("User", back_populates="api_keys")


class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    exchange = Column(String)  # "binance" or "upbit"
    symbol = Column(String)  # e.g., "BTCUSDT"
    trade_type = Column(String)  # "spot" or "futures"
    order_type = Column(String)  # "market", "limit", etc.
    side = Column(String)  # "buy" or "sell"
    quantity = Column(Float)
    price = Column(Float)
    status = Column(String)  # "open", "filled", "cancelled", etc.
    order_id = Column(String)  # Exchange order ID
    profit_loss = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    extra_data = Column(JSON, nullable=True)  # For any additional data
    
    # Relations
    user = relationship("User", back_populates="trades")


class TradingSetting(Base):
    __tablename__ = "trading_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    strategy_name = Column(String)
    exchange = Column(String)  # "binance" or "upbit"
    trade_type = Column(String)  # "spot" or "futures"
    symbol = Column(String)  # e.g., "BTCUSDT"
    is_active = Column(Boolean, default=False)
    
    # Strategy parameters (stored as JSON for flexibility)
    parameters = Column(JSON)
    
    # Risk management settings
    max_position_size = Column(Float)
    stop_loss_percentage = Column(Float)
    take_profit_percentage = Column(Float)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    user = relationship("User", back_populates="settings")


class NotificationSetting(Base):
    __tablename__ = "notification_settings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    slack_webhook_url = Column(String, nullable=True)
    discord_webhook_url = Column(String, nullable=True)
    notify_on_trade = Column(Boolean, default=True)
    notify_on_error = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())




