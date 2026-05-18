import os

def read_file(filepath):
    """Sequential file reading: scans line by line."""
    lines = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    return lines

def read_file_direct(filepath, position, length):
    """Direct access simulation: jumps directly to a position (seek)."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        f.seek(position)
        return f.read(length)

def scan_directory(directory_path, extension=".txt"):
    """Scans directory for files with specific extension."""
    matched_files = []
    if not os.path.exists(directory_path):
        return matched_files
        
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(extension):
                matched_files.append(os.path.join(root, file))
    return matched_files

def write_report(report_path, content):
    """Writes execution report to file."""
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)
