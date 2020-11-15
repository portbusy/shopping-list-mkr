import argparse
from operator import itemgetter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--new',
                        help='If true the old shopping list will be deleted',
                        default=False,
                        required=False)
    args = parser.parse_args()
    skipOldData = args.new
    shoppingList = []
    try:
        if(not skipOldData):
            with open('shoppingList.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    splittedLine = line.split(': ')
                    itemName = splittedLine[0]
                    itemAmount = int(splittedLine[1].strip('g\n'))
                    tmpObj = {'name': itemName, 'amount': itemAmount}
                    shoppingList.append(tmpObj)
                file.close()
    except:
        print("No file found, passing")
        pass

    endLoop = False
    while not endLoop:
        itemAndAmount = input("Enter the name of the item and the amount, separated by comma (name, amount): ")
        if(itemAndAmount == 'end'):
            endLoop = True
            break
        else:
            splittedItem = itemAndAmount.split(", ")
            if (len(splittedItem) < 2):
                print("Be sure to enter the name of the item and the amount separated by space")
            else:
                itemName = splittedItem[0]
                itemAmount = splittedItem[1]
                found = False
                for x in shoppingList:
                    if x['name'] == itemName:
                        print(f'Found item with name {x["name"]}, amount {x["amount"]}')
                        found = True
                        x['amount'] = int(x['amount']) + int(itemAmount)
                if not found:
                    tmpObj = {'name': itemName, 'amount': itemAmount}
                    shoppingList.append(tmpObj)
    shoppingList = sorted(shoppingList, key=itemgetter('name'))
    print(shoppingList)
    with open('shoppingList.txt', 'w') as file:
        for item in shoppingList:
            file.writelines(f'{item["name"]}: {item["amount"]}g\n')


if __name__ == '__main__':
    main()