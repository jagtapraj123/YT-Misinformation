from youtube_transcript_api import YouTubeTranscriptApi

def captionScraper(videoID):
    # videoID = url.split('v=')[1].split('&')[0]
    # print("Video ID", videoID)
    found = False

    try:
        # Get list of captions available.
        transcript_list = YouTubeTranscriptApi.list_transcripts(videoID)
        captionDict = {}
        try:
            # Check if caption in "en" or "en-US" language is present.
            transcript = transcript_list.find_transcript(['en', 'en-US'])
            captionDict = transcript.fetch()
            found = True
        except:
            # If not, Translate from other language captions.
            print("Transcript for video {} not found. Translating from other language.".format(videoID))
            for transcript in transcript_list:
                captionDict = transcript.translate('en').fetch()
                found = True
                break
        
        # Caption returned is timestamped.
        # Removing timestamps and compile a string of caption.
        if found:
            caption = ""
            for each in captionDict:
                text = each['text']
                if ('[' not in text) and (']' not in text):
                    caption = caption + ' ' + text
            # print("Processed Caption : ", caption)
            caption = ' '.join(caption.split('\n'))
            return str(caption.strip())
        else:
            return None
    except:
        return None

    
