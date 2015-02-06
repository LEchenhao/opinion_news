#-*-coding=utf-8-*-
"""默认参数配置文件
   default_settings.py
"""

MONGOD_PORT = 27017
MONGOD_HOST = 'localhost'

MONGO_DB_NAME = 'news'

EVENTS_COLLECTION = 'news_topic'
SUB_EVENTS_COLLECTION = 'news_subevent'
SUB_EVENTS_FEATURE_COLLECTION = 'news_subevent_feature'
EVENTS_NEWS_COLLECTION_PREFIX = 'post_'
EVENTS_COMMENTS_COLLECTION_PREFIX = 'comment_'
COMMENTS_CLUSTER_COLLECTION = 'comment_cluster'

MARKET_WORDS = 'market_words.txt'

HAPPY_WORDS = './words/happy.txt'
ANGRY_WORDS = './words/angry.txt'
SAD_WORDS = './words/sad.txt'

# clustering.py
CLUSTERING_CLUTO_FOLDER = 'cluto'
CLUSTERING_CLUTO_EXECUTE_PATH = './cluto-2.1.2/Linux-i686/vcluster'
CLUSTERING_KMEANS_CLUSTERING_NUM = 10
CLUSTERING_TOPK_FREQ_WORD = 20 # 计算每类tfidf词前，选取的高频词的数量
CLUSTERING_CLUSTER_EVA_TOP_NUM = 5 # 聚类评价时保留的聚类数
CLUSTERING_CLUSTER_EVA_LEAST_FREQ = 10 # 
CLUSTERING_CLUSTER_EVA_LEAST_SIZE = 8 #

# comment_clustering_tfidf_v7

