import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0
        self.withdraws = 0.0

    def __str__(self):
        title = self.name
        titleLength = len(title)
        titleBorder = int((30 - titleLength)/2) * '*'

        title = titleBorder + title + titleBorder

        statement = title + '\n'

        for item in self.ledger:
            description = item['description'] + (23 * ' ')
            formatedAmount = "{:.2f}".format(item['amount'])
            amount = (7 * ' ') + formatedAmount

            statement = statement + description[:23] + amount[len(amount)-7:] + '\n'

        formatedBalance = "{:.2f}".format(self.balance)
        total = 'Total: ' + formatedBalance

        statement = statement + total

        return statement

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance = self.balance + amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.withdraws = self.withdraws + amount
            self.ledger.append({"amount": amount * -1, "description": description})
            self.balance = self.balance - amount

            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f'Transfer from {self.name}')

            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def get_balance(self):
        return self.balance

    def get_withdraws(self):
        return self.withdraws

    def get_name(self):
        return self.name


def create_spend_chart(categories):
    title = 'Percentage spent by category\n'
    categoriesAmount = len(categories)
    finalDivisor = '    -'
    categoriesSpent = []
    sumSpentAllCategories = 0.0

    chart = title

    axisY = [
        '100| ', 
        ' 90| ',
        ' 80| ',
        ' 70| ',
        ' 60| ',
        ' 50| ',
        ' 40| ',
        ' 30| ',
        ' 20| ',
        ' 10| ',
        '  0| ',
        ]

    for categorie in categories:
        sumSpentAllCategories = sumSpentAllCategories + categorie.get_withdraws()
        categoriesSpent.append({ 'categorie':  categorie.get_name(), 'spent': categorie.get_withdraws()})

    for item in categoriesSpent:
        percentageSpent = math.ceil(item['spent']/sumSpentAllCategories*10)
        item['percentageSpent'] = percentageSpent

    for position in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
        line = axisY[10-position]

        for item in categoriesSpent:
            if item['percentageSpent'] > position:
                line = line + 'o  '
            else:
                line = line + '   '

        chart = chart + line + '\n'
            
    for i in range(categoriesAmount):
        finalDivisor = finalDivisor + '---'
        
    chart = chart + finalDivisor + '\n'

    bigestCategoryName = ''
    
    for item in categoriesSpent:
        if len(item['categorie']) > len(bigestCategoryName):
            bigestCategoryName = item['categorie']

    for i in range(len(bigestCategoryName)):
        line = '     '

        for item in categoriesSpent:
            if i < len(item['categorie']):
                line = line + item['categorie'][i] + '  '
            else:
                line = line + '   '
        
        chart = chart + line

        if i < len(bigestCategoryName) - 1:
            chart = chart + '\n'

    return chart
