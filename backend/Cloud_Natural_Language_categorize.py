import os
from google.cloud import language_v1

# Generates category tags for the provided text by invoking
# Google Cloud Natural Language API
def tag_text(text_content):
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    response = client.classify_text(request = {'document': document})

    content_categories = []
    for category in response.categories:
        if category.name.count("/") == 1:
            content_categories.append(category.name[1:])
        else:
            category_hierarchy = category.name[1:].split('/')
            content_categories.append(category_hierarchy[0])

    return content_categories
