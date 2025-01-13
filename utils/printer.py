class ProFormaPrinter:
    def __init__(self, xbrl_tags, financial_structure, debug=False):
        self.debug = debug
        self.xbrl_tags = xbrl_tags
        self.financial_structure = financial_structure

    def debug_print(self, message):
        if self.debug:
            print(f"[DEBUG] {message}")

    def print_financial_statements(self, financial_statements):
        """
        Print financial statements organized by end date and following the financial structure.
        """
        if not financial_statements:
            self.debug_print("No financial statements to print")
            return

        # Sort dates in reverse chronological order
        sorted_dates = sorted(financial_statements.keys(), reverse=True)

        for end_date in sorted_dates:
            print(f"\nFinancials for end date: {end_date}")
            print("=" * 80)

            # Go through each statement type in the structure
            for statement_type, structure in self.financial_structure.items():
                print(f"\n{statement_type.upper().replace('_', ' ')}")
                print("-" * 80)

                # Print each group and its items
                for group in structure['groups']:
                    print(f"\n{group['name']}:")
                    
                    for item in group['items']:
                        item_data = financial_statements[end_date].get(item)
                        if item_data and item_data['value'] is not None:
                            value = item_data['value']
                            # Format number if it's numeric
                            try:
                                formatted_value = f"${float(value):,.2f}"
                            except (ValueError, TypeError):
                                formatted_value = value
                            
                            date_info = f"({item_data.get('start', 'No start')} to {item_data.get('end', 'No end')})"
                            print(f"{item.replace('_', ' ').title():<45} {formatted_value} {date_info}")
                        else:
                            print(f"{item.replace('_', ' ').title():<45} No data")

            print("\n" + "=" * 80)