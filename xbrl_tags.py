def get_xbrl_tags():
    income_statement_tags = {
        'revenue': [
            'us-gaap:Revenues',
            'Revenues',
            'SalesRevenueNet',
            'RevenuesNetOfInterestExpense'
            'RevenueFromContractWithCustomerExcludingAssessedTax'
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
        'profit_before_tax': [
            'us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
            'ProfitLossBeforetax',
            'IncomeLossBeforeIncomeTaxes',
            'ProfitBeforeTax',
            'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest'
        ],
        'income_tax_expense': [
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
            'RetainedEarnings',
            'us-gaap:RetainedEarningsAccumulatedDeficit'
        ]
    }
    
    balance_sheet_tags = {
        'cash_and_securities': [
            'CashAndCashEquivalentsAtCarryingValue',
            'CashCashEquivalentsAndMarketableSecurities',
            'MarketableSecurities'
        ],
        'total_current_assets': [
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
        'total_assets': [
            'Assets',
            'us-gaap:Assets'
        ],
        'current_liabilities': [
            'LiabilitiesCurrent'
        ],
        'long_term_liabilities': [
            'LiabilitiesNoncurrent',
            'NoncurrentLiabilities'
        ],
        'total_liabilities': [
            'Liabilities',
            'us-gaap:Liabilities'
        ],
        'outstanding_stock': [
            'CommonStockSharesOutstanding',
            'CommonStockSharesIssued'
        ],
        'retained_earnings': [
            'RetainedEarningsAccumulatedDeficit',
            'RetainedEarnings'
        ],
        'StockHolders_Equity': [
            'StockholdersEquity',
            'us-gaap:StockholdersEquity'
        ],
        'total_liabilities_and_SE': [
            'LiabilitiesAndStockholdersEquity',
            'us-gaap:LiabilitiesAndStockholdersEquity'
        ]

    }
    
    return {
        'income_statement': income_statement_tags,
        'balance_sheet': balance_sheet_tags
    }