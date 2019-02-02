from watson_developer_cloud import ToneAnalyzerV3
import configparser
import json

config = configparser.ConfigParser()
config.read("config.ini")

tone_analyzer = ToneAnalyzerV3(
    version = "2019-02-02",
    iam_apikey = config["Watson"]["watsonApi"],
    url = config["Watson"]["watsonUrl"]
)


# returns json file
def query(text):
    tone_analysis = tone_analyzer.tone({"text": text}, "application/json").get_result()
    return json.dumps(tone_analysis, indent=2)

