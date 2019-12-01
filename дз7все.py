import click
import requests
from urllib.request import urlretrieve

@click.group()
def cli():
    pass

@cli.command()
@click.argument('token', nargs=1)
def info(token):
    try:
        r = requests.get('https://cloud-api.yandex.net:443/v1/disk/',
                     headers={'Authorization': "OAuth "+token})
        code = r.status_code
        r = r.json()
        if code == 200:
            click.echo("успешно")
            click.echo(r['total_space'])
            click.echo(r['used_space'])
        else:
            click.echo("ошибка"+str(code))
    except Exception as ex:
        click.echo(ex)

@cli.command()
@click.argument('token', nargs=1)
@click.argument('path', nargs=1)
@click.option('--is_file_q', is_flag=True)
def info_file(token, path, is_file_q):
    try:
        r = requests.get('https://cloud-api.yandex.net/v1/disk/resources?path=' + path,
                         headers={'Authorization': "OAuth " + token})
        code = r.status_code
        r = r.json()
        if code == 200:
            click.echo("успешно")
            if is_file_q:
                click.echo(r["name"])
                click.echo(r['size'])
                click.echo(r["mime_type"])
                click.echo(r['created'])
            else:
                for d in r['_embedded']['items']:
                    click.echo(d['name'])
        else:
            click.echo("ошибка"+str(code))
    except Exception as ex:
        click.echo(ex)

@cli.command()
@click.argument('token', nargs=1)
@click.argument('path', nargs=1)
@click.argument('filename', nargs=1)
def download(token, path, filename):
    try:
        r = requests.get('https://cloud-api.yandex.net/v1/disk/resources/download?path=' + path, stream=True,
                     headers={'Authorization': "OAuth " + token})
        code = r.status_code
        r = r.json()
        if code == 200:
            click.echo("успешно")
            urlretrieve(r['href'], filename)
        else:
            click.echo("ошибка"+str(code))

    except Exception as ex:
        click.echo(ex)

@cli.command()
@click.argument('token', nargs=1)
@click.argument('path', nargs=1)
def new_dir(token, path):
    try:
        r = requests.put('https://cloud-api.yandex.net/v1/disk/resources?path=' + path,
                         headers={'Authorization': "OAuth "+token})
        code = r.status_code
        r = r.json()
        if code == 201:
            click.echo("успешно")
        else:
            click.echo("ошибка" + str(code))
    except Exception as ex:
        click.echo(ex)

@cli.command()
@click.argument('token', nargs=1)
@click.argument('path', nargs=1)
@click.argument('url', nargs=1)
def upload_1(token, path, url):
    try:
        req = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload?url=' + url + "&path="+path,
                         headers={'Authorization': "OAuth "+token})
        code = req.status_code
        click.echo(req)
        if code == 202:
            click.echo("загружено успешно")
        else:
            click.echo("ошибка" + str(code))
    except Exception as ex:
        click.echo(ex)

@cli.command()
@click.argument('token', nargs=1)
@click.argument('path1', nargs=1)
@click.argument('path2', nargs=1)
@click.option('--overwrite', is_flag=False)
def upload_2(token, path1, path2, overwrite):
    try:
        r = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload?path=' + path1 + "&overwrite="+str(overwrite),
                         headers={'Authorization': "OAuth "+token})
        if r.status_code == 200:
            with open(path2, 'rb') as fin:
                req = requests.put(r.json()["href"], data=fin)
                code = req.status_code
                if code == 201:
                    click.echo("загружено успешно")
                else:
                    click.echo("ошибка" + str(code))
    except Exception as ex:
        click.echo(ex)


if __name__ == '__main__':
    cli()