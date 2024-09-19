from datetime import datetime
import json
import logging
import requests

from django.core.exceptions import MultipleObjectsReturned
from server.presentations.models import Creator, Presentation


class PresentationsParser:

    def __init__(self, file_path):
        self.file_path = file_path

    @staticmethod
    def parse_image(image_url):
        try:
            response = requests.get(image_url)
            return response.url
        except Exception as error:
            logging.error("Error fetching image: %s ", error)
            return image_url

    @staticmethod
    def parse_date(date_string):
        return datetime.strptime(date_string, "%B %d, %Y")

    @staticmethod
    def parse_creator(creator):
        try:
            creator_obj, _ = Creator.objects.get_or_create(
                name=creator["name"], defaults={"profile_url": creator["profileUrl"]}
            )
        except MultipleObjectsReturned:
            creator_obj = Creator.objects.filter(name=creator["name"]).first()

        return creator_obj

    def parse_and_save(self, image_request=True):
        with open(self.file_path, newline="") as json_file:
            raw_data = json.load(json_file)
            presentations = []

            for row in raw_data:
                presentation = dict()
                presentation["title"] = row.get("title", "")
                presentation["thumbnail"] = self.parse_image(row["thumbnail"]) if image_request else row["thumbnail"]
                presentation["creator"] = self.parse_creator(row["creator"])
                presentation["created_at"] = self.parse_date(row["createdAt"])
                presentations.append(Presentation(**presentation))

        try:
            Presentation.objects.bulk_create(presentations)
        except Exception as error:
            logging.error("Cannot create presentations due to {}".format(error))
