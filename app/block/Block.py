from app import storage
from dateutil import parser
from sqlalchemy import Column, String, Integer, DateTime
import json

class Block(storage.Base):
    __tablename__ = 'blocks'

    _id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    prev_block_id = Column(String)
    prev_block_hash = Column(String)
    tx_list = Column(String)
    merkle_root = Column(String)
    time_stamp = Column(DateTime)
    block_id = Column(String)
    block_hash = Column(String)
    nonce = Column(String)
    block_info = Column(String)
    block_miner = Column(Integer)

    def __init__(self):
        self.type = 'B'

    def __str__(self):
        return self.to_json()

    def to_json(self):
        return json.dumps({
            'type': self.type,
            'time_stamp': self.time_stamp.strftime('%Y%m%d%H%M%S'),
            'prev_block_id': self.prev_block_id,
            'prev_block_hash': self.prev_block_hash,
            'merkle_root': self.merkle_root,
            'block_hash': self.block_hash,
            'nonce': self.nonce,
            'block_id': self.block_id
        })

    def from_json(self, dictionary):
        """Constructor"""
        for key in dictionary:
            setattr(self, key, dictionary[key])

        self.time_stamp = parser.parse(self.time_stamp)
        return self
