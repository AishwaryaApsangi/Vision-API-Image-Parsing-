import csv
import os
import urllib.parse
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/aishwarya/Downloads/visionapi.json'

client = vision.ImageAnnotatorClient()

def analyze_image_from_uri(image_uri: str, image_id: str):
    features = [
        vision.Feature(type_=vision.Feature.Type.FACE_DETECTION),
        vision.Feature(type_=vision.Feature.Type.IMAGE_PROPERTIES),
        vision.Feature(type_=vision.Feature.Type.LABEL_DETECTION),
        vision.Feature(type_=vision.Feature.Type.LANDMARK_DETECTION),
        vision.Feature(type_=vision.Feature.Type.LOGO_DETECTION),
        vision.Feature(type_=vision.Feature.Type.SAFE_SEARCH_DETECTION),
        vision.Feature(type_=vision.Feature.Type.OBJECT_LOCALIZATION)
    ]

    image = vision.Image()
    image.source.image_uri = image_uri
    request = vision.AnnotateImageRequest(image=image, features=features)
    response = client.annotate_image(request=request)

    return response

fieldnames = [
    'image_id', 'face_number', 'image_url', 'vertices', 'joy_likelihood',
    'under_exposed_likelihood', 'blurred_likelihood', 'anger', 'sorrow',
    'headwear', 'surprise', 'Object', 'Fraction', 'Red', 'Green', 'Blue',
    'landmark_info', 'adult', 'medical', 'spoof', 'violence', 'racy',
    'labels', 'logo_description'
]

start_line = 11633
end_line = 17258
current_line = 0

with open('labels.csv', 'w', newline='', encoding='utf-8') as outputfile:
    writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
    writer.writeheader()

    with open('labels.csv', 'w', newline='', encoding='utf-8') as outputfile:
        writer = csv.DictWriter(outputfile, fieldnames=fieldnames)
        writer.writeheader()

        with open('2_Case-Level_Dataset_One Page.csv', 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                current_line += 1
                if start_line <= current_line <= end_line:
                    if row['cases.title_img'].strip() == '':
                        result = {key: 'blank line' for key in fieldnames}
                        result['image_id'] = row['uv.case_id']
                    else:
                        encoded_image_url = urllib.parse.quote(row['cases.title_img'], safe=':/')
                        image_id = row['uv.case_id']
                        response = analyze_image_from_uri(encoded_image_url, image_id)

                        result = {
                            'image_id': image_id,
                            'face_number': len(response.face_annotations) if response.face_annotations else 0,
                            'image_url': row['cases.title_img'],
                            'vertices': ','.join(
                                ['({},{})'.format(vertex.x, vertex.y) for face in response.face_annotations for vertex in
                                 face.bounding_poly.vertices]) if response.face_annotations else 'No vertices detected',
                            'joy_likelihood': response.face_annotations[
                                0].joy_likelihood if response.face_annotations else 'Likelihood.UNKNOWN',
                            'under_exposed_likelihood': response.face_annotations[
                                0].under_exposed_likelihood if response.face_annotations else 'Likelihood.UNKNOWN',
                            'blurred_likelihood': response.face_annotations[
                                0].blurred_likelihood if response.face_annotations else 'Likelihood.UNKNOWN',
                            'anger': response.face_annotations[0].anger_likelihood if response.face_annotations else 'Likelihood.UNKNOWN',
                            'sorrow': response.face_annotations[0].sorrow_likelihood if response.face_annotations else 'Likelihood.UNKNOWN',
                            'headwear': response.face_annotations[
                                0].headwear_likelihood if response.face_annotations else 'Likelihood.UNKNOWN',
                            'surprise': response.face_annotations[
                                0].surprise_likelihood if response.face_annotations else 'Likelihood.UNKNOWN',
                            'Object': ', '.join([obj.name for obj in
                                                 response.localized_object_annotations]) if response.localized_object_annotations else 'No Objects detected',
                            'Fraction': response.image_properties_annotation.dominant_colors.colors[
                                0].pixel_fraction if response.image_properties_annotation.dominant_colors.colors else 'None',
                            'Red': response.image_properties_annotation.dominant_colors.colors[
                                0].color.red if response.image_properties_annotation.dominant_colors.colors else 'None',
                            'Green': response.image_properties_annotation.dominant_colors.colors[
                                0].color.green if response.image_properties_annotation.dominant_colors.colors else 'None',
                            'Blue': response.image_properties_annotation.dominant_colors.colors[
                                0].color.blue if response.image_properties_annotation.dominant_colors.colors else 'None',
                            'landmark_info': ', '.join([landmark.description for landmark in
                                                        response.landmark_annotations]) if response.landmark_annotations else 'No landmarks detected',
                            'adult': response.safe_search_annotation.adult if response.safe_search_annotation else 'None',
                            'medical': response.safe_search_annotation.medical if response.safe_search_annotation else 'None',
                            'spoof': response.safe_search_annotation.spoof if response.safe_search_annotation else 'None',
                            'violence': response.safe_search_annotation.violence if response.safe_search_annotation else 'None',
                            'racy': response.safe_search_annotation.racy if response.safe_search_annotation else 'None',
                            'labels': ', '.join([label.description for label in
                                                 response.label_annotations]) if response.label_annotations else 'No labels detected',
                            'logo_description': ', '.join([logo.description for logo in
                                                           response.logo_annotations]) if response.logo_annotations else 'No logos detected'
                        }

                    writer.writerow(result)

                if current_line > end_line:
                    break  

print("Processing complete.")
