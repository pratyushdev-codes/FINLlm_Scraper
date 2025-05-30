
from pydantic import BaseModel


class Data(BaseModel):
    """
    Represents the data structure of a Stock Data.
    """

    MarketCap: str
    StockPE: str
    ROCE: str
    BookValue: str
    ROE: float
    HighLow: int
    FaceValue: str
