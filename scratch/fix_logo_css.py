with open('assets/css/index.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace object-fit: cover with object-fit: contain for nav-logo
css = css.replace('.nav-logo img {\n    width: 80px;\n    height: 80px;\n    background-color: #ffffff;\n    border: 3px solid #2d6a2d;\n    border-radius: 50%;\n    display: block;\n    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);\n    transition: all 0.3s ease;\n    padding: 2px;\n    object-fit: cover;',
                  '.nav-logo img {\n    width: 80px;\n    height: 80px;\n    background-color: #ffffff;\n    border: 3px solid #2d6a2d;\n    border-radius: 50%;\n    display: block;\n    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);\n    transition: all 0.3s ease;\n    padding: 4px;\n    object-fit: contain;')

css = css.replace('.nav-logo img {\n        width: 60px;\n        height: 60px;\n        border: 2px solid #2d6a2d;\n        padding: 2px;\n        object-fit: cover;\n    }',
                  '.nav-logo img {\n        width: 60px;\n        height: 60px;\n        border: 2px solid #2d6a2d;\n        padding: 4px;\n        object-fit: contain;\n    }')

with open('assets/css/index.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated nav-logo object-fit: contain')

