from random import uniform 
#Homework 1
class Portfolio(object):
    def __init__(self, cash = 0.0, stock={}, mfund={}, history=[]):
        self.cash = float(cash)
        self.stock = stock
        self.mfund = mfund
        #self.stock.dictionary= {}
        #self.mutual.dictionary= {}
        self.history = history


    def addCash(self, cash):
        self.cash += float(cash)
        self.history.append("You have added $%.2f"  %float(cash))
        return(self.cash)

    def withdrawCash(self, cash):
        if cash < self.cash:
			self.cash -= float(cash)
			self.history.append("You have withdrawn $%.2f"  %float(cash))
        else:
        	self.history.append("Attempted to withdraw too much.")
        	raise Exception, "Stopped because you do not have enough money in account."
        return(self.cash)

    def __str__(self):
        money = "You have %d in cash, %s stocks, and %s mutual funds " %(self.cash, self.stock, self.mfund)
        return money

    def buyStock(self, s_quantity, stock):
    	if (s_quantity * stock.price) > self.cash:
    		raise Exception, "Not enough money"
    	else:
    		self.cash -= (s_quantity * stock.price)
    		if stock.s_symbol not in self.stock.keys():
    			self.stock[stock.s_symbol] = s_quantity
    		else:
    			self.stock[stock.s_symbol] += s_quantity
    		self.history.append("You have bought %s shares of %s at a price of %d. Your cash on hand was decreased by %.f" %(s_quantity, stock.s_symbol,stock.price, (s_quantity * stock.price)) )
    		return self.stock

    def sellStock(self, s_symbol, s_quantity):
    	toSell = self.stock[s_symbol]
    	if s_quantity < toSell:
    		self.stock[s_symbol] -= float(s_quantity)
    		print "You currently have %s and %s" %(self.cash, self.stock)
    	elif s_quantity == toSell:
    		#stock.remove(self.stock[s_symbol])
    		del self.stock[s_symbol]
    		print "You currently have %s and %s" %(self.cash, self.stock)
    	else:
    		raise Exception, "Stopped because you do not that many stock/quantity to sell"
    	newcash = uniform((float(.5) * Stocks[s_symbol]),(float(1.5) * Stocks[s_symbol]))
    	newcash = round(newcash, 2)
    	self.cash += newcash
    	self.history.append("You added %.2f by selling %s shares of %s"%(float(newcash),s_quantity,s_symbol))

    def buyMutualFund(self, fracShares, mfund):
    	self.cash -= round(float(fracShares),2)
    	if mfund.f_symbol in self.mfund.keys():
    		self.mfund[mfund.f_symbol]+= round(fracShares,2)
    	else:
    		self.mfund[mfund.f_symbol] = round(fracShares,2)
    	self.history.append("You have bought %.2f of %s. " %(round(fracShares,2), mfund.f_symbol))
    	return self.mfund

    def sellMutualFund(self, f_symbol, fracShares):
    	toSell = round(float(self.mfund[f_symbol]),2)
    	if fracShares < toSell:
    		self.mfund[f_symbol] -= float(fracShares)
    		print "You currently have %s and %s" %(self.cash, self.mfund)
    	elif fracShares == toSell:
    		#mfund.remove(self.mfund[f_symbol])
    		del self.mfund[f_symbol]
    		print "You currently have %s and %s" %(self.cash, self.mfund)
    	else:
    		raise Exception, "Stopped because you do not that many Mutual Funds to sell"
    	newcash = uniform(.9,1.2) * fracShares
    	newcash = round(newcash,2)
    	self.cash += round(float(newcash),2)
    	self.history.append("You added %.2f by selling %s shares of %s"%(newcash,fracShares,f_symbol))

    def history(self):
        self.histroy = history
        print self.history 

    #buy mutual fund function 
    	#(self, shares, MutualFund)

class Stock(object):
	def __init__(self, price, s_symbol):
		self.price = price
		self.s_symbol = s_symbol
		Stocks[s_symbol]=price
	def __str__(self):
		return "%s at %s" %(self.s_symbol, self.price)
Stocks = {}

class MutualFund(object):
	def __init__(self, f_symbol):
		self.f_symbol = f_symbol
	def __str__(self):
		return f_symbol	
 
##########################
###   To Check Work    ###
##########################

portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50)
portfolio.history




############################
###    Things to do      ###
############################

# portfolio.history works but portfolio.history() does not



