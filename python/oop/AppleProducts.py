class AppleProduct:
  def __init__(self, name, model, base_price):
    self.name = name
    self.model = model
    self.base_price = base_price
  def companyInfo(self):
    st = ("Company Name: Apple\nFouder: Steve Jobs, Steve Wozniak, Ronald Wayne\nCurrent CEO: Tim Cook\nAddress: Apple Inc, 2511 Laguna Blvd, Elk Grove, CA 95758, United States")    
    return st
  def feature(self):
    st = (f"Name: {self.name}\nProduct Model: {self.model}\nHardware Quality: Excellent Hardwares\nGuarantee/ Warranty: Apple Care")
    return st
  def __str__(self):
    print('This is apple product.')
  def calculatePrice(self):
    print('Total Price:', self.base_price)
# Write your codes here.
# Do not change the following lines of code.

m1 = MacBookPro2020('MacBook', 'MacBookPro2020', 8, 'M1', 10)
print(m1)
print('====================================')
m1.calculatePrice()
print('###################################')
iphone = iPhone12('iPhone', 'iPhone 12', 8, 'A14', 5)
print(iphone)
print('====================================')
iphone.calculatePrice()  
print('###################################')
print('Total Price of these two products: ',end='')
print('%.2f Dollars'%(m1 + iphone))