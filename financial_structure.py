def get_financial_structure():
    """
    Defines the structure of financial statements including the order and grouping
    of line items. Each item references an XBRL tag key that maps to possible tags
    in the xbrl_tags module.
    """
    return {
        'income_statement': {
            'groups': [
                {
                    'name': 'Revenue and Gross Profit',
                    'items': [
                        'revenue',
                        'cost_of_revenue',
                        'gross_profit'
                    ]
                },
                {
                    'name': 'Operating Expenses',
                    'items': [
                        'research_and_development_expense',
                        'selling_general_and_administrative_expense',
                        'total_operating_expenses'
                    ]
                },
                {
                    'name': 'Operating Income',
                    'items': [
                        'total_operating_income'
                    ]
                },
                {
                    'name': 'Non-Operating Items',
                    'items': [
                        'interest_expense',
                        'interest_income',
                        'other_nonoperating_income',
                        'total_nonoperating_income'
                    ]
                },
                {
                    'name': 'Income Before Tax',
                    'items': [
                        'income_before_tax'
                    ]
                },
                {
                    'name': 'Income Taxes',
                    'items': [
                        'current_income_tax',
                        'deferred_income_tax_expense_benefit',
                        'income_tax_expense',
                        'provision_for_income_taxes'
                    ]
                },
                {
                    'name': 'Net Income',
                    'items': [
                        'profit_loss',
                        'income_from_noncontrolling_interests',
                        'net_income'
                    ]
                },
                {
                    'name': 'Other Income Items',
                    'items': [
                        'discontinued_operations_income'
                    ]
                }
            ]
        },
        'balance_sheet': {
            'groups': [
                {
                    'name': 'Current Assets',
                    'items': [
                        'cash_and_cash_equivalents',
                        'marketable_securities_current',
                        'vendor_non_trade_receivables_current',
                        'accounts_receivable',
                        'inventories',
                        'prepaid_expenses',
                        'other_assets_current',
                        'prepaid_expense_and_other_assets_current',
                        'total_current_assets'
                    ]
                },
                {
                    'name': 'Non-Current Assets',
                    'items': [
                        'marketable_securities_noncurrent',
                        'property_plant_and_equipment_gross',
                        'accumulated_depreciation',
                        'accumulated_depreciation_depletion_amortization',
                        'property_plant_and_equipment_net',
                        'intangible_assets',
                        'intangible_assets_excluding_goodwill',
                        'goodwill',
                        'income_tax_assets',
                        'other_non_current_assets',
                        'total_non_current_assets',
                    ]
                },
                {
                    'name': 'Total Assets',
                    'items': [
                        'total_assets',
                    ]
                },
                {
                    'name': 'Current Liabilities',
                    'items': [
                        'accounts_payable',
                        'long_term_debt_current',
                        'current_deferred_revenue',
                        'commercial_paper',
                        'other_current_liabilities',
                        'total_current_liabilities'
                    ]
                },
                {
                    'name': 'Non-Current Liabilities',
                    'items': [
                        'long_term_debt_non_current',
                        'other_non_current_liabilities',
                        'total_non_current_liabilities',
                    ]
                },
                {
                    'name': 'Total Liabilities',
                    'items': [
                        'total_liabilities',
                    ]
                },
                {
                    'name': "Stockholders' Equity",
                    'items': [
                        'preferred_stock',
                        'common_stock_value',
                        'common_stock_shares_outstanding',
                        'additional_paid_in_capital',
                        'common_stock_and_paid_in_capital',
                        'accumulated_other_comprehensive_income',
                        'accumulated_other_comprehensive_income_net_of_tax',
                        'retained_earnings',
                        'stockholders_equity',
                        'total_liabilities_and_SE'
                    ]
                }
            ]
        },
        'cash_flow': {
            'groups': [
                {
                    'name': 'Operating Activities',
                    'items': [
                        'profit_loss',
                        'net_income',
                        'depreciation',
                        'deprecition_and_amortization',
                        'depreciation_depletion_and_amortization',
                        'share_based_compensation_expense',
                        'deferred_income_taxes',
                        'gain_loss_on_investments',
                        'cash_from_operating_activities',
                    ],
                    'name': 'changes in operating assets',
                    'items': [
                        'increase_decrease_accounts_receivable',
                        'increase_decrease_inventories',
                        'increase_decrease_prepaid_expenses_and_other_assets',
                        'increase_decrease_accounts_payable',
                        'increase_decrease_accrued_and_other_current_liabilities',
                        'increase_decrease_other_non_current_liabilities',
                    ],
                },
                {
                    'name': 'Investing Activities',
                    'items': [
                        'proceeds_from_maturities_of_marketable_securities',
                        'proceeds_from_sales_of_marketable_securities',
                        'purchases_of_marketable_securities',
                        'payments_to_acquire_productive_assets',
                        'payments_to_acquire_property_plant_equipment',
                        'other_investing_activities',
                        'aquisitions_net_of_cash_aquired',
                        'cash_from_investing_activities',
                    ]
                },
                {
                    'name': 'Financing Activities',
                    'items': [
                        'repurchases_of_common_stock',
                        'repayments_of_debt',
                        'payment_of_dividends',
                        'issuance_of_debt',
                        'issuance_of_debt_net_of_costs',
                        'proceeds_from_repayments_of_commercial_paper',
                        'Proceeds_From_Payments_For_Other_Financing_Activities',
                        'cash_from_financing_activities',
                    ],
                },
                {
                    'name': 'Cash Position',
                    'items': [
                        'cash_and_restricted_cash'
                    ]
                }
            ]
        }
    }