Case1: Ratings: count total number of ratings eg: 5*, 4*, 3*, 2*, 1*
from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
def steps(self):
return[MRStep (mapper=self.mappergetratings, 
		reducer=self.reducercountratings)]

def mappergetratings(self,_,line):	
(userID, movieID, ratings,timestamp)= line.split("\t")
 yield ratings, 1

def reducercountratings(self, key, value):
 yield key, sum(value)

if __name__=='__main__':
 RatingsBreakdown.run()

 
Case2: Movie: Count movieID & number of times MovieID has been repeated.
from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
def steps(self):
return[MRStep (mapper=self.mappergetratings, 
		reducer=self.reducercountratings)]

def mappergetratings(self,_,line):	
(userID, movieID, ratings,timestamp)= line.split("\t")
 yield movieID, 1

def reducercountratings(self, key, value):
 yield key, sum(value)

if __name__=='__main__':
 RatingsBreakdown.run()

Case3: Sort the movies with their popularity.
from mrjob.job import MRJob
from mrjob.step import MRStep

class RatingsBreakdown(MRJob):
def steps(self):
return[MRStep (mapper=self.mappergetratings, 
		reducer=self.reducercountratings),
	MRStep (reducer=self.reducersortedcount)]

def mappergetratings(self,_,line):	
(userID, movieID, ratings,timestamp)= line.split("\t")
 yield movieID, 1

def reducercountratings(self, key, value):
 yield str(sum(values)).zfill(5), key

def reducersortedcount(self, count, movies):
for movie in movies:
 yield movie, count

if __name__=='__main__':
 RatingsBreakdown.run()
