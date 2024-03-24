import streamlit as st
# streamlit run placement.py

def main():
    st.title("My placement Website")
    st.markdown("---")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Placement Task over 40", "Contact"])

    if page == "Home":
        st.header("Welcome to My placement Website!")
        st.write("This is the home page of my Placement  website.")
    
    elif page == "About":
        st.header("About Me")
        st.write("I am a passionate developer with experience in various technologies.")
    
    elif page == "Projects":
        st.header("Projects")
        st.write("Here are some of the projects I have worked on:")
        # You can list your projects here with descriptions and links
    
    elif page == "Placement Task over 40":
        st.header("Placement Task over 40")
        st.write("This page contains information about the task placement .")
        multi = '''
                What to study for Placements / Internships?

                    DSA
                    Projects
                    Theory Subjects
                    Resume
                    Practice
                
                Data Structures & Algorithms (DSA)
                    
                    Step1: Study Topic
                    Step2: Practice Qs from DSA Trending Q (450)    

                    
                Love Babbar's : https://drive.google.com/file/d/1FMdN_OCfOI0iAeDlqswCiC2DZzD4nPsb/view        

                
                Problems Time limit      

                    Easy: 5-10 mins
                    medium: 15-20 mins
                    Hard: 45-60 mins

                Data Structures & Algorithms (DSA)

                    Week 1

                      Arrays (Searching, Sorting); 2D Arrays; Strings

                    Week 2

                      Time & Space Complexity; Recursion; Divide & Conquer; Backtracking

                    Week 3

                      ArrayList/Vectors; LinkedList

                    Week 4

                      Stacks; Queues      
                      
                    Week 5 + 6

                      Trees (BT, BST, Tries)

                    Week 7

                      PriorityQueue; Hashing; Greedy

                    Week 8 + 9

                      Graphs

                    Week 10 + 11

                      Dynamic Programming (DP)

                    Week 12

                      Bit Manipulation/ Segment Trees

                Projects

                    Web Development

                    App Development

                    Machine Learning I AI

                    Blockchain Development

                    iot / Game Development

                    Weekends (2 & 3 month)    

                RESUME

                    1 Day     

                Theory Subjects

                    OOPS (2 days)

                    DataBase Management Systems (DBMS) (4 days)

                    Operating Systems (OS) (4 days)

                    Computer Networking (CN) (4 days)   

                PRACTICE

                    Contests 

                      leetcode 

                        weekly
                        biweekly
                      Codeforces  

                    Mock Interviews      

                FINAL THOUGHTS:

                    Don't seek praise,
                    seek criticism.










                    
                '''
        st.markdown(multi)
    
    elif page == "Contact":
        st.header("Contact Me")
        st.write("You can reach me via email at example@example.com")
        # You can include a contact form or social media links here

if __name__ == "__main__":
    main()
