def pagination_text(page_number, page_size, total_products):
	start = 1 + (page_number - 1) * page_size
	end = page_size * (page_number) if (start + page_size) <= total_products else total_products
	return 'Showing ' + str(start) + ' to ' + str(end) + ' of ' + str(total_products) + ' Products.'