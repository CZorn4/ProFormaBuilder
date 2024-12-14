def get_xbrl_tags():
    income_statement_tags = {
        'revenue': [
            'us-gaap:Revenues',
            'Revenues',
            'SalesRevenueNet',
            'RevenuesNetOfInterestExpense'
        ],
        'cost_of_goods_sold': [
            'us-gaap:CostOfRevenue',
            'CostOfGoodsAndServicesSold', 
            'CostOfRevenue',
            'CostOfGoodsSold'
        ],
        'interest_paid': [
            'us-gaap:InterestExpense',
            'InterestExpense',
            'InterestPaidNet'
        ],
        'interest_earned': [
            'us-gaap:InvestmentIncomeInterest',
            'InterestAndDividendIncome',
            'InvestmentIncomeInterest',
            'InterestIncome'
        ],
        'depreciation': [
            'DepreciationAmortizationAndImpairment',
            'DepreciationDepletionAndAmortization',
            'DepreciationAmortizationAndAccretionNet',
            'DepreciationAndAmortization',
            'tsla:DepreciationAmortizationAndImpairment'
        ],
        'profit_before_tax': [
            'us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
            'ProfitLossBeforetax',
            'IncomeLossBeforeIncomeTaxes',
            'ProfitBeforeTax'
        ],
        'income_tax': [
            'us-gaap:IncomeTaxExpenseBenefit',
            'IncomeTaxExpenseBenefit',
            'IncomeTaxesPaid'
        ],
        'profit_after_tax': [
            'us-gaap:NetIncomeLoss',
            'NetIncomeLoss',
            'ProfitLoss'
        ],
        'dividends': [
            'CommonStockDividendsPerShareDeclared',
            'PaymentsOfDividends'
        ],
        'retained_earnings': [
            'RetainedEarningsAccumulatedDeficit',
            'RetainedEarnings'
        ]
    }
    
    balance_sheet_tags = {
        'cash_and_securities': [
            'CashAndCashEquivalentsAtCarryingValue',
            'CashCashEquivalentsAndMarketableSecurities',
            'MarketableSecurities'
        ],
        'current_assets': [
            'AssetsCurrent'
        ],
        'ppe_gross': [
            'PropertyPlantAndEquipmentGross',
            'PropertyPlantAndEquipment'
        ],
        'accumulated_depreciation': [
            'AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment'
        ],
        'ppe_net': [
            'PropertyPlantAndEquipmentNet'
        ],
        'current_liabilities': [
            'LiabilitiesCurrent'
        ],
        'long_term_liabilities': [
            'LiabilitiesNoncurrent',
            'NoncurrentLiabilities'
        ],
        'outstanding_stock': [
            'CommonStockSharesOutstanding',
            'CommonStockSharesIssued'
        ],
        'retained_earnings': [
            'RetainedEarningsAccumulatedDeficit',
            'RetainedEarnings'
        ],
        'StockHolders Equity': [
            'StockholdersEquity'
        ]
    }
    
    return {
        'income_statement': income_statement_tags,
        'balance_sheet': balance_sheet_tags
    }