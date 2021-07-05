from CaptionScraper import captionScraper
import pandas as pd
from tqdm import tqdm
tqdm.pandas()

def getVID(url):
    # check if video url is valid
    try:
        # Valid only if it has "v={Video_ID}" substring
        Video_ID = url.split('v=')[1].split('&')[0]
        return Video_ID
    except:
        print("Not valid URL : {}".format(url))
        return None

if __name__ == '__main__':
    # Reading Original Dataset
    original_data_filepath = 'data.csv'
    dataset = pd.read_csv(original_data_filepath)

    # Dropping extra information
    dataset = dataset.drop(columns=["aria-label", "annotation", "notes", "duration", "favoriteCount", "popularity"])

    # Get Video_IDs from video urls (If valid)
    dataset['Video_ID'] = dataset['vid_url'].progress_apply(getVID)

    # Drop videos if Video_ID is not available. (Invalid url/Link to playlist (or channel) rather than video)
    dataset = dataset.dropna(subset=["Video_ID"])

    print(dataset.columns)
    print(dataset)

    # Get captions from Video_IDs using captionScraper
    dataset["Captions"] = dataset["Video_ID"].progress_apply(captionScraper)
    
    # Drop videos with empty captions
    dataset["Captions"] = dataset["Captions"].progress_apply(lambda x: None if x == "" else x)
    dataset = dataset.dropna(subset=["Captions"])

    print(dataset.columns)
    print(dataset)

    # Break dataset by Topic
    dataset_vaccines = dataset[dataset['Topic'] == 'vaccines']
    dataset_911 = dataset[dataset['Topic'] == '911']
    dataset_chemtrails = dataset[dataset['Topic'] == 'chemtrails']
    dataset_flatearth = dataset[dataset['Topic'] == 'flatearth']
    dataset_moonlanding = dataset[dataset['Topic'] == 'moonlanding']

    # Save to csv files
    dataset_vaccines.to_csv('data_vaccines.csv', index=False)
    dataset_911.to_csv('data_911.csv', index=False)
    dataset_chemtrails.to_csv('data_chemtrails.csv', index=False)
    dataset_flatearth.to_csv('data_flatearth.csv', index=False)
    dataset_moonlanding.to_csv('data_moonlanding.csv', index=False)