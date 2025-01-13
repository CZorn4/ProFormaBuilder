def get_xbrl_tags():
    return {
        'revenue': [
            'Revenues',
            'RevenueFromContractWithCustomerExcludingAssessedTax',
        ],

        'cost_of_revenue': [
            'CostOfRevenue',
            'CostOfGoodsAndServicesSold',
            'CostOfGoodsSold',
        ],
        'gross_profit': [
            'GrossProfit',
        ],
        'research_and_development_expense': [
            'ResearchAndDevelopmentExpense',
        ],
        'selling_general_and_administrative_expense': [
            'SellingGeneralAndAdministrativeExpense',
        ],
        'selling_and_marketing_expense': [
            'SellingAndMarketingExpense',
        ],
        'total_operating_expenses': [
            'OperatingExpenses',
            'OperatingCostsAndExpenses',
        ],
        'total_operating_income': [
            'OperatingIncomeLoss',
            'IncomeFromOperations',
            'OperatingIncome',
        ],
        'interest_expense': [
            'InterestExpenseNonoperating',
            'InterestExpense',
        ],
        'interest_income': [
            'InvestmentIncomeInterest'
        ],
        'interest_and_debt_expense': [
            'InterestAndDebtExpense',
        ],
        'investment_income': [
            'InvestmentIncomeNet',
        ],
        'other_nonoperating_income': [
            'OtherNonoperatingIncomeExpense',
        ],
        'total_nonoperating_income': [
            'NonoperatingIncomeExpense',
            'TotalNonoperatingIncome',
            'OtherIncomeLossNet',
        ],
        'income_before_tax': [
            'IncomeLossBeforeIncomeTaxes',
            'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
            'IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments',
            'ProfitBeforeTax',
            'ProfitLossBeforetax',
            'EarningsBeforeTax',
            'IncomeBeforeTaxes'
        ],
        'current_income_tax': [
            'CurrentIncomeTaxExpenseBenefit',
            'CurrentTaxExpense',
            'IncomeTaxesCurrent',
        ],
        'deferred_income_tax_expense_benefit': [
            'DeferredIncomeTaxExpenseBenefit',
            'DeferredTaxExpense',
            'IncomeTaxesDeferred',
        ],
        'income_tax_expense': [
            'IncomeTaxExpenseBenefit',
            'IncomeTaxesPaid',
        ],
        'provision_for_income_taxes': [
            'ProvisionForIncomeTaxes',
        ],
        'profit_loss': [
            'ProfitLoss',
        ],
        'continuing_operations_income': [
            'IncomeLossFromContinuingOperations',
        ],
        'discontinued_operations_income': [
            'IncomeLossFromDiscontinuedOperationsNetOfTaxAttributableToReportingEntity',
        ],
        'income_from_noncontrolling_interests': [
            'NetIncomeLossAttributableToNoncontrollingInterest',
        ],
        'net_income': [
            'NetIncomeLoss',
            'NetIncome',
            'NetEarnings',
            'NetIncomeLossAvailableToCommon',
        ],
        'deferred_income_taxes': [
            'DeferredIncomeTaxExpenseBenefit',
            'DeferredTaxExpense',
            'IncomeTaxesDeferred',
        ],
        'gain_loss_on_investments': [
            'GainLossOnInvestments',
            'InvestmentGainsLosses',
            'RealizedGainLossOnInvestments',
        ],
        'cash_from_operating_activities': [
            'NetCashProvidedByUsedInOperatingActivities',
            'CashFlowFromOperations',
            'OperatingCashFlow',
        ],
        'increase_decrease_accounts_receivable': [
            'IncreaseDecreaseInAccountsReceivable'
        ],
        'increase_decrease_inventories': [
            'IncreaseDecreaseInInventories',
        ],
        'increase_decrease_prepaid_expenses_and_other_assets': [
            'IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets',
        ],
        'increase_decrease_accounts_payable': [
            'IncreaseDecreaseInAccountsPayable',
        ],
        'increase_decrease_accrued_and_other_current_liabilities': [
            'IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities',
        ],
        'increase_decrease_other_non_current_liabilities': [
            'IncreaseDecreaseInOtherNoncurrentLiabilities'
        ],
        'repurchases_of_common_stock': [
            'PaymentsForRepurchaseOfCommonStock',
            'StockRepurchased',
            'CommonStockRepurchased',
        ],
        'repayments_of_debt': [
            'RepaymentsOfDebt',
            'DebtRepayment',
            'RepaymentOfDebt',
            'RepaymentsOfLongTermDebt',
        ],
        'proceeds_from_repayments_of_commercial_paper': [
            'ProceedsFromRepaymentsOfCommercialPaper'
        ],
        'Proceeds_From_Payments_For_Other_Financing_Activities': [
            'ProceedsFromPaymentsForOtherFinancingActivities'
        ],
        'payment_of_dividends': [
            'PaymentsOfDividends',
            'DividendsPaid',
            'CommonStockDividendsPaid',
        ],
        'issuance_of_debt': [
            'DebtIssuance',
            'ProceedsFromDebt',
            'ProceedsFromIssuanceOfLongTermDebt'
        ],
        'issuance_of_debt_net_of_costs': [
            'ProceedsFromDebtNetOfIssuanceCosts',
        ],
        'cash_from_financing_activities': [
            'NetCashProvidedByUsedInFinancingActivities',
            'FinancingCashFlow',
            'CashFlowFromFinancing',
        ],
        'cash_and_restricted_cash': [
            'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents',
            'CashAndRestrictedCash',
            'RestrictedCash',
        ],
        'cash': [
            'Cash',
        ],
        'cash_and_cash_equivalents': [
            'CashAndCashEquivalentsAtCarryingValue',
            'CashAndEquivalents',
        ],
        'marketable_securities_current': [
            'MarketableSecuritiesCurrent',
            'ShortTermInvestments',
            'TradingSecurities',
        ],
        'vendor_non_trade_receivables_current': [
            'NontradeReceivablesCurrent'
        ],
        'marketable_securities_noncurrent': [
            'MarketableSecuritiesNoncurrent',
        ],
        'cash_and_marketable_securities': [
            'CashCashEquivalentsAndMarketableSecurities',
        ],
        'accounts_receivable': [
            'AccountsReceivableNetCurrent',
            'ReceivablesNet',
            'TradeAccountsReceivable',
        ],
        'inventories': [
            'InventoryNet',
            'InventoriesNet',
            'MerchandiseInventories',
        ],
        'prepaid_expenses': [
            'PrepaidExpense',
            'PrepaidExpenses',
        ],
        'other_assets_current': [
            'OtherAssetsCurrent',
            'OtherCurrentAssets',
            'MiscellaneousCurrentAssets',
        ],
        'prepaid_expense_and_other_assets_current': [
            'PrepaidExpenseAndOtherAssetsCurrent',
        ],
        'total_current_assets': [
            'AssetsCurrent',
            'CurrentAssets',
            'TotalCurrentAssets',
        ],
        'property_plant_and_equipment_gross': [
            'PropertyPlantAndEquipmentGross',
            'GrossPropertyPlantAndEquipment',
            'PropertyAndEquipmentGross',
        ],
        'property_plant_and_equipment_accumulated_depreciation': [
            'PropertyPlantAndEquipmentAccumulatedDepreciation',
        ],
        'accumulated_depreciation_depletion_amortization': [
            'AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment',
        ],
        'accumulated_depreciation_amortization': [
            'AccumulatedDepreciationAndAmortization',
        ],
        'accumulated_depreciation': [
            'AccumulatedDepreciation',
        ],
        'share_based_compensation_expense': [
            'ShareBasedCompensation',
        ],
        'property_plant_and_equipment_net': [
            'PropertyPlantAndEquipmentNet',
            'NetPropertyPlantAndEquipment',
        ],
        'intangible_assets': [
            'IntangibleAssets',
        ],
        'intangible_assets_excluding_goodwill': [
            'IntangibleAssetsNetExcludingGoodwill',
        ],
        'intangible_assets_and_goodwill': [
            'GoodwillAndIntangibleAssets',
        ],
        'goodwill': [
            'Goodwill',
            'GoodwillGross',
        ],
        'income_tax_assets': [
            'DeferredIncomeTaxAssetsNet',
            'DeferredTaxAssets',
            'IncomeTaxesReceivable',
        ],
        'other_non_current_assets': [
            'OtherAssetsNoncurrent',
            'OtherLongTermAssets',
            'MiscellaneousNoncurrentAssets',
        ],
        'total_non_current_assets': [
            'AssetsNoncurrent'
        ],
        'total_assets': [
            'Assets',
            'AssetsTotal',
            'TotalAssets',
        ],
        'accounts_payable': [
            'AccountsPayableCurrent',
            'AccountsPayableTrade',
            'TradeAccountsPayable',
        ],
        'current_deferred_revenue': [
            'ContractWithCustomerLiabilityCurrent'
        ],
        'commercial_paper': [
            'CommercialPaper'
        ],
        'other_current_liabilities': [
            'OtherLiabilitiesCurrent',
            'OtherCurrentLiabilities',
            'MiscellaneousCurrentLiabilities',
        ],
        'total_current_liabilities': [
            'LiabilitiesCurrent',
            'CurrentLiabilities',
            'TotalCurrentLiabilities',
        ],
        'long_term_debt': [
            'LongTermDebt',
        ],
        'long_term_debt_current': [
            'LongTermDebtCurrent',
            'DebtCurrent',
        ],
        'long_term_debt_non_current': [
            'LongTermDebtNoncurrent',
            'DebtNonCurrent',
        ],
        'long_term_debt_capital_lease_obligations': [
            'LongTermDebtAndCapitalLeaseObligations',
        ],
        'other_non_current_liabilities': [
            'OtherLiabilitiesNoncurrent',
            'OtherLongTermLiabilities',
            'MiscellaneousNoncurrentLiabilities',
        ],
        'total_non_current_liabilities': [
            'LiabilitiesNoncurrent'
        ],
        'total_liabilities': [
            'Liabilities',
            'TotalLiabilities',
            'LiabilitiesTotal',
        ],
        'preferred_stock': [
            'PreferredStockValueOutstanding',
            'PreferredStock',
            'PreferredStockValue',
        ],
        'common_stock_value': [
            'CommonStockValue',
        ],
        'common_stock_shares_outstanding': [
            'CommonStockSharesOutstanding',
        ],
        'common_stock_and_paid_in_capital': [
            'CommonStockAndAdditionalPaidInCapital',
        ],
        'accumulated_other_comprehensive_income': [
            'AccumulatedOtherComprehensiveIncome',
        ],
        'accumulated_other_comprehensive_income_net_of_tax': [
            'AccumulatedOtherComprehensiveIncomeLossNetOfTax',
        ],
        'retained_earnings': [
            'RetainedEarnings',
            'RetainedEarningsAccumulatedDeficit',
            'RetainedEarningsAccumulatedLosses',
        ],
        'stockholders_equity': [
            'StockholdersEquity',
            'ShareholdersEquity',
            'TotalStockholdersEquity',
        ],
        'total_liabilities_and_SE': [
            'LiabilitiesAndStockholdersEquity',
            'TotalLiabilitiesAndEquity',
            'LiabilitiesAndShareholdersEquity',
        ],
        'common_stock_outstanding': [
            'CommonStockSharesOutstanding',
            'EntityCommonStockSharesOutstanding',
            'SharesOutstanding',
            'CommonSharesOutstanding',
        ],
        'additional_paid_in_capital': [
            'AdditionalPaidInCapital',
            'PaidInCapital',
            'AdditionalCapital',
        ],
        'treasury_stock': [
            'TreasuryStock',
            'TreasuryStockValue',
            'CommonTreasuryStock',
        ],
        'other_comprehensive_income': [
            'OtherComprehensiveIncomeLossNetOfTax',
            'OtherComprehensiveIncomeLoss',
        ],
        'comprehensive_income_with_noncontrolling': [
            'ComprehensiveIncomeNetOfTaxIncludingPortionAttributableToNoncontrollingInterest',
        ],
        'noncontrolling_comprehensive_income': [
            'ComprehensiveIncomeNetOfTaxAttributableToNoncontrollingInterest',
        ],
        'total_comprehensive_income': [
            'ComprehensiveIncomeNetOfTax',
            'TotalComprehensiveIncome',
            'ComprehensiveIncomeLoss',
        ],
        'basic_shares': [
            'WeightedAverageNumberOfSharesOutstandingBasic',
            'BasicWeightedAverageShares',
            'WeightedAverageShares',
        ],
        'diluted_shares': [
            'WeightedAverageNumberOfDilutedSharesOutstanding',
            'DilutedWeightedAverageShares',
            'WeightedAverageDilutedShares',
        ],
        'depreciation': [
            'Depreciation',
            'DepreciationExpense',
        ],
        'depreciation_and_amortization': [
            'DepreciationAndAmortization',
        ],
        'depreciation_depletion_and_amortization': [
            'DepreciationDepletionAndAmortization',
        ],
        'proceeds_from_maturities_of_marketable_securities': [
            'ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities'
        ],
        'proceeds_from_sales_of_marketable_securities': [
            'ProceedsFromSaleOfAvailableForSaleSecuritiesDebt'
        ],
        'purchases_of_marketable_securities': [
            'PaymentsToAcquireAvailableForSaleSecuritiesDebt',
        ],
        'payments_to_acquire_productive_assets': [
            'PaymentsToAcquireProductiveAssets',
        ],
        'payments_to_acquire_property_plant_equipment': [
            'PaymentsToAcquirePropertyPlantAndEquipment',
        ],
        'other_investing_activities': [
            'PaymentsForProceedsFromOtherInvestingActivities',
        ],
        'aquisitions_net_of_cash_aquired': [
            'PaymentsToAcquireBusinessesNetOfCashAcquired',
        ],
        'cash_from_investing_activities': [
            'NetCashProvidedByUsedInInvestingActivities',
            'InvestingCashFlow',
            'CashFlowFromInvesting',
        ],
        'computed_federal_tax': [
            'IncomeTaxReconciliationIncomeTaxExpenseBenefitAtFederalStatutoryIncomeTaxRate',
        ],
        'federal_statutory_rate': [
            'EffectiveIncomeTaxRateReconciliationAtFederalStatutoryIncomeTaxRate',
        ],
        'effective_tax_rate': [
            'EffectiveIncomeTaxRateContinuingOperations',
            'EffectiveIncomeTaxRate',
            'EffectiveTaxRate',
        ],
        'deferred_tax_assets_gross': [
            'DeferredTaxAssetsGross',
            'DeferredIncomeTaxAssetsGross',
        ],
        'deferred_tax_assets_valuation_allowance': [
            'DeferredTaxAssetsValuationAllowance',
            'DeferredTaxAssetValuationAllowance',
        ],
        'deferred_tax_assets_net': [
            'DeferredTaxAssetsNet',
        ],
        'deferred_tax_liabilities_gross': [
            'DeferredIncomeTaxLiabilities',
            'DeferredTaxLiabilities',
            'GrossDeferredTaxLiabilities',
        ],
        'deferred_tax_assets_liabilities_net': [
            'DeferredTaxAssetsLiabilitiesNet',
        ]
    }