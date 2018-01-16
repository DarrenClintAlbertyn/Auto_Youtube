Feature: Search and Download your song

  Scenario Outline: Download your Youtube Tracks
    Given the name of the artist is "<artist>" and the songname is "<songName>"
    Given the downloader is opening to download your Track
    Given the page is open and clicks on the Links


Examples:
|artist				|songName							|
|Eddie Murphy		|Party all the time					|

