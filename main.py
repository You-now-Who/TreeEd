import streamlit as st
from ret_prompt import get_topics, get_ai_help
from searcher import search_google, search_youtube

youtube = False
ai_help = False

def search(query):
    # Perform search logic here
    # You can use any search API or library of your choice

    if ai_help:
        ai_text = get_ai_help(query)
        # st.write(f"** {query} **")
        st.write(f"* " + str(ai_text))
        st.write('---')


    results = []

    topics = get_topics(query)
    for topic in topics:
        result = search_google("how to learn " + topic, 3)
        if youtube:
            result += search_youtube("how to learn " + topic, 3)
        st.write(f"** {topic} **")
        for link in result:
            st.write(f"* " + str(link))
        st.write('---')
        # st.write(result)
        results.append({ "title": topic, "url": result[0], "thumbnail": "https://i.imgur.com/7b0vFV4.png" })
    
    # Example search results
    return results

def main():

    global ai_help
    
    st.image('https://i.imgur.com/iFxbZSC.png', output_format='JPEG', width=300)
    

    st.write('''
             #### TreeEd is an AI-powered search engine that creates personalized course structures with free educational resources on the web.
             ---
             '''
             )
    # Create a central search bar with styling
    query = st.text_input('What topic would you like to learn about?', key='search_input')
    search_button = st.button('Search', key='search_button')
    youtube = st.toggle('Search for YouTube videos too')
    ai_help = st.toggle('Get AI help')
    
    if search_button:
        results = search(query)
        
        # # Use a grid layout for search results
        # col1, col2, col3 = st.columns(3)
        
        # for i, result in enumerate(results):
        #     with col1:
        #         st.write(f"**{result['title']}**")
        #         # st.image(result['thumbnail'], use_column_width=True)
        #         st.write(result['url'])
        #         st.write('---')
                
        #     if (i+1) % 3 == 0:
        #         col1, col2, col3 = st.columns(3)
        #     else:
                # col1, col2, col3 = col2, col3, col1

if __name__ == '__main__':
    main()