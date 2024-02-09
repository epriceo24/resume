import streamlit as st

# Function to display the about page
def about_page():
    st.title("Em Price")
    st.write("Welcome to my portfolio!")
    st.subheader("Skills:")
    st.write("- Python")
    st.image("images/python.png", width = 100)
    st.write("- JavaScript")
    st.image("images/js.png", width = 100)
    st.write("- HTML/CSS")
    st.image("images/htmlcss.png", width = 100)
    st.write("- PHP")
    st.image("images/php.png", width = 100)
    st.write("- Microsoft Office")
    st.image("images/micro.png", width = 100)
    st.subheader("Hobbies/Interests:")
    st.write("I enjoy playing instruments, reading, and running.")

# Function to display the projects page
def projects_page():
    st.title("Projects")
    st.write("Here are some of the major projects I have worked on:")
    st.subheader("Dj Turntable")
    st.write("http://areawebsites.org/ePrice/djturntable/index.html")
    st.subheader("Pampered Pups")
    st.write("http://areawebsites.org/ePrice/pamperedpupsweb/index.php")
    st.subheader("Dream Job Newsletter")
    st.write("http://areawebsites.org/ePrice/stuffforportfolio/filmcameraop.pdf")

# Function to display the resume page
def resume_page():
    st.title("Resume")
    st.write("Here is my current resume.")
    st.write("[Resume PDF](http://areawebsites.org/ePrice/stuffforportfolio/Real%20Resume.pdf)")

# Main function to create multi-page app
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["About", "Projects", "Resume"])

    if page == "About":
        about_page()
    elif page == "Projects":
        projects_page()
    elif page == "Resume":
        resume_page()

if __name__ == "__main__":
    main()
