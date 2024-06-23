from typing import List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from database.base import Base


class Player(Base):
    __tablename__ = "player"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(length=100))
    kingdom: Mapped[List["Kingdom"]] = relationship(back_populates="player")
    kingdom_id: Mapped[int] = mapped_column(ForeignKey("kingdom.id"))


class Kingdom(Base):
    __tablename__ = "kingdom"
    id: Mapped[int] = mapped_column(primary_key=True)
    top_power: Mapped[int] = mapped_column(Integer)
    top_kps: Mapped[int] = mapped_column(Integer)
    t5_kill: Mapped[int] = mapped_column(Integer)
    t4_kill: Mapped[int] = mapped_column(Integer)
    t3_kill: Mapped[int] = mapped_column(Integer)
    t2_kill: Mapped[int] = mapped_column(Integer)
    t1_kill: Mapped[int] = mapped_column(Integer)
    death: Mapped[int] = mapped_column(Integer)
    player: Mapped["Player"] = relationship(back_populates="kingdom")


class KingdomHistory(Base):
    __tablename__ = "kingdom_history"
    id: Mapped[int] = mapped_column(primary_key=True)
    top_power: Mapped[int] = mapped_column(Integer)
    top_kps: Mapped[int] = mapped_column(Integer)
    t5_kill: Mapped[int] = mapped_column(Integer)
    t4_kill: Mapped[int] = mapped_column(Integer)
    t3_kill: Mapped[int] = mapped_column(Integer)
    t2_kill: Mapped[int] = mapped_column(Integer)
    t1_kill: Mapped[int] = mapped_column(Integer)
    death: Mapped[int] = mapped_column(Integer)
    kingdom_id: Mapped[int] = mapped_column(ForeignKey("kingdom.id"))
    player: Mapped["Player"] = relationship(back_populates="kingdom")

class PlayerHistory(Base):
    __tablename__ = "player_history"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(length=100))
    deaths: Mapped[int] = mapped_column(Integer)
    t5_kill: Mapped[int] = mapped_column(Integer)
    t4_kill: Mapped[int] = mapped_column(Integer)
    t3_kill: Mapped[int] = mapped_column(Integer)
    t2_kill: Mapped[int] = mapped_column(Integer)
    t1_kill: Mapped[int] = mapped_column(Integer)
    rss_gather: Mapped[int] = mapped_column(Integer)
    rss_donation: Mapped[int] = mapped_column(Integer)
    data_scan: Mapped[str] = mapped_column(String(length=100))
    kill_points: Mapped[int] = mapped_column(Integer)
    power: Mapped[int] = mapped_column(Integer)
    player_id: Mapped[int] = mapped_column(ForeignKey("player.id"))


