import os, glob

folder = r'd:\AllDataVsCode\proyekview_webapp'
html_files = glob.glob(os.path.join(folder, '*.html'))

search_str = '<p class="nav-group-label">Administrasi</p>'
replace_str = '''<p class="nav-group-label">Manajemen Mitra</p>
                <a href="vendor.html" class="nav-link">
                    <span class="material-icons">business_center</span>
                    <span>Rapor Kontraktor</span>
                </a>

                <p class="nav-group-label">Administrasi</p>'''

for file_path in html_files:
    if os.path.basename(file_path) in ['index.html', 'vendor.html']: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if search_str in content and 'Manajemen Mitra' not in content:
        content = content.replace(search_str, replace_str)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated sidebar in {os.path.basename(file_path)}')
