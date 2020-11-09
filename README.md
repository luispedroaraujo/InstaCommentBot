# InstaBotComment
Basic automation for Instagram random tags/comments using **Python**, **Selenium** and **ChromeDriver**
> Created to send random tags in Instagram giveaways but it can be useful for other purpose.

## Variables and arguments:
**postUrl**: array with posts' URL that you want to comment;

**nLines**: array with the "number" of tags you want to comment on each post, respectively (index based);

**nseed**: the random number generator needs a number to start with (a seed value), to be able to generate a random number.

**smallDelay, mediumDelay, bigDelay, username and password** are self-explanatory.

## What do you need:
- [Python](http://python.org/downloads/)
- [Selenium](https://selenium-python.readthedocs.io/installation.html)
- [ChromeDriver](http://chromedriver.chromium.org)

## General usage
### `instaBot.py`
- Adapt **postUrl** with the posts that you want to comment, and **nLines** with the number of tags/comments you want.
- Change **usarname** and **password** with your Instagram credentials.
### `accountsToTag.txt`
- In `accountsToTag.txt` you can put the accounts/comments you want to tag/send.

## Intallation
### On macOS:
- Use `pip`or `pip3`:
```bash
sudo pip3 install selenium
brew cask install chromedriver
```
- Use `python`or `python3`:
```bash
python3 instaBot.py
```

## Next steps:
- Remove **smallDelay** and wait for page load;
- Improve random accounts selection when using multiple tags in the same comment;
- Implement **nLines** dynamically;
- ...
