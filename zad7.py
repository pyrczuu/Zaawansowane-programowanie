import argparse
import requests

URL = "https://api.openbrewerydb.org/v1/breweries"


class Brewery:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.name = data.get("name")
        self.type = data.get("brewery_type")
        self.city = data.get("city")
        self.state = data.get("state_province")
        self.country = data.get("country")
        self.website = data.get("website_url")

    def __repr__(self):
        return (f"{self.name} ({self.type}) - {self.city}, "
                f"{self.state}, {self.country}")


def get_breweries(city: str | None = None, count: int = 20) -> list[Brewery]:
    params = {"per_page": count}
    if city:
        params["by_city"] = city
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    return [Brewery(item) for item in response.json()]
