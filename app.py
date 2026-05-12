@app.route('/debug/templates')
def debug_templates():
    template_dir = app.template_folder
    import os
    if not os.path.isdir(template_dir):
        return {'error': f'Template directory does not exist: {template_dir}', 'cwd': os.getcwd(), 'file': __file__}
    files = []
    for root, dirs, filenames in os.walk(template_dir):
        for f in filenames:
            rel_path = os.path.relpath(os.path.join(root, f), template_dir)
            files.append(rel_path)
    return {'template_dir': template_dir, 'files': sorted(files)}