import base64
from datetime import datetime
import json
import os

from flask import Blueprint, request, redirect, send_file, render_template, Response
import config
from jinja2 import Environment, FileSystemLoader
import get
import baseios6
import page_components.lockup
import page_components.swoosh
import plistlib

homepage = Blueprint("homepage", __name__)

# jinja2 path
env = Environment(loader=FileSystemLoader('templates'))


@homepage.route("/bag2.xml")
def bag2file():
    return get.template('bagencoded.jinja2',{
            'server_url': config.OUTGOING_ADDRESS,
            
        })

@homepage.route("/bag.xml")
def bagfile():
    baddie_file = get.template('bagcontent.jinja2',{
            'server_url': config.OUTGOING_ADDRESS,
            
        })
    pl = dict(
        bag = baddie_file.encode(),
        certs = [
            base64.b64decode("MIIDRjCCAi6gAwIBAgIBBDANBgkqhkiG9w0BAQUFADB+MRMwEQYDVQQKEwpBcHBsZSBJbmMuMRUwEwYDVQQLEwxpVHVuZXMgU3RvcmUxGjAYBgNVBAMTEWlUdW5lcyBTdG9yZSBSb290MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTESMBAGA1UEBxMJQ3VwZXJ0aW5vMB4XDTEzMDUzMTAyMTAxNVoXDTE4MDUzMDAyMTAxNVowgYExEzARBgNVBAoTCkFwcGxlIEluYy4xFTATBgNVBAsTDGlUdW5lcyBTdG9yZTEdMBsGA1UEAxMUaVR1bmVzIFN0b3JlIFVSTCBCYWcxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRIwEAYDVQQHEwlDdXBlcnRpbm8wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAKXjMEPJ9vviPcCti/L1X/7mvv8l09B6xEh+R6sHi78kpO2Yan5hujq3AaCADngFMgMf4EabroGlpzZq8ZrZ39l/9wSCYP5pWsqtvlsUWfBRcZBMSluq46CkraiRAKimFdQkHpRDY/xvj7ssklGT/d6ErJ9T4xTcP7O/rymAy2OfAgMBAAGjTzBNMB0GA1UdDgQWBBT0yZ9Y7+LfAwy/x0tierNMO/1O1jAfBgNVHSMEGDAWgBSw2uF/qItKaoFdDKGEVkYeau/lzzALBgNVHQ8EBAMCB4AwDQYJKoZIhvcNAQEFBQADggEBAFRXv/OQVGq6Pc2epJG9oz6+3ZaK2AyhlaXdymMu2ExDSwU9vIHmrsZl5bycNWeyVKpJJNFbzDwonTBnfriG+R/GURK48TT9/EGEJolb9nJUkQ7botMkfd7leyU8wbURggRjx6jlVmC4DZlbVtX0QT43sxmhllVgU+2PYtbxwtm1Px7lKJlicuzuJUdxTJ08LWQAdjwsoQfOVtkj6sRbQOB2Lj2bkwyRWtKNgdlcTk08y76Mo/phaRM7EktzX7qWm6WpyaFT/AFozOiEXXzp5oLUHh/Bf3m7ImJBDubbott1dDNlFRcSjgrg2kz4ru/asmTidrVF4H5gBeyIQ67+ktM=")
        ],
        signature = base64.b64decode("FXC1ZSUFKVdThvf4OO9rRHFvpMlbMbZN+oPqtZLimFdvK/8eXytMBP77PXzWPQRUCLGOqvcm69tu+/bFJVfxF0NGBR5CBD/yXjQx4Qx9dNllspnkKh7q7OT65vEhWXq8yyeP6dDCzLlqW97vpFCFVBxiKF/rtCsaksHTeJsH6K4=")
    )
    return Response(plistlib.dumps(pl), mimetype='application/x-plist')

@homepage.route("/WebObjects/MZStore.woa/wa/footerSections")
def footer():
    return get.template('footer.xml.jinja2',{
            'server_url': config.OUTGOING_ADDRESS,
        })

@homepage.route("/WebObjects/MZStore.woa/wa/viewGrouping")
def homepage2():
    homepage_data = baseios6.BASE_UI

    testapp = page_components.lockup.App(
        id="719219382",
        bundle_id="dev.preloading.epic",
        kind="software",
        name=":3 app",
        genre="Gaming",
        url="https://preloading.dev",
        tinyUrl="https://preloading.dev",
        artwork=[page_components.lockup.Artwork(
            width=64,
            height=64,
            url="http://preloading.dev/static/images/background_anim.gif"
        )],
        uber=page_components.lockup.Uber(
            titleTextColor="021316",
            backgroundColor="00d8fb",
            primaryTextColor="021316",
            masterArt=[]
        ),
        artistName=":3 productions",
        artistUrl="https://preloading.dev",
        artistId=719219385,
        release_date=datetime.now(),
        pc_rating_software="100,itunes-games",
        pc_parental_rating="1",
        user_rating="5",
        user_rating_count="30942829",
        rating_system="itunes-games",
        rating_client_id=100,
    )

    appJson = page_components.lockup.generateLockup(testapp)
    container = page_components.swoosh.generate_swoosh(":3 nya~ uwu", [appJson], "https://example.com")

    homepage_data['pageData'] = {
        'resourceBasePath':'http://apps.apple.com/htmlResources/9ae3/files/',
        'pageComponent':'grouping_page',
        'groupingData':{
            "groupingId":"25208",
            "genreId":"36",
            "stack":[container],
            "quickLinks":[],
            "headerImages":None,
            "pageTitle":"App Store",
            "metricsBase":{
                "pageType":"Genre",
                "pageId":"25208",
                "pageDetails":"Mobile Software Applications_25208",
                "page":"Genre_25208",
                "serverInstance":"2500275",
                "storeFrontHeader":"143455-6,16",
                "language":"6",
                "storeFront":"143455"
            }
        },
        'sf6ResourceImagePath':'https://s.mzstatic.com/9ae3/frameworks-sf6/images/'
    }

    return get.template('homepage.jinja2',{
                'serverData': json.dumps(homepage_data) ,
                
            })