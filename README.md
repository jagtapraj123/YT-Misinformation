# YT-Misinformation

The Caption Scraper takes the YouTube video URL as the input and returns a text file containing captions as the output. It uses YouTube-Caption-API to get the subtitles of the video. If the subtitles are not present in English, it translates the available subtitles to English. If the channel does not provide the manual subtitles, it uses YouTube's auto-captions feature to get subtitles.

## Caption Scraper Functionalities

1. **URL Finder :** Takes input of the search string 's' or Hash-Tag 'h' and number of videos to scrape 'n'. It uses web scrapping to search the string on YouTube and outputs list of video URLs shown by YouTube search engine.

2. **Info Scraper :** Takes input of a video URL 'v'. It uses web scrapping to search the video and collect following information:       
    
    a. Title
    
    b. Description
    
    c. Number of Views
    
    d. Number of Likes-Dislikes
    
    e. Number of Comments
    
3. **Caption Scraper :** Takes the YouTube video URL as the input and returns a text file containing captions as the output

4. **Comments Scraper :** Takes input of a video URL 'v' and number of comments to scrape 'n_c'. It uses web scrapping to search the video and collect top 'n_c' number of text comments.


## Files Information
This repository contains mainly three different folders:

1. Code: contains the Caption Scraper script.
2. Dataset: contains the dataset collected using Caption Scraper script. We used this dataset in our paper titled "Misinformation Detection on YouTube Using Video Captions".
3. Results: contains the classification model results on the dataset.

## Citation
Please cite our paper using any of the mentioned format:

MLA:

Jagtap, Raj, Abhinav Kumar, Rahul Goel, Shakshi Sharma, Rajesh Sharma, and Clint P. George. "Misinformation Detection on YouTube Using Video Captions." arXiv preprint arXiv:2107.00941 (2021).

BibTex:

@article{jagtap2021misinformation,

  title={Misinformation Detection on YouTube Using Video Captions},
  
  author={Jagtap, Raj and Kumar, Abhinav and Goel, Rahul and Sharma, Shakshi and Sharma, Rajesh and P. George, Clint},
  
  journal={arXiv preprint arXiv:2107.00941},
  
  year={2021}
  
}
