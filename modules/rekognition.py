import boto3
import downloadImage
import slackMessage

rekognitionConnection = boto3.client('rekognition')

def rekognise(imageUrl):
    image = downloadImage.getImage(imageUrl)
    imgobj = {'Bytes': image.read()}
    rekresp = rekognitionConnection.detect_labels(Image=imgobj, MaxLabels=123)
    return getIsHotdog(rekresp)

def rekImage(requestForm):
    imageUrl = requestForm['text']
    return slackMessage.notifySlackChannel(requestForm, rekognise(imageUrl))

def getIsHotdog(response):
    for label in response['Labels']:
        if label['Name'] == "Hot Dog":
            return "Is " + label['Name']
    return "Not Hot Dog"
