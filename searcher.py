from googlesearch import search
import search_google.api
import streamlit as st

def search_youtube(query, num_results):
    search_query = query + ' site:youtube.com'
    results = []
    
    for url in search(search_query, num_results=num_results):
        if 'youtube.com/watch' in url:
            results.append(url)
    
    return results

def search_google(query, num_results):
    results = []
    
    try:
        for url in search(query, num_results=num_results):
            results.append(url)
    except Exception as e:
        # results = search_google.api.results(query, num_results)
        st.write("Error, API limit exceeded. Please try again later.")
        return None
    
    return results

if __name__ == '__main__':
    # Example usage
    query = 'python tutorial and courses'
    num_results = 5
    youtube_results = search_google(query, num_results)
    print(youtube_results)