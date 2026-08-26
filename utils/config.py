import os

class Config:
    BASE_URL: str = os.getenv("BASEURL", "https://www.saucedemo.com")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    BROWSER: str = os.getenv("BROWSER", "chromium")
    SLOW_MO: int = int(os.getenv("SLOW_MO","0"))
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT","10000"))
    VIEWPORT = {"width": 1440, "height": 900}
