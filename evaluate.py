import data

def count(shared_urls, info, tweets):
    #matching = [dataset_by_url[el] for el in shared_urls if el in dataset_by_url]
    #verified = [el for el in matching if el['label'] == 'true']
    #fake = [el for el in matching if el['label'] == 'fake']
    results = [data.classify_url(url, info) for url in shared_urls] # NEED TWEET ID here
    matching = [el for el in results if el]
    verified = [el for el in matching if el['label'] == 'true']
    fake = [el for el in matching if el['label'] == 'fake']
    return {
        'tweets_cnt': len(tweets),
        'shared_urls_cnt': len(shared_urls),
        'verified_cnt': len(verified),
        'fake_cnt': len(fake),
        'fake_urls': fake,
        'true_urls': verified,
        'unknown_cnt': len(shared_urls) - len(matching)
    }
