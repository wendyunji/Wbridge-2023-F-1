from gensim.models import doc2vec, Doc2Vec
from gensim.models.doc2vec import TaggedDocument
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

# 파일로부터 모델을 읽는다. 없으면 생성한다.
try:
    d2v_faqs = Doc2Vec.load('d2v_faqs_size200_min5_epoch20_jokes.model')
    lemmatizer = WordNetLemmatizer()
    stop_words = stopwords.words('english')
    faqs = pd.read_csv('jokes.csv')
except:
    faqs = pd.read_csv('jokes.csv')
    nltk.download('punkt')
    # 토근화
    tokened_questions = [word_tokenize(question.lower()) for question in faqs['Question']]
    lemmatizer = WordNetLemmatizer()
    nltk.download('wordnet')
    # lemmatization
    lemmed_questions = [[lemmatizer.lemmatize(word) for word in doc] for doc in tokened_questions]
    nltk.download('stopwords')
    # stopword 제거 불용어 제거하기
    stop_words = stopwords.words('english')
    questions = [[w for w in doc if not w in stop_words] for doc in lemmed_questions]
    # 리스트에서 각 문장부분 토큰화
    index_questions = []
    for i in range(len(faqs)):
        index_questions.append([questions[i], i ])

    # Doc2Vec에서 사용하는 태그문서형으로 변경
    tagged_questions = [TaggedDocument(d, [int(c)]) for d, c in index_questions]
    # make model
    import multiprocessing
    cores = multiprocessing.cpu_count()
    d2v_faqs = doc2vec.Doc2Vec(
                                    vector_size=200,
                                    hs=1,
                                    negative=0,
                                    dm=0,
                                    dbow_words=1,
                                    min_count=5,
                                    workers=cores,
                                    seed=0,
                                    epochs=20
                                    )
    d2v_faqs.build_vocab(tagged_questions)
    d2v_faqs.train(tagged_questions,
                   total_examples=d2v_faqs.corpus_count,
                   epochs=d2v_faqs.epochs)

    d2v_faqs.save('d2v_faqs_size200_min5_epoch20_jokes.model')

# FAQ 답변
def faq_answer(input):
    # 테스트하는 문장도 같은 전처리를 해준다.
    tokened_test_string = word_tokenize(input)
    lemmed_test_string = [lemmatizer.lemmatize(word) for word in tokened_test_string]
    test_string = [w for w in lemmed_test_string if not w in stop_words]

    topn = 5
    test_vector = d2v_faqs.infer_vector(test_string)
    result = d2v_faqs.docvecs.most_similar([test_vector], topn=topn)
    print(result)

    for i in range(topn):
        print("{}위. {}, {} {} {}".format(i + 1, result[i][1], result[i][0], faqs['Question'][result[i][0]], faqs['Answer'][result[i][0]]))

    return faqs['Answer'][result[0][0]]


faq_answer("What do you call a person who is outside a door and has no arms nor legs?")