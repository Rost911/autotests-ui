from elements.base_element import BaseElement
from playwright.sync_api import Locator


class Link(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        return super().get_locator(**kwargs).nth(nth)