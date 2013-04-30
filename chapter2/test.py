from recommendations import critics
from recommendations import sim_distance
import recommendations
import pydelicious
from deliciousrec import *

def p():
	for item in critics['Lisa Rose']:
		if item in critics['Gene Seymour']:
			print item

def test():
	s = set()
	print s
	s.add('a')
	s.add(1)
	print s

def getPersons():
	return set([person for person in critics])

def getFilms():
	return set([item for person in critics for item in critics[person]])

if __name__ == "__main__":  

	if 1>10:
		test()
		exit(0)
	
	rem = recommendations	
	deli = pydelicious

	print "----------------------------------------------------------------"
	for who in getPersons():
		scores = [(rem.sim_pearson(critics,who,other),other) for other in getPersons() if who!=other]
		scores1 = [(rem.sim_distance(critics,who,other),other) for other in getPersons() if who!=other]
		scores.sort()
		scores.reverse()
		scores1.sort()
		scores1.reverse()
		print who
		print "\t"+str(scores)
		print "\t"+str(scores1)
	print "----------------------------------------------------------------"

	# p()
	# print recommendations.sim_distance(critics,'Lisa Rose','Gene Seymour')
	# print recommendations.sim_pearson(critics,'Lisa Rose','Gene Seymour')
	# print rem.topMatches(critics,'Toby',similarity=sim_distance)
	
	# print "-----------persons------------"
	# for who in getPersons():
	# 	print who
	# print "-----------films------------"
	# for item in getFilms():
	# 	print item	
	# for who in getPersons():
	# 	print ""
	# 	print "-----------"+who+"------------"
	# 	print rem.topMatches(critics,who,n=5)
	# 	for item in critics[who]:
	# 		print item
	# 	print rem.getRecommendations(critics,who)
	# 	print rem.getRecommendations(critics,who,similarity=sim_distance)

	# ************************************************************************************************************************************
	for item in getFilms():
		print item
		movie = rem.transformPrefs(critics)
	# 	print "\t sim_pearson "+str(rem.topMatches(movie,item))
	# 	print "\t sim_distance "+str(rem.topMatches(movie,item,similarity=sim_distance))
		print "\t"+str(rem.getRecommendations(movie,item))
	# 	can list all the human who like the same thing, will it be useful for tuangou???
	# ************************************************************************************************************************************

	# print 

	# itemsim = rem.calculateSimilarItems(critics)
	# print itemsim
	# for item in itemsim:
	# 	print item
	# 	print "\t sim_distance "+str(itemsim[item])

	# print deli.get_popular(tag='mahout')
	# print deli.get_urlposts('http://www.baeldung.com/persistence-with-spring-series/')

	# delusers=initializeUserDict('programming')
	# delusers['tsegaran']={}
	# fillItems(delusers)
	# print delusers


	# ************************************************************************************************************************************
	# calc similarity using topMatches, whatever item or user, like below, but notice the data set is diff, 
	# and the pearson similarity is better i think.
	# rem.topMatches(critics,'Toby',similarity=sim_distance) 
	# rem.topMatches(transformPrefs(critics),item,similarity=sim_distance) 
	# rem to 'toby' by item and user base recommender
	itembase = rem.getRecommendedItems(critics,rem.calculateSimilarItems(critics),'Toby')
	userbase = rem.getRecommendations(critics,'Toby')	
	print itembase
	print userbase	
	avg_item_user_base = [((item[0]+item_u[0])/2,item[1]) for item in itembase for item_u in userbase if item[1] == item_u[1]]
	print avg_item_user_base
	# ************************************************************************************************************************************


