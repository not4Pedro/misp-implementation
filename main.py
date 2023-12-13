from pathlib import Path

from TaranisObject import TaranisObject
from pymisp import ExpandedPyMISP, MISPEvent, MISPObject
import logging, json


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    type = "MISP_PUBLISHER"
    name = "MISP Publisher"
    description = "Publisher for publishing in MISP"

    misp_url = "https://localhost"
    misp_verifycert = False
    misp_key = "MYVK7a8HU9CQroHIiKRQ8Eo4GzgQmZyf5jxRHg26"

    # event_json = {
    #     "org_id": "1231231231416",
    #     "distribution": "0",
    #     "info": "wow_with_attribute",
    #     "orgc_id": "123452",
    #     # "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b11",
    #     "date": "1991-01-15",
    #     "published": False,
    #     "analysis": "0",
    #     "attribute_count": "321",
    #     "timestamp": "1617875569",
    #     "sharing_group_id": "1",
    #     "proposal_email_lock": True,
    #     "locked": True,
    #     "threat_level_id": "1",
    #     "publish_timestamp": "1617875569",
    #     "sighting_timestamp": "1617875569",
    #     "disable_correlation": False,
    #     # "extends_uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b11",
    #     "event_creator_email": "test@example.com",
    #     "Attribute": [{
    #         "category": "External analysis",
    #         "type": "text",
    #         "value": "This is a story",
    #         "to_ids": False,
    #         "uuid": "c99506a6-1255-4b71-afa5-7b8ba48c3b1s",
    #         "timestamp": "1617875569",
    #         "distribution": "0",
    #         "sharing_group_id": "1",
    #         "comment": "logged source ip",
    #         "deleted": False,
    #         "disable_correlation": True
    #     }]
    # }
    event_json = {
        # # "distribution": "0",
        # "info": "Event with Taranis objects",
        # # "orgc_id": "taranis_id",
        # "disable_correlation": False

        "info": "Live Exploitation Underscores Urgency to Patch Critical WS-FTP Server Flaw",
        "orgc_id": "1",
        "date": "2023-09-26",
        "analysis": "0",
        "attribute_count": "11",
        "sharing_group_id": "1",
        "sighting_timestamp": "1695945600",
        "disable_correlation": False,

        "Tag": [
            {
                "id": "12345",
                "name": "Mastodon",
                "colour": "#ffff00",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "APIs",
                "colour": "#ffff00",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Richard Bird",
                "colour": "#ff8000",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Richard",
                "colour": "#ff8000",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "CNBC",
                "colour": "#cc6600",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Center",
                "colour": "#cc6600",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Firefox",
                "colour": "#cc6600",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Firefox ESR",
                "colour": "#cc6600",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "CVE-2023-3467",
                "colour": "#cc0000",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "CVE-2023-3466",
                "colour": "#cc0000",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "CVE-2023-3519",
                "colour": "#cc0000",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "CVE-2023-42657",
                "colour": "#cc0000",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "CVE-2023-40044",
                "colour": "#cc0000",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Facebook",
                "colour": "#cc00cc",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Apple",
                "colour": "#cc00cc",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Controls",
                "colour": "#cc00cc",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Mitsubishi Electric",
                "colour": "#cc00cc",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            },
            {
                "id": "12345",
                "name": "Sony",
                "colour": "#cc00cc",
                "exportable": True,
                "org_id": "12345",
                "user_id": "12345",
                "hide_tag": False,
                "numerical_value": "12345",
                "is_galaxy": True,
                "is_custom_galaxy": True,
                "inherited": 1
            }
        ]

    }

    # @description is "title"
    # @references is link
    # @summary is content
    # @published stays unchanged
    # object_json
    stories = [
        # {
        #     "title": "Test News Item 1",
        #     "link": "https://url/13",
        #     "content": "CVE-2020-1234 - Test Aggregate 1",
        #     "published": "2023-08-01T17:01:04.801998"
        # },
        # {
        #     "title": "Test News Item 2",
        #     "link": "https://url/13",
        #     "content": "CVE-2020-1234 - Test Aggregate 1",
        #     "published": "2023-08-01T17:01:04.801998"
        # },
        # {
        #     "title": "Test News Item 3",
        #     "link": "https://url/13",
        #     "content": "CVE-2020-1234 - Test Aggregate 1",
        #     "published": "2023-08-01T17:01:04.801998"
        # },
        # {
        #     "title": "Test News Item 4",
        #     "link": "https://url/13",
        #     "content": "CVE-2020-1234 - Test Aggregate 1",
        #     "published": "2023-08-01T17:01:04.801998"
        # },
        # {
        #     "title": "Test News Item 5",
        #     "link": "https://url/13",
        #     "content": "CVE-2020-1234 - Test Aggregate 1",
        #     "published": "2023-08-01T17:01:04.801998"
        # }

        {
            "title": "Progress warns of maximum severity WS_FTP Server vulnerability",
            "link": "bleepingcomputer.com",
            "content": "Progress warns of maximum severity...",
            "published": "2023-12-12T15:52:07.132Z",
            "author": "Sergiu Gatlan"
        },
        {
            "title": "Case closed: DIVD-2023-00033",
            "link": "csirt.divd.nl",
            "content": "CVE-2020-1234 - Test Aggregate 1",
            "published": "2023-08-01T17:01:04.801998"
        },
        {
            "title": "Live Exploitation Underscores Urgency to Patch Critical WS-FTP Servers",
            "link": "feeds.feedburner.com",
            "content": "DIVD-2023-00033 - Citrix systems expl...",
            "published": "2023-08-01T17:01:04.801998",
            "author": "Ryan Naraine"
        },
        {
            "title": "Security researchers believe mass exploitation attempts against WS_FTP servers",
            "link": "theregister.co.uk",
            "content": "Security researchers believe mass exp...",
            "published": "2023-08-01T17:01:04.801998"
        }
    ]

    misp = ExpandedPyMISP(misp_url, misp_key, misp_verifycert)
    event = MISPEvent()

    event.load(event_json)

    #########################
    for story in stories:
        taranis_obj = TaranisObject(parameters=story,
                                    misp_objects_path_custom='venv/lib/python3.11/site-packages/pymisp/data/misp-objects/objects')
        event.add_object(taranis_obj)
    #########################

    # this can add an attribute using an existing template
    # misp_object = event.add_object(name='vulnerability')
    # misp_object.from_json(object_json)

    # Approach #1
    # Enclosed code for remapping
    #     if key == 'title':
    #         key = 'description'
    #     elif key == 'link':
    #         key = 'references'
    #     elif key == 'content':
    #         key = 'summary'
    # for key, value in object_json.items():
    #     misp_object.add_attribute(key, value=value)
    #
    # print(event.to_json())
    #
    misp.add_event(event)
