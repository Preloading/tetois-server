from dataclasses import dataclass
from datetime import time
from typing import List
from datetime import datetime

@dataclass
class Artwork:
    width: int
    height: int
    url: str

@dataclass
class Uber:
    titleTextColor: str
    backgroundColor: str
    primaryTextColor: str
    masterArt: List[Artwork]

@dataclass
class App:
    id: str
    bundle_id: str
    kind: str
    name: str
    genre: str
    url: str
    tinyUrl: str
    artwork: List[Artwork]
    uber: Uber
    artistName: str
    artistUrl: str
    artistId: int
    release_date: time
    pc_rating_software: str
    pc_parental_rating: str
    user_rating:float
    user_rating_count:int
    rating_system: str
    rating_client_id: int
    

def generateLockup(app: App):
    d = {
        "componentName": "lockup",
        "id": app.id,
        "kind": app.kind,
        "name": app.name,
        "genre": app.genre,
        "url": app.url,
        "tinyUrl": app.tinyUrl,
        "artwork": [
        ],
        "uber": {
        "titleTextColor": app.uber.titleTextColor,
        "backgroundColor": app.uber.backgroundColor,
        "primaryTextColor": app.uber.primaryTextColor,
        "masterArt": []
        },
        "shareEmailBodyURL": "https://userpub.itunes.apple.com/WebObjects/MZUserPublishing.woa/wa/tellAFriendEmailBody?cc=ca&displayable-kind=11&id=719219382&name=s&type=14",
        "artistName": "Epic Creations, Inc.",
        "artistUrl": "https://apps.apple.com/ca/developer/epic-creations-inc/id719219385?softwareType=iPhone&kind=11",
        "artistId": app.artistId,
        "release_date": app.release_date.strftime("%b %d, %Y"),
        "release_date_utc": app.release_date.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "parental_control_attributes": {
            "rating-software": app.pc_rating_software,
            "parental-rating": app.pc_parental_rating
        },
        "user_rating": app.user_rating,
        "user_rating_count": app.user_rating_count,
        "rating-system": app.rating_system,
        "rating-client-id": app.rating_client_id,
        "rating-id": "1",
        "rating-name": "4+",
        "is_universal_app": "true",
        "posted": "May 29, 2026",
        "version": "7.47",
        "rated": "Ages 4+, Made for Ages 6–8",
        "genreAgeBand": "Education (Made For Ages 6–8)",
        "minimum-os-version": "12.2",
        "versionID": "886221764",
        "bundle-id": app.bundle_id,
        "icon-is-prerendered": "true",
        "required-capabilities": "armv7 ",
        "offers": [
        {
            "confirm-text": "INSTALL APP",
            "action-params": "productType=C&price=0&salableAdamId=719219382&pricingParameters=STDQ&pg=default&appExtVrsId=886221764",
            "button_text": "GET",
            "priceFormatted": "Free",
            "priceType": "STDQ",
            "assetFlavors": [
            {
                "name": "10:purple",
                "fileSize": "216641536",
                "fileSizeText": "217 MB",
                "preview": {
                "duration": None,
                "url": None
                }
            }
            ]
        }
        ],
        "pills": [
        {
            "pageComponentName": "product_details_page",
            "title": "Details"
        },
        {
            "pageComponentName": "product_reviews_page",
            "title": "Reviews"
        },
        {
            "pageComponentName": "product_related_page",
            "title": "Related"
        }
        ]
    }
    return d