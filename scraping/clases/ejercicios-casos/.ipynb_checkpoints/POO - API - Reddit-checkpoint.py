import praw
from .scraping import *

class Reddit(Scrapper):
    
    def __init__(self,username, password, client_id, secret, app_name, subreddits=[]):
        #reddit instance
        self.reddit = praw.Reddit(client_id=client_id,
                                  client_secret=secret,
                                  user_agent=app_name,
                                  username=username,
                                  password=password)
        self.client_id = client_id
        self.secret = secret
        self.app_name = app_name
    
        #predefined subreddits
        #self.subreddits = subreddits    
    
    def crawl(self, topico):
        '''
        busca subreddits relevantes al tema que 
        estoy buscnado
        devuelve urls 
        '''
        data = {}
        query = topico
        sorteo = ['new', 'hot','top', 'comments', 'relevance']
        for i in sorteo:
            url = f'https://www.reddit.com/search.json?q={query}&sort={i}&limit=100'
            response = rq.get(url)
            js = response.json()
            data[i] = js
        
        #urls = [x for x in data...]
        self.subreddits.extend(urls)

    def parse_sub(self, subreddit):
        '''
        scrapea y devuelve el dataframe con los subreddits 
        de crawl más aquellos que le indiquemos
        (chequear el parser de prawl)
        '''

        # Instanciamos subredit
        sub = reddit.subreddit(subreddit)
        
        # Creamos un diccionario para guardar la data
        topics_dict = { "title":[], "score":[], 
                    "id":[], "url":[],
                    "comms_num":[], "created": [], 
                    "body":[]}
        
        # Guardamos los top_limit topicos
        top_limit = sub.top(limit=limit)
        
        # Parseo sobre los top
        for submission in top_limit:
            topics_dict["title"].append(submission.title)
            topics_dict["score"].append(submission.score)
            topics_dict["id"].append(submission.id)
            topics_dict["url"].append(submission.url)
            topics_dict["comms_num"].append(submission.num_comments)
            topics_dict["created"].append(submission.created)
            topics_dict["body"].append(submission.selftext)
        
        # Pasamos a dataframe
        data_subreddit = pd.DataFrame(data=topics_dict)
        
        return data_subreddit
    
    def save(self, data):
        # appendear a un csv en principio, despues db
        self.csv_path = './data.csv'
        with open(self.csv_path, 'a+') as out:
            out.write(data)
    
    def start(self, topicos):
        for topico in topicos:
            subreddits = self.crawl(topico)
            for sub in subreddits:
                data = self.parse(sub)
            self.save(data)

