# DIRC
## Directory of Internet Recipes &amp; Cocktails

DIRC is a curated directory of high quality cooking websites that are free of intrusive popup advertisements. The websites are crawled and indexed to create a special purpose recipe search engine which can be found at https://iri.cooking

The theory behind this project is that a human managed web directory can serve as the basis for higher quality search engines. Help is needed in order to scale up the list of websites so any submissions or suggestions are greatly appreciated

## Contributing

There are 2 ways to contribute links to the directory.
1. Create a pull request here on the repository. Then add an entry to 'Directory/iri.ini' file according to the guidelines list below.
2. Submit links using the form at https://iri.cooking/contact.php

## Submission Guidelines

The purpose of IRI.cooking is to help people avoid low quality cooking websites that are cluttered with ads. So we can’t accept low effort content farm sites, AI generated slop or anything with popup ads

Absolutely no video ads! They noticeably slow down browsers, especially for people using older devices

Static ads are acceptable. For example, if you have a blog that contains a banner promoting your new cookbook then that is fine. Or if a recipe on your site has a paid promotion then that is okay too. The ads that we’re avoiding are the embedded algorithmic popups created by internet advertising companies

An ad at the very bottom of a page is also fine so long as it is a static image or gif, not a video

## Why No Popup Ads at all?

‘too many’ popups is hard to define. How much is that? 2? 4? 10?
It’s easier to just not accept websites that have any at all. Further more, sometimes all it takes is one popup video to slow your browser down, especially if you are on an old or low powered device

## Project Status

DIRC is a hobby project and still in development. The goal is to be a proof of concept for a new way to create search engines. If all goes well then, in theory, the same concept could be used to create a general purpose search engine
Also I like to cook and I think most of the popular recipe websites are terrible

## Directory Structure

The directory is an ini file which contain the website entries.

Example entry:

[Recipes from The Great British Bake Off]

author=Love Productions

info=The Great British Bake Off is the ultimate baking battle where passionate amateur baking fans compete to be crowned the UK’s Best Amateur Baker.

tags=tv shows

rating=good

startURL=https://thegreatbritishbakeoff.co.uk/recipes

crawlURLFilters=https://thegreatbritishbakeoff.co.uk

scrapeURLFilters=thegreatbritishbakeoff.co.uk/recipes/

dontCrawlURLFilters=^https://thegreatbritishbakeoff.co.uk/bake-offs/,^https://thegreatbritishbakeoff.co.uk/your-bakes/,collection=

dontScrapeURLFilters=

Required Fields:
1. [TITLE]
This is the title of the website
2. author=Author of site
3. info=A brief description of the site
tags=The Category or relevant words
4. rating=good
Rating is either (mid, good, great)
5. startURL=Where the crawler should start crawling

Optional Fields:
These parameters are for the web crawler and don't need to be included
1. crawlURLFilters=A list of strings or regular expressions for which URLs the crawler should follow
2. scrapeURLFilters=A list of strings or regular expressions for which URLs the crawler should index
3. dontCrawlURLFilters=A list of strings or regular expressions for which URLs the crawler should explicitly avoid
4. dontScrapeURLFilters=A list of strings or regular expressions for which URLs the crawler should explicitly not index
