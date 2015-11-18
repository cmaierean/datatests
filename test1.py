##############################################
# Carmen Maierean (cmaierean@gmail.com)
##############################################

import csv
import numpy as np
import urllib2
import matplotlib.pyplot as plt 


def get_csv():
	response = urllib2.urlopen("http://stat.columbia.edu/~rachel/datasets/nyt1.csv")
	cr = csv.reader(response)
	data = list(cr)
	return data

def parse_csv(data):
	users = {0:[0, 0, 0, 0, 0, 0,0, 0]}
	basicctr = 0
	ctrgroup = 0
	userno = 1
	for row in data:
		if row[0] == "Age":
			continue
		if int(row[2]) != 0:
			basicctr = float(row[3])/float(row[2])
		else:
			basicctr = 0
		
		if int(row[0]) < 18:
			agegroup = 0
		if int(row[0]) >= 18 and int(row[0]) < 24:
			agegroup = 1
		if int(row[0]) >= 25 and int(row[0]) < 34:
			agegroup = 2
		if int(row[0]) >= 35 and int(row[0]) < 44:
			agegroup = 3
		if int(row[0]) >= 45 and int(row[0]) < 54:
			agegroup = 4
		if int(row[0]) >= 55 and int(row[0]) < 64:
			agegroup = 5
		if int(row[0]) >= 65:
			agegroup = 6

		if basicctr == 0:
			ctrgroup = 0
		if basicctr > 0 and basicctr < 0.1:
			ctrgroup = 1
		if basicctr >= 0.1 and basicctr < 0.2:
			ctrgroup = 2
		if basicctr >= 0.2 and basicctr < 0.5:
			ctrgroup = 3
		if basicctr >= 0.5 and basicctr <= 1:
			ctrgroup = 4



		users.update({userno:[int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), agegroup, basicctr, ctrgroup]})
		userno+=1

	return users

def get_usersbyage(users):
	ages = [0, 0, 0, 0, 0, 0, 0]
	ages[0] = sum(1 for user in users.itervalues() if user[5] == 0)
	ages[1] = sum(1 for user in users.itervalues() if user[5] == 1)
	ages[2] = sum(1 for user in users.itervalues() if user[5] == 2)
	ages[3] = sum(1 for user in users.itervalues() if user[5] == 3)
	ages[4] = sum(1 for user in users.itervalues() if user[5] == 4)
	ages[5] = sum(1 for user in users.itervalues() if user[5] == 5)
	ages[6] = sum(1 for user in users.itervalues() if user[5] == 6)
	return ages

def get_usersbygender(users):
	genders =[0, 0]
	genders[0] = sum(1 for user in users.itervalues() if user[1] == 0)
	genders[1] = sum(1 for user in users.itervalues() if user[1] == 1)
	return genders

def get_usersbysignedin(users):
	signedins = [0, 0]
	signedins[0] = sum(1 for user in users.itervalues() if user[4] == 0)
	signedins[1] = sum(1 for user in users.itervalues() if user[4] == 1)
	return signedins

def get_usersbyctr(users):
	ctrs = [0, 0, 0, 0, 0]
	ctrs[0] = sum(1 for user in users.itervalues() if user[7] == 0)
	ctrs[1] = sum(1 for user in users.itervalues() if user[7] == 1)
	ctrs[2] = sum(1 for user in users.itervalues() if user[7] == 2)
	ctrs[3] = sum(1 for user in users.itervalues() if user[7] == 3)
	ctrs[4] = sum(1 for user in users.itervalues() if user[7] == 4)
	return ctrs


def get_impressionsbyage(users, agegroup):
	impressions =[]
	for user in users.itervalues():
	 if user[5] == agegroup:
	 	impressions.append(user[2]) 
	return impressions

def get_ctrbyage(users, agegroup):
	ctrs =[]
	for user in users.itervalues():
	 if user[5] == agegroup:
	 	ctrs.append(user[7]) 
	return ctrs

def get_ctrbygender(users, gender):
	ctrs =[]
	for user in users.itervalues():
	 if user[1] == gender:
	 	ctrs.append(user[7]) 
	return ctrs

def get_ctrbysignedin(users, signedin):
	ctrs =[]
	for user in users.itervalues():
	 if user[4] == signedin:
	 	ctrs.append(user[7]) 
	return ctrs

def get_ctrbygenderage(users, gender, agegroup):
	ctrs =[0]
	for user in users.itervalues():
	 if user[1] == gender and user[5] == agegroup and user[7] != 0:
	 	ctrs.append(user[7]) 
	return ctrs

def get_ctrbygendersignedin(users, gender, signedin):
	ctrs =[0]
	for user in users.itervalues():
	 if user[1] == gender and user[4] == signedin and user[7] != 0:
	 	ctrs.append(user[7]) 
	return ctrs

