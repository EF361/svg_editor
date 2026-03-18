import streamlit.components.v1 as components

def svg_renderer(svg_code, height=700):
    # We wrap the SVG in a div to ensure it centers and scales correctly
    html_content = f"""
    <div style="display: flex; justify-content: center; align-items: center; height: {height}px; background: #fafafa; border: 1px solid #e5e7eb; border-radius: 8px; overflow: auto;">
        {svg_code}
    </div>
    """
    components.html(html_content, height=height + 50)