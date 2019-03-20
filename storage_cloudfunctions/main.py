from googleapiclient.discovery import build
import os


""" NOTE: Init variables """
PROJECT = os.environ['GCP_PROJECT']
DATASET = 'storage_image'
TABLE = 'labels'

vision_service = build('vision', 'v1')
bq_service = build('bigquery', 'v2')


def event_trigger(data, context):

    """ NOTE:Print event Storage object """
    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(data['bucket']))
    print('File: {}'.format(data['name']))
    print('Metageneration: {}'.format(data['metageneration']))
    print('Created: {}'.format(data['timeCreated']))
    print('Updated: {}'.format(data['updated']))

    #""" NOTE:Call to vision Api Labels """
    #gs_uri = "gs://{}/{}".format(data['bucket'], data['name'])
    #body = { "requests": [
    #          {
    #             "image": {
    #                 "source": {
    #                     "gcsImageUri": gs_uri}
    #             },
    #             "features": [{
    #                     "type": "LABEL_DETECTION"
    #                     }]
    #          }
    #        ]}
    #vision_labels = vision_service.images().annotate(body=body).execute()
    #print(vision_labels)

    #""" NOTE:Insert into BQ """
    #labels_detected = []
    #for item in vision_labels['responses'][0]['labelAnnotations']:
    #    labels_detected.append(item['description'])
    #labels_detected = ', '.join([str(x) for x in labels_detected])

    #query = "INSERT INTO `{project}.storage_image.labels` (`file`,`labels`) \
    #         VALUES ('{file_name}', '{tags}')".format(project=PROJECT,
    #                                                  file_name=data['name'],
    #                                                  tags=labels_detected)
    #body_bq = {"configuration": {
    #                "query": {
    #                    "query": query,
    #                    "useLegacySql": False
    #                    }
    #                }
    #            }
    #bq_service.jobs().insert(projectId=PROJECT, body=body_bq).execute()

    """ NOTE:Formal response """
    return 'ok'

