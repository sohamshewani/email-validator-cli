import click
import re

@click.command()
@click.argument('files', nargs=-1)
def validate_emails(files):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\[a-zA-Z]{2,}$'
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
        matches = re.findall(pattern, content)
        if matches:
            print(f'Valid emails in {file}:
{matches}')
        else:
            print(f'{file} does not contain any valid emails.')

if __name__ == '__main__':
    validate_emails()