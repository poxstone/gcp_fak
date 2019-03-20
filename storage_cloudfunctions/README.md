# Cloud Storage + Cloud Functions + BigQuery
> NOTE: [use lab](https://www.qwiklabs.com/focuses/3563?parent=catalog)

## APIS
- Authorize: Cloud Vision API, Cloud Storage, BigQuery API

## Clone
```bash
git clone https://github.com/poxstone/cf_vision_bq;
```


## Deploy (cloudshell)
```bash
cd cf_vision_bq;
export PROJECT="$GOOGLE_CLOUD_PROJECT";
export BUCKET="${PROJECT}_images";
gsutil mb gs://${BUCKET};
gcloud functions deploy "event_trigger" --runtime "python37" --trigger-resource "$BUCKET" --trigger-event "google.storage.object.finalize" --project "$PROJECT";
```

## Upload image to Cloud Storage
```bash
export IMG_URL="https://images.clarin.com/2019/01/18/RBBMxtqH5_1256x620__1.jpg";
curl "$IMG_URL" -o image.jpg;
gsutil cp image.jpg gs://$BUCKET;
```


## Create Dataset and Table in BigQuery
- **Dataset name**: "storage_image"
- **Table name**: "labels"
- **Schema**: file:STRING,labels:STRING

### Simple query BigQuery
```sql
SELECT * FROM `<PROJECT_ID>.storage_image.labels`
```


