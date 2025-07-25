def get_shape_diagram(shape):
    """
    Generate SVG diagrams for different geometric shapes
    Returns HTML string containing SVG diagram
    """
    
    diagrams = {
        "rectangle": '''
        <div style="text-align: center;">
            <svg width="200" height="120" viewBox="0 0 200 120">
                <rect x="30" y="20" width="140" height="80" 
                      fill="none" stroke="#2E86AB" stroke-width="2"/>
                <text x="100" y="35" text-anchor="middle" font-size="12" fill="#2E86AB">length</text>
                <text x="15" y="65" text-anchor="middle" font-size="12" fill="#2E86AB">width</text>
                <!-- Dimension lines -->
                <line x1="30" y1="10" x2="170" y2="10" stroke="#666" stroke-width="1"/>
                <line x1="30" y1="8" x2="30" y2="12" stroke="#666" stroke-width="1"/>
                <line x1="170" y1="8" x2="170" y2="12" stroke="#666" stroke-width="1"/>
                <line x1="20" y1="20" x2="20" y2="100" stroke="#666" stroke-width="1"/>
                <line x1="18" y1="20" x2="22" y2="20" stroke="#666" stroke-width="1"/>
                <line x1="18" y1="100" x2="22" y2="100" stroke="#666" stroke-width="1"/>
            </svg>
        </div>
        ''',
        
        "square": '''
        <div style="text-align: center;">
            <svg width="200" height="120" viewBox="0 0 200 120">
                <rect x="50" y="20" width="100" height="100" 
                      fill="none" stroke="#F18F01" stroke-width="2"/>
                <text x="100" y="35" text-anchor="middle" font-size="12" fill="#F18F01">side</text>
                <text x="35" y="75" text-anchor="middle" font-size="12" fill="#F18F01">side</text>
                <!-- Dimension lines -->
                <line x1="50" y1="10" x2="150" y2="10" stroke="#666" stroke-width="1"/>
                <line x1="50" y1="8" x2="50" y2="12" stroke="#666" stroke-width="1"/>
                <line x1="150" y1="8" x2="150" y2="12" stroke="#666" stroke-width="1"/>
                <line x1="40" y1="20" x2="40" y2="120" stroke="#666" stroke-width="1"/>
                <line x1="38" y1="20" x2="42" y2="20" stroke="#666" stroke-width="1"/>
                <line x1="38" y1="120" x2="42" y2="120" stroke="#666" stroke-width="1"/>
            </svg>
        </div>
        ''',
        
        "circle": '''
        <div style="text-align: center;">
            <svg width="200" height="120" viewBox="0 0 200 120">
                <circle cx="100" cy="60" r="50" 
                        fill="none" stroke="#C73E1D" stroke-width="2"/>
                <line x1="100" y1="60" x2="150" y2="60" stroke="#C73E1D" stroke-width="2"/>
                <circle cx="100" cy="60" r="2" fill="#C73E1D"/>
                <text x="125" y="55" text-anchor="middle" font-size="12" fill="#C73E1D">radius</text>
                <text x="100" y="75" text-anchor="middle" font-size="10" fill="#666">center</text>
            </svg>
        </div>
        ''',
        
        "triangle": '''
        <div style="text-align: center;">
            <svg width="200" height="120" viewBox="0 0 200 120">
                <polygon points="100,20 40,100 160,100" 
                         fill="none" stroke="#A4243B" stroke-width="2"/>
                <line x1="100" y1="20" x2="100" y2="100" stroke="#666" stroke-width="1" stroke-dasharray="2,2"/>
                <text x="100" y="15" text-anchor="middle" font-size="12" fill="#A4243B">vertex</text>
                <text x="100" y="110" text-anchor="middle" font-size="12" fill="#A4243B">base</text>
                <text x="85" y="65" text-anchor="middle" font-size="12" fill="#A4243B">height</text>
            </svg>
        </div>
        '''
    }
    
    return diagrams.get(shape, "")