def get_ctrbysignedinage(users, signedin, agegroup):
	ctrs =[0]
	for user in users.itervalues():
	 if user[5] == agegroup and user[4] == signedin and user[7] != 0:
	 	ctrs.append(user[7]) 
	return ctrs


def create_images_1d(users):
	agegroups = get_usersbyage(users)
	ctrgroups = get_usersbyctr(users)
	signedgroups = get_usersbysignedin(users)
	gendergroups = get_usersbygender(users)

	plt.title("Age Groups")
	plt.bar([18, 24, 34, 44, 54, 64, 74], agegroups, [6, 10, 10, 10, 10, 10, 10])
	plt.savefig("agegroups.png")
	plt.clf()

	plt.title("Ctr Groups")
	plt.bar([0, 1, 2, 3, 4], ctrgroups, 1)
	plt.savefig("ctrgroups.png")
	plt.clf()

	plt.title("Signed Groups")
	plt.bar([0, 1], signedgroups)
	plt.savefig("signedgroups.png")
	plt.clf()

	plt.title("Gender Groups")
	plt.bar([0, 1], gendergroups)
	plt.savefig("gendergroups.png")
	plt.clf()


def create_images_2d(users):
	title = "a title"
	filename = "img.png"
	binsimp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 10, 11, 12, 13, 14, 15]
	binsctr = [0, 1, 2, 3, 4]
	ctrs =[]
	imps =[]
	label_ =[]

	for i in range(0,7):
		ctr_temp = get_ctrbyage(users, i)
		ctrs.append(ctr_temp)
		label_.append("Age" + str(i))
	plt.hist(ctrs, 5, label = label_, normed=1)
	plt.legend()
	plt.savefig("ctrbyagemulti_N.png")
	plt.clf()
	plt.hist(ctrs, 5, label = label_)
	plt.legend()
	plt.savefig("ctrbyagemulti.png")
	plt.clf()

	for i in range(0,7):
		imp_temp = get_impressionsbyage(users, i)
		imps.append(imp_temp)
		label_.append("Age" + str(i))
	plt.hist(imps, 10, label = label_, normed=1)
	plt.legend()
	plt.savefig("impbyagemulti_N.png")
	plt.clf()
	plt.hist(imps, 10, label = label_)
	plt.legend()
	plt.savefig("impbyagemulti.png")
	plt.clf()

	ctrs =[]
	label_ =[]


	for i in range(0,2):
		ctr_temp = get_ctrbygender(users, i)
		ctrs.append(ctr_temp)
		label_.append("Gender" + str(i))

	plt.hist(ctrs, 5, label=label_, normed=1)
	plt.legend()
	plt.savefig("ctrbygendermulti_N.png")
	plt.clf()
	plt.hist(ctrs, 5, label=label_)
	plt.legend()
	plt.savefig("ctrbygendermulti.png")
	plt.clf()


	ctrs =[]
	label_ =[]

	for i in range(0,2):
		ctr_temp = get_ctrbysignedin(users, i)
		ctrs.append(ctr_temp)
		label_.append("Signedin" + str(i))

	plt.hist(ctrs, 5, label=label_, normed=1)
	plt.legend()
	plt.savefig("ctrbysignedmulti_N.png")
	plt.clf()
	plt.hist(ctrs, 5, label=label_)
	plt.legend()
	plt.savefig("ctrbysignedmulti.png")
	plt.clf()

def create_images_3d(users):	
	for i in range(0,7):
		ctrs =[]
		label_=[]
		for j in range (0,2):
			ctrs_temp = get_ctrbygenderage(users,j,i)
			ctrs.append(ctrs_temp)
			label_.append("Gender" + str(j))
		filename_ctrgenderage = "CTR_Age"+str(i)+"byGender.png"
		plt.title("CTR for Age"+str(i)+"by Gender") 
		plt.hist(ctrs, 5, normed=1, label=label_)
		plt.legend()
		plt.savefig(filename_ctrgenderage)
		plt.clf()
		
	for i in range(0,7):
		ctrs =[]
		label_=[]
		for j in range (0,2):
			ctrs_temp = get_ctrbysignedinage(users,j,i)
			ctrs.append(ctrs_temp)
			label_.append("Signedin" + str(j))

		filename_ctrsignedinage = "CTR_Age"+str(i)+"bySignedin.png"
		plt.title("CTR for Age"+str(i)+"by Signedin") 
		plt.hist(ctrs,5, normed=1, label=label_)
		plt.legend()
		plt.savefig(filename_ctrsignedinage)
		plt.clf()

	for i in range (0,2):
		ctrs =[]
		label_=[]
		for j in range(0,2):
			ctrs_temp = get_ctrbygendersignedin(users,j,i)
			ctrs.append(ctrs_temp)
			label_.append("Gender" + str(j))

		filename_ctrgendersignedin = "CTR_Signedin"+str(i)+"byGender.png"
		plt.title("CTR for Signedin"+str(i)+"by Gender") 
		plt.hist(ctrs, 5, normed = 1, label=label_)
		plt.legend()
		plt.savefig(filename_ctrgendersignedin)
		plt.clf()




