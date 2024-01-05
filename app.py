import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(words, frequencies, colors):
  
    repeated_words = [word for word, freq in zip(words, frequencies) for _ in range(freq)]


    text = ' '.join(repeated_words)

 
    wordcloud = WordCloud(width=800, height=400, background_color='white',
                          colormap=colors).generate(text)

    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')


    st.pyplot(fig)

def main():
    st.markdown("<h1 style='color: red;'>Word Cloud Visualization !!!</h1>", unsafe_allow_html=True)

    words_input = st.text_area("Enter words (separated by space):")
    frequencies_input = st.text_area("Enter corresponding frequencies (separated by space):")
    colors_input = st.selectbox("Choose a color map:", ['viridis', 'plasma', 'inferno', 'magma', 'cividis'])

    if st.button("Generate Word Cloud"):
        words = words_input.split()
        frequencies = [int(freq) for freq in frequencies_input.split()]
        generate_word_cloud(words, frequencies, colors_input)

if __name__ == "__main__":
    main()
