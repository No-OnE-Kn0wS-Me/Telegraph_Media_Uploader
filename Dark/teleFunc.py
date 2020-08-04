from telegraph import Telegraph


def teleGraph(short_name,page_title,page_contents):
    # simple function to make a telegraph page 
    
    telegraphy = Telegraph()
    telegraphy.create_account(short_name=short_name)

    response = telegraphy.create_page(
            page_title,
            html_content=page_contents
        )

    return response["url"]
    # return response


print(teleGraph('hh','qqq','sss'))