def create_images_3d_grouped(users):
	# binsctr = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
	
	#ctr group by gender/signedin and age
	for i in range(0,7):
		for j in range (0,2):
			title = "Ctr by Age"+ str(i)
			filename_ctrgenderage = "ctrgender"+str(j)+"age"+str(i)+".png"
			ctrs = get_ctrbygenderage(users,j,i)
			plt.title(title) 
			n, bins, patches = plt.hist(ctrs, normed=1)
			print filename_ctrgenderage
			print n, bins
			plt.savefig(filename_ctrgenderage)
			plt.clf()

		for j in range (0,2):
			title = "Ctr by Signedin" + str(j) + "Age"+str(i)
			filename_ctrsignedinage = "ctrsignedin"+str(j)+"age"+str(i)+".png"
			ctrs = get_ctrbysignedinage(users,j,i)
			plt.title(title) 
			n, bins, patches = plt.hist(ctrs, normed=1)
			print filename_ctrsignedinage
			print n, bins
			plt.savefig(filename_ctrsignedinage)
			plt.clf()
	#ctr group by gender and signedin
	for i in range (0,2):
		for j in range(0,2):
			title = "Ctr by Gender" + str(j) + "Signedin"+str(i)
			filename_ctrgendersignedin = "ctrgender"+str(j)+"signedin"+str(i)+".png"
			ctrs = get_ctrbygendersignedin(users,j,i)
			plt.title(title) 
			n, bins, patches = plt.hist(ctrs, normed = 1)
			print filename_ctrgendersignedin
			print n, bins
			plt.savefig(filename_ctrsignedinage)
			plt.clf()

def compute_quantiles(users):
	ages_ = []
	ctrs_ = []
	agequantiles = [0, 0, 0, 0, 0]
	ctrsquantiles = [0, 0, 0, 0, 0]

	for user in users.itervalues():
		ages_.append(user[0])
		ctrs_.append(user[6])

	ages = np.array(ages_)
	ctrs = np.array(ctrs_)

	agequantiles[0] = np.percentile(ages, 0)
	agequantiles[1] = np.percentile(ages, 25)
	agequantiles[2] = np.percentile(ages, 50)
	agequantiles[3] = np.percentile(ages, 75)
	agequantiles[4] = np.percentile(ages, 100)

	ctrsquantiles[0] = np.percentile(ctrs, 0)
	ctrsquantiles[1] = np.percentile(ctrs, 25)
	ctrsquantiles[2] = np.percentile(ctrs, 50)
	ctrsquantiles[3] = np.percentile(ctrs, 75)
	ctrsquantiles[4] = np.percentile(ctrs, 100)

	return agequantiles, ctrsquantiles
	# return ages
def compute_mean(users):
	ages_ = []
	ctrs_ = []
	agemean = 0
	ctrmean = 0

	for user in users.itervalues():
		ages_.append(user[0])
		ctrs_.append(user[6])

	ages = np.array(ages_)
	ctrs = np.array(ctrs_)

	agemean = np.mean(ages)
	ctrmean = np.mean(ctrs)

	return agemean, ctrmean
def compute_variance(users):
	ages_ = []
	ctrs_ = []
	agevar = 0
	ctrvar = 0

	for user in users.itervalues():
		ages_.append(user[0])
		ctrs_.append(user[6])

	ages = np.array(ages_)
	ctrs = np.array(ctrs_)

	agevar = np.var(ages)
	ctrmean = np.var(ctrs)

	return agevar, ctrvar



data = get_csv()
users = parse_csv(data)
# create_images_1d(users)
# print "usersbyage"
# print get_usersbyage(users)
# print "usersbygender"
# print get_usersbygender(users)
# print "usersbysignedstatus"
# print get_usersbysignedin(users)
# print "usersbyctr"
# print get_usersbyctr(users)
# print "age & ctr compute_quantiles"
# print compute_quantiles(users)
# print "age & ctr compute_mean"
# print compute_mean(users)
# print "age & ctr compute_variance"
# print compute_variance(users)
# print get_usersbyctr(users)
# create_images_1d(users)
# create_images_2d(users)
# create_images_3d(users)
# create_images_3d_grouped(users)

