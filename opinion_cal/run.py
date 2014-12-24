#-*-coding=utf-8-*-

import time
from utils import _default_mongo
from config import MONGO_DB_NAME, EVENTS_NEWS_COLLECTION_PREFIX, \
        START_TS, END_TS
from Info import News
from Event import Event
from Features import Feature
from trace import subevent_classifier
from duplicate_filter import max_same_rate, max_same_rate_shingle


if __name__ == '__main__':
    mongo = _default_mongo(usedb=MONGO_DB_NAME)
    topic = "APEC2014"
    topicid = "54916b0d955230e752f2a94e"

    event = Event(topicid)
    subevents = event.getSubEvents()
    feature_words_list = []
    labels_list = []
    """
    for subevent in subevents:
        subeventid = subevent["id"]
        feature = Feature(subeventid)
        fwords = feature.get_newest()
        feature_words_list.append(fwords)
        labels_list.append(subeventid)
    """

    results = event.getInfos(START_TS, END_TS)
    count = 0
    now = time.time()
    items = []
    for r in results:
        r['text4duplicate'] = r['title'] + r['content168']
        """
        if max_same_rate(items, r) < 0.8:
            items.append(r)
        """
        rate = max_same_rate_shingle(items, r)
        if rate < 0.2:
            items.append(r)
        print time.time() - now

        """
        news = News(r["_id"], event.id)
        label = subevent_classifier(r['title'].encode('utf-8') + r['content168'].encode('utf-8'), labels_list, feature_words_list)

        if label == "other":
            label = event.getOtherSubEventID()

        news.update_news_subeventid(label)
        """

        count += 1
        if count == 100:
            print count, ' need ', time.time() - now, ' seconds'

    print count, ' need ', time.time() - now, ' seconds'

    print len(items)
    for item in items:
        pass
        #print item["title"]

