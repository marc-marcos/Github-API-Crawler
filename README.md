# Github-API-Crawler

This project attempts to crawl through the followers of users of Github and then display them in a nice and stylish way. This is achieved by providing the script with an initial username and then the script will crawl through that users followers and through that users' followers followers and so on. The limit to that can be set through the script and in order to work the script needs a Github token (free) and an initial Github user.

All the requirements can be checked in the ``requirements.txt`` file.

The program exports the results to a format where the program Obsidian MD can interpret them to form graphics like these:

![obsidian image](README/img.jpg)

This image corresponds to a network of depth 50, that is the scripts default value.

