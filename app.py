import streamlit as st
import math
from shape_diagrams import get_shape_diagram

# Configure page
st.set_page_config(
    page_title="Mensuration Calculator",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    st.title("📐 Mensuration Calculator")
    st.markdown("**Calculate measurements for different geometric shapes**")
    
    # Shape selection - exactly like your original code
    st.sidebar.header("Select Shape")
    shape = st.sidebar.selectbox(
        "Mensuration of which shape you want to take out?",
        ["", "Square", "Rectangle", "Circle", "Triangle"],
        format_func=lambda x: {
            "": "Choose a shape...",
            "Square": "1. Square", 
            "Rectangle": "2. Rectangle",
            "Circle": "3. Circle", 
            "Triangle": "4. Triangle"
        }.get(x, x),
        key="main_shape_selector"
    )
    
    if shape == "Square":
        calculate_square()
    elif shape == "Rectangle":
        calculate_rectangle()
    elif shape == "Circle":
        calculate_circle()
    elif shape == "Triangle":
        calculate_triangle()
    else:
        st.info("Please select a shape from the sidebar to start calculating!")

def calculate_square():
    st.header("Square Calculator")
    
    # Display shape diagram
    diagram = get_shape_diagram("square")
    if diagram:
        st.html(diagram)
    
    calculation_type = st.selectbox(
        "What do you want to take out?",
        ["", "Perimeter", "Area", "Length of diagonal", "Side"],
        format_func=lambda x: {
            "": "Choose calculation type...",
            "Perimeter": "1. Perimeter",
            "Area": "2. Area", 
            "Length of diagonal": "3. Length of diagonal",
            "Side": "4. Side"
        }.get(x, x),
        key="square_calculation_type"
    )
    
    if calculation_type == "Perimeter":
        st.subheader("Calculate Perimeter")
        s = st.number_input("Enter side without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Perimeter"):
            if s > 0:
                p = s * 4
                st.success(f"Perimeter is {p} {unit}")
            else:
                st.error("Please enter a positive value for side")
    
    elif calculation_type == "Area":
        st.subheader("Calculate Area")
        s = st.number_input("Enter side without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Area"):
            if s > 0:
                a = s ** 2
                st.success(f"Area is {a} sq. {unit}")
            else:
                st.error("Please enter a positive value for side")
    
    elif calculation_type == "Length of diagonal":
        st.subheader("Calculate Length of Diagonal")
        s = st.number_input("Enter side without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Diagonal"):
            if s > 0:
                d1 = ((s ** 2) * 2) ** 0.5
                st.success(f"Length of diagonal is {d1:.3f} {unit}")
            else:
                st.error("Please enter a positive value for side")
    
    elif calculation_type == "Side":
        st.subheader("Calculate Side")
        known_value = st.selectbox(
            "What do you know about the square?",
            ["", "Area", "Perimeter"],
            format_func=lambda x: {
                "": "Choose what you know...",
                "Area": "1. Area",
                "Perimeter": "2. Perimeter"
            }.get(x, x),
            key="square_side_known_value"
        )
        
        if known_value == "Area":
            a = st.number_input("Enter area without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit (without sq.):", value="cm", help="If the unit is sq.m, then enter m")
            
            if st.button("Calculate Side from Area"):
                if a > 0:
                    s = a ** 0.5
                    st.success(f"Side is {s:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for area")
        
        elif known_value == "Perimeter":
            p = st.number_input("Enter perimeter without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Side from Perimeter"):
                if p > 0:
                    s = p / 4
                    st.success(f"Side is {s:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for perimeter")

def calculate_rectangle():
    st.header("Rectangle Calculator")
    
    # Display shape diagram
    diagram = get_shape_diagram("rectangle")
    if diagram:
        st.html(diagram)
    
    calculation_type = st.selectbox(
        "What do you want to take out?",
        ["", "Perimeter", "Area", "Length of diagonal", "Length", "Breadth"],
        format_func=lambda x: {
            "": "Choose calculation type...",
            "Perimeter": "1. Perimeter",
            "Area": "2. Area",
            "Length of diagonal": "3. Length of diagonal",
            "Length": "4. Length",
            "Breadth": "5. Breadth"
        }.get(x, x),
        key="rectangle_calculation_type"
    )
    
    if calculation_type == "Perimeter":
        st.subheader("Calculate Perimeter")
        l = st.number_input("Enter length without unit:", min_value=0.0, step=0.1)
        b = st.number_input("Enter breadth without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Perimeter"):
            if l > 0 and b > 0:
                p = 2 * (l + b)
                st.success(f"Perimeter is {p} {unit}")
            else:
                st.error("Please enter positive values for length and breadth")
    
    elif calculation_type == "Area":
        st.subheader("Calculate Area")
        l = st.number_input("Enter length without unit:", min_value=0.0, step=0.1)
        b = st.number_input("Enter breadth without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Area"):
            if l > 0 and b > 0:
                a = l * b
                st.success(f"Area is {a} sq. {unit}")
            else:
                st.error("Please enter positive values for length and breadth")
    
    elif calculation_type == "Length of diagonal":
        st.subheader("Calculate Length of Diagonal")
        l = st.number_input("Enter length without unit:", min_value=0.0, step=0.1)
        b = st.number_input("Enter breadth without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Diagonal"):
            if l > 0 and b > 0:
                d = (l ** 2 + b ** 2) ** 0.5
                st.success(f"Length of diagonal is {d:.3f} {unit}")
            else:
                st.error("Please enter positive values for length and breadth")
    
    elif calculation_type == "Length":
        st.subheader("Calculate Length")
        known_value = st.selectbox(
            "What do you know about the rectangle?",
            ["", "Area", "Perimeter"],
            format_func=lambda x: {
                "": "Choose what you know...",
                "Area": "1. Area",
                "Perimeter": "2. Perimeter"
            }.get(x, x),
            key="rectangle_length_known_value"
        )
        
        if known_value == "Area":
            a = st.number_input("Enter area without unit:", min_value=0.0, step=0.1)
            b = st.number_input("Enter breadth without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit (without sq.):", value="cm")
            
            if st.button("Calculate Length from Area"):
                if a > 0 and b > 0:
                    l = a / b
                    st.success(f"Length is {l:.3f} {unit}")
                else:
                    st.error("Please enter positive values for area and breadth")
        
        elif known_value == "Perimeter":
            p = st.number_input("Enter perimeter without unit:", min_value=0.0, step=0.1)
            b = st.number_input("Enter breadth without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Length from Perimeter"):
                if p > 0 and b > 0:
                    l = (p / 2) - b
                    if l > 0:
                        st.success(f"Length is {l:.3f} {unit}")
                    else:
                        st.error("Invalid input: breadth is too large for the given perimeter")
                else:
                    st.error("Please enter positive values for perimeter and breadth")
    
    elif calculation_type == "Breadth":
        st.subheader("Calculate Breadth")
        known_value = st.selectbox(
            "What do you know about the rectangle?",
            ["", "Area", "Perimeter"],
            format_func=lambda x: {
                "": "Choose what you know...",
                "Area": "1. Area",
                "Perimeter": "2. Perimeter"
            }.get(x, x),
            key="rectangle_breadth_known_value"
        )
        
        if known_value == "Area":
            a = st.number_input("Enter area without unit:", min_value=0.0, step=0.1)
            l = st.number_input("Enter length without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit (without sq.):", value="cm")
            
            if st.button("Calculate Breadth from Area"):
                if a > 0 and l > 0:
                    b = a / l
                    st.success(f"Breadth is {b:.3f} {unit}")
                else:
                    st.error("Please enter positive values for area and length")
        
        elif known_value == "Perimeter":
            p = st.number_input("Enter perimeter without unit:", min_value=0.0, step=0.1)
            l = st.number_input("Enter length without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Breadth from Perimeter"):
                if p > 0 and l > 0:
                    b = (p / 2) - l
                    if b > 0:
                        st.success(f"Breadth is {b:.3f} {unit}")
                    else:
                        st.error("Invalid input: length is too large for the given perimeter")
                else:
                    st.error("Please enter positive values for perimeter and length")

def calculate_circle():
    st.header("Circle Calculator")
    
    # Display shape diagram
    diagram = get_shape_diagram("circle")
    if diagram:
        st.html(diagram)
    
    pi = 22/7  # Using the same value as your original code
    
    calculation_type = st.selectbox(
        "What do you want to take out?",
        ["", "Circumference", "Area", "Diameter", "Radius"],
        format_func=lambda x: {
            "": "Choose calculation type...",
            "Circumference": "1. Circumference",
            "Area": "2. Area",
            "Diameter": "3. Diameter",
            "Radius": "4. Radius"
        }.get(x, x),
        key="circle_calculation_type"
    )
    
    if calculation_type == "Circumference":
        st.subheader("Calculate Circumference")
        known_value = st.selectbox(
            "Which of the following you know about the circle?",
            ["", "Radius", "Diameter"],
            format_func=lambda x: {
                "": "Choose what you know...",
                "Radius": "1. Radius",
                "Diameter": "2. Diameter"
            }.get(x, x)
        )
        
        if known_value == "Radius":
            r = st.number_input("Enter radius without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Circumference from Radius"):
                if r > 0:
                    c = 2 * pi * r
                    st.success(f"Circumference is {c:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for radius")
        
        elif known_value == "Diameter":
            d = st.number_input("Enter diameter without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Circumference from Diameter"):
                if d > 0:
                    c = pi * d
                    st.success(f"Circumference is {c:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for diameter")
    
    elif calculation_type == "Area":
        st.subheader("Calculate Area")
        known_value = st.selectbox(
            "Which of the following you know about the circle?",
            ["", "Radius", "Diameter"],
            format_func=lambda x: {
                "": "Choose what you know...",
                "Radius": "1. Radius",
                "Diameter": "2. Diameter"
            }.get(x, x)
        )
        
        if known_value == "Radius":
            r = st.number_input("Enter radius without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Area from Radius"):
                if r > 0:
                    a = pi * (r ** 2)
                    st.success(f"Area is {a:.3f} sq. {unit}")
                else:
                    st.error("Please enter a positive value for radius")
        
        elif known_value == "Diameter":
            d = st.number_input("Enter diameter without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Area from Diameter"):
                if d > 0:
                    a = (pi * ((d / 2) ** 2))
                    st.success(f"Area is {a:.3f} sq. {unit}")
                else:
                    st.error("Please enter a positive value for diameter")
    
    elif calculation_type == "Diameter":
        st.subheader("Calculate Diameter")
        known_value = st.selectbox(
            "Which of the following you know about the circle?",
            ["", "Radius", "Area", "Circumference"],
            format_func=lambda x: {
                "": "Choose what you know...",
                "Radius": "1. Radius",
                "Area": "2. Area",
                "Circumference": "3. Circumference"
            }.get(x, x)
        )
        
        if known_value == "Radius":
            r = st.number_input("Enter radius without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Diameter from Radius"):
                if r > 0:
                    d = r * 2
                    st.success(f"Diameter is {d:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for radius")
        
        elif known_value == "Area":
            a = st.number_input("Enter area without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit without sq.:", value="cm")
            
            if st.button("Calculate Diameter from Area"):
                if a > 0:
                    d = (((a ** 0.5) / pi) * 2)
                    st.success(f"Diameter is {d:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for area")
        
        elif known_value == "Circumference":
            c = st.number_input("Enter circumference without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Diameter from Circumference"):
                if c > 0:
                    d = c / pi
                    st.success(f"Diameter is {d:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for circumference")
    
    elif calculation_type == "Radius":
        st.subheader("Calculate Radius")
        known_value = st.selectbox(
            "Which of the following you know about the circle?",
            ["", "Diameter", "Area", "Circumference"],
            format_func=lambda x: {
                "": "Choose what you know...",
                "Diameter": "1. Diameter",
                "Area": "2. Area",
                "Circumference": "3. Circumference"
            }.get(x, x)
        )
        
        if known_value == "Diameter":
            d = st.number_input("Enter diameter without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Radius from Diameter"):
                if d > 0:
                    r = d / 2
                    st.success(f"Radius is {r:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for diameter")
        
        elif known_value == "Area":
            a = st.number_input("Enter area without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit without sq.:", value="cm")
            
            if st.button("Calculate Radius from Area"):
                if a > 0:
                    r = ((a ** 0.5) / pi)
                    st.success(f"Radius is {r:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for area")
        
        elif known_value == "Circumference":
            c = st.number_input("Enter circumference without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Radius from Circumference"):
                if c > 0:
                    r = ((c / pi) / 2)
                    st.success(f"Radius is {r:.3f} {unit}")
                else:
                    st.error("Please enter a positive value for circumference")

def calculate_triangle():
    st.header("Triangle Calculator")
    
    # Display shape diagram
    diagram = get_shape_diagram("triangle")
    if diagram:
        st.html(diagram)
    
    calculation_type = st.selectbox(
        "What do you want to take out?",
        ["", "Perimeter", "Area", "Height", "Base"],
        format_func=lambda x: {
            "": "Choose calculation type...",
            "Perimeter": "1. Perimeter",
            "Area": "2. Area",
            "Height": "3. Height",
            "Base": "4. Base"
        }.get(x, x),
        key="triangle_calculation_type"
    )
    
    if calculation_type == "Perimeter":
        st.subheader("Calculate Perimeter")
        triangle_type = st.selectbox(
            "Which type of triangle is it?",
            ["", "Equilateral", "Isosceles", "Scalene"],
            format_func=lambda x: {
                "": "Choose triangle type...",
                "Equilateral": "1. Equilateral",
                "Isosceles": "2. Isosceles",
                "Scalene": "3. Scalene"
            }.get(x, x)
        )
        
        if triangle_type == "Equilateral":
            s = st.number_input("Enter the length of the sides without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Perimeter (Equilateral)"):
                if s > 0:
                    p = s * 3
                    st.success(f"Perimeter is {p} {unit}")
                else:
                    st.error("Please enter a positive value for side length")
        
        elif triangle_type == "Isosceles":
            l = st.number_input("Enter leg i.e. the similar sides of isosceles triangle without unit:", min_value=0.0, step=0.1)
            b = st.number_input("Enter base i.e. the unequal side of isosceles triangle without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Perimeter (Isosceles)"):
                if l > 0 and b > 0:
                    p = (2 * l) + b
                    st.success(f"Perimeter is {p} {unit}")
                else:
                    st.error("Please enter positive values for legs and base")
        
        elif triangle_type == "Scalene":
            s1 = st.number_input("Enter first side without unit:", min_value=0.0, step=0.1)
            s2 = st.number_input("Enter second side without unit:", min_value=0.0, step=0.1)
            s3 = st.number_input("Enter third side without unit:", min_value=0.0, step=0.1)
            unit = st.text_input("Enter unit:", value="cm")
            
            if st.button("Calculate Perimeter (Scalene)"):
                if s1 > 0 and s2 > 0 and s3 > 0:
                    # Check triangle inequality
                    if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
                        p = s1 + s2 + s3
                        st.success(f"Perimeter is {p} {unit}")
                    else:
                        st.error("Invalid triangle! The sum of any two sides must be greater than the third side.")
                else:
                    st.error("Please enter positive values for all sides")
    
    elif calculation_type == "Area":
        st.subheader("Calculate Area")
        b = st.number_input("Enter base without unit:", min_value=0.0, step=0.1)
        h = st.number_input("Enter height without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Area"):
            if b > 0 and h > 0:
                a = b * h * 0.5
                st.success(f"Area is {a} sq. {unit}")
            else:
                st.error("Please enter positive values for base and height")
    
    elif calculation_type == "Height":
        st.subheader("Calculate Height")
        a = st.number_input("Enter area without sq. unit:", min_value=0.0, step=0.1)
        b = st.number_input("Enter base without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Height"):
            if a > 0 and b > 0:
                h = (a / b) * 2
                st.success(f"Height is {h:.3f} {unit}")
            else:
                st.error("Please enter positive values for area and base")
    
    elif calculation_type == "Base":
        st.subheader("Calculate Base")
        a = st.number_input("Enter area without sq. unit:", min_value=0.0, step=0.1)
        h = st.number_input("Enter height without unit:", min_value=0.0, step=0.1)
        unit = st.text_input("Enter unit:", value="cm")
        
        if st.button("Calculate Base"):
            if a > 0 and h > 0:
                b = (a / h) * 2
                st.success(f"Base is {b:.3f} {unit}")
            else:
                st.error("Please enter positive values for area and height")

if __name__ == "__main__":
    main()
