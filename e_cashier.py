

products_prices = {
  "Lenovo ThinkPad X140e": 414,
  "Lenovo ThinkPad T440": 440,
  "Lenovo ThinkPad E540": 499,
  "Lenovo ThinkPad T440p": 589,
  "Lenovo ThinkPad E440": 599,
  "Dell XPS 13-9343": 799,
  "ASUS Zenbook UX303LA": 812,
  "Lenovo Thinkpad T540p": 825,
  "ASUS Zenbook UX303LA": 849,
  "Dell XPS 13 4289": 899,
  "Dell XPS 13 9343": 899,
  "Apple Macbook Air 13": 938,
  "Lenovo ThinkPad T450s": 1060,
  "Lenovo ThinkPad T550": 1080,
  "Lenovo ThinkPad T540p": 1109,
  "Dell Latitude 15 E5550": 1170,
  "Dell XPS 15-9530": 1189,
  "ASUS Zenbook UX303LN": 1239,
  "Lenovo ThinkPad T440p": 1263,
  "Dell Latitude 14 E7450": 1276,
  "Dell XPS 13 9343": 1295,
  "Apple Macbook Pro Retina 13": 1299,
  "ASUS Zenbook UX301LA": 1299,
  "Dell XPS 15-4737": 1329,
  "Dell XPS 15-8949": 1899,
  "Apple Macbook Pro Retina 15": 2349
}

def products_output(products_list, cols):
    lines = ("\t\t".join(products_list[i:i+cols]) for i in xrange(0,len(products_list),cols))
    return "\n".join(lines)
#print products_output(products_prices.keys(),3)

def e_cashier(products_prices, user_product):
    for i in products_prices:
        if i == user_product:
            return "Price for %s is %i$"%(i, products_prices[i])
#print e_cashier(products_prices, user_product)

def main():

    print """Welcome to <---e-Cashier--->
Here is the list of our products:\n"""

    print products_output(products_prices.keys(),3)

    user_product = raw_input("\nPlease choose and input product's name for information about it's price: ")

    print e_cashier(products_prices, user_product),"\n"


if __name__ == "__main__":
    main()
