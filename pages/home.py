import streamlit as st
import streamlit.components.v1 as components


def page_home(**kwargs):
    # ---- Header ----
    with st.container():
        st.title("A Movie Recommender Tutorial from some Data Science Students :wink:")
        st.subheader(":school: Greetings from Universiti Malaya :school:")
        st.write("Website is hosted through Azure Virtual Machine :hushed:")

    # ---- SVD Introduction ----
    with st.container():
        st.write("----")
        st.title("Introduction")
        st.write(
            "This is a working demo as part of the student project to put the understanding on the concept of Singular Value Decomposition (SVD) used in movie recommender system into action. Below are some of brief explanation on the concepts in preparing this recommender system. In this work, the dataset used is MovieLens 1M dataset."
        )

        st.write("##")
        st.subheader("Instruction of use:")
        st.write(
            """
- On the top left of webpage, click on  :arrow_forward:
- After clicking, navigation bar appears on screen.
- Kindly select “Movie Recommender”.
- On this page, you're required to pick a movie.
- A list of recommended movies instantly appears on your screen
- You may now enjoy watching one of the movies! :laughing:
"""
        )

        st.write("##")
        st.subheader("Recommender System")
        st.write(
            "A system that offers recommendation which is aimed to predict preferences and choices. Recommender system is not as complicated as it seems when the secret mask beneath it is revealed. The fundamentals of the algorithms for a recommendation system can be based on the significant dependencies that is portrayed by the user-centric activity. For example, someone who is interested in action film is more likely to be also interested in action video games.  Basically, it is a subclass of information filtering systems that seek to predict the rating a user will give to an item. It has a wide application in commercial systems as well as being used as playlist generators for video and music services, product recommenders for online stores, or content recommenders for social media platforms and open web content recommenders."
        )
        st.write("##")
        st.subheader("Singular Value Decomposition (SVD)")
        st.write(
            "SVD is a linear algebra method used as dimensionality reduction technique in machine learning. SVD is a factorization technique that decomposes a matrix M of form m*n into USVT where, "
        )
        st.write(
            """
- U = real or complex unitary matrix (m*m) 
- ∑ = rectangular diagonal matrix(m*n) with non-negative real numbers (square root of non-negative eigen values of M in descending order) on the diagonal. 
- VT= real or complex unitary matrix (n*n). 
- If M is a real matrix, U and VT are orthogonal matrices. SVD performs three transformations in sequence: 
  - A first rotation in input space 
  - A simple positive scaling that takes a matrix from input space to outer space 
  - Another rotation in outer space 
"""
        )
        st.write(
            "In the context of recommender system, SVD uses a matrix structure where each row represents a user while each column represents an item and elements of the matrix are the ratings given to items by the users."
        )

        st.write("##")
        st.subheader("Types of filtering")
        st.write(
            "In the context of movie recommender system with the use of MovieLens 1M Dataset, SVD is used as a collaborative filtering technique. There are few other types of filtering systems that could be implemented in a recommender system as shown as below:"
        )
        st.image("./src/img/filtering.png")
        st.write("##")

    # ---- Materials & Reference ----
    with st.container():
        st.write("----")
        left_column, right_column = st.columns(2)
        with left_column:
            st.title("Materials")
            st.write("[Source code >](https://github.com/davionchai/um-7009-bdaa/)")
            st.write("[Data Source >](https://grouplens.org/datasets/movielens/1m/)")
            st.write(
                "[Reference >](https://analyticsindiamag.com/singular-value-decomposition-svd-application-recommender-system/)"
            )
            st.markdown(
                "[Back to top ^](#a-movie-recommender-tutorial-from-some-data-science-students)",
                unsafe_allow_html=True,
            )
    components.html(
        f"<script>window.parent.document.querySelector('section.main').scrollTo(0, 0);</script>",
        height=0,
    )
