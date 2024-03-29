from ..evaluation import evaluate
from ..external import twitter_connector


def analyse_url(url, allow_cached=False, only_cached=False):
    pass


def analyse_tweet(tweet_id, allow_cached=False, only_cached=False):
    pass


def analyse_twitter_account(
    twitter_id, allow_cached=False, only_cached=False, use_credibility=False
):
    user = twitter_connector.get_twitter_user(twitter_id)
    tweets = twitter_connector.get_user_tweets(user["id"])
    return evaluate.count_user(user, tweets, allow_cached, only_cached, use_credibility)


def analyse_twitter_account_from_screen_name(
    twitter_screen_name,
    allow_cached=False,
    only_cached=False,
    use_credibility=False,
    update_status_fn=None,
):
    print(update_status_fn)
    if update_status_fn:
        update_status_fn("getting information about the profile")
    user = twitter_connector.search_twitter_user_from_screen_name(twitter_screen_name)
    if update_status_fn:
        update_status_fn("retrieving the tweets of the profile")
    tweets = twitter_connector.get_user_tweets(user["id"])
    if update_status_fn:
        update_status_fn("unshortening the URLs contained in the tweets")
    result = evaluate.count_user(
        user, tweets, allow_cached, only_cached, use_credibility
    )
    # print(result)
    return result


def analyse_friends_from_screen_name(
    screen_name, limit, allow_cached=True, only_cached=True, use_credibility=False
):
    """Returns the analysis for all the friends, default cached"""
    friends = twitter_connector.search_friends_from_screen_name(screen_name, limit)
    if limit:
        friends = friends[:limit]
    result = []
    for friend in friends:
        user_cnt = evaluate.count_user(
            friend, [], allow_cached, only_cached, use_credibility
        )
        result.append(user_cnt)
    return result


def analyse_friends(
    user_id, limit, allow_cached=True, only_cached=True, use_credibility=False
):
    """Returns the analysis for all the friends, default cached"""
    user = twitter_connector.get_twitter_user(user_id)
    friends = twitter_connector.search_friends_from_screen_name(user["screen_name"])
    if limit:
        friends = friends[:limit]
    result = []
    for friend in friends:
        user_cnt = evaluate.count_user(
            friend, [], allow_cached, only_cached, use_credibility
        )
        result.append(user_cnt)
    return result


def analyse_twitter_accounts_from_screen_name(
    twitter_screen_names, allow_cached=True, only_cached=True, use_credibility=False
):
    """Returns the analysis for all the friends, default cached"""
    result = []
    for screen_name in twitter_screen_names:
        user = twitter_connector.search_twitter_user_from_screen_name(screen_name)
        if not user:
            continue
        if not allow_cached:
            print("retrieving tweets")
            tweets = twitter_connector.get_user_tweets(user["id"])
        else:
            tweets = []
        user_cnt = evaluate.count_user(
            user, tweets, allow_cached, only_cached, use_credibility
        )
        result.append(user_cnt)
    return result


def analyse_time_distribution_url(url, time_granularity):
    return evaluate.analyse_url_distribution(url, time_granularity=time_granularity)


def analyse_time_distribution_tweets(tweet_ids, time_granularity, mode, reference_date):
    return evaluate.analyse_tweet_time(
        tweet_ids, time_granularity, mode, reference_date
    )
