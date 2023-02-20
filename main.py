from flask import Flask, request, jsonify, send_from_directory, redirect, url_for
import os, requests, speedtest
from bs4 import BeautifulSoup

st = speedtest.Speedtest()

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.errorhandler(500)
def page_not_found(e):
    return redirect(url_for('index'))

@app.errorhandler(405)
def page_not_found(e):
    return redirect(url_for('index'))

@app.errorhandler(403)
def page_not_found(e):
    return redirect(url_for('index'))

@app.errorhandler(400)
def page_not_found(e):
    return redirect(url_for('index'))

@app.errorhandler(401)
def page_not_found(e):
    return redirect(url_for('index'))

@app.errorhandler(408)
def timeout(e):
    return redirect(url_for('timeout'))

@app.errorhandler(504)
def gateway_timeout(e):
    return """
    <!DOCTYPE html>
    <html lang="en" oncontextmenu="return false">
    <head>
            <title>Wikipedia Scraper</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <body>
            <h1>Gateway Timeout Error</h1>
            <p>Mohon maaf, permintaan Anda tidak dapat diproses saat ini karena masalah dengan server gateway.</p>
            <p>We apologize, your request cannot be processed at this time due to an issue with the gateway server.</p>
            <a href="/">Go Back</a>
            </body>
            </html>
    """

@app.errorhandler(502)
def bad_gateway(e):
    return """
    <!DOCTYPE html>
    <html lang="en" oncontextmenu="return false">
    <head>
            <title>Wikipedia Scraper</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <body>
            <h1>Bad Gateway Error</h1>
            <p>Mohon maaf, permintaan Anda tidak dapat diproses saat ini karena masalah dengan server gateway.</p>
            <p>We apologize, your request cannot be processed at this time due to an issue with the gateway server.</p>
            <a href="/">Go Back</a>
            </body>
            </html>
    """

@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt', mimetype='text/plain')
    # return """
    # User-agent: *
    # <br />
    # Allow: /
    # """


@app.errorhandler(503)
def service_unavailable(e):
    return """
    <!DOCTYPE html>
    <html lang="en" oncontextmenu="return false">
    <head>
            <title>Wikipedia Scraper</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <body>
            <h1>Service Unavailable Error</h1>
            <p>Mohon maaf, permintaan Anda tidak dapat diproses saat ini karena masalah dengan server layanan yang tidak ada (Wikipedia).</p>
            <p>We apologize, your request cannot be processed at this time due to an issue with the service unavailable server.</p>
            <a href="/">Go Back</a>
            </body>
            </html>
    """

@app.route('/timeout')
def timeout():
    return """
<!DOCTYPE html>
<html lang="en" oncontextmenu="return false">
<head>
        <title>Wikipedia Scraper</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
        <h1>Timeout Error</h1>
        <p>Sorry, Your Connection is timeout. Please try again later.</p>
        <p>Mohon maaf, koneksi Anda telah berakhir. Silakan coba lagi nanti.</p>
        <a href="/">Go Back</a>
        </body>
        </html>
"""

@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html lang="en" oncontextmenu="return false">
        <title>Wikipedia Scraper</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
        <link rel="icon" href="https://i.pinimg.com/564x/06/2e/7f/062e7f7ae6d8ba893b44f66a08983024.jpg" type="image"/x-icon">
        <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
        <meta property="og:title" content="Wikipedia Scraper by Xnuvers007">
        <meta property="og:description" content="Wikipedia Scraper">
        <meta property="og:image" content="https://i.pinimg.com/564x/06/2e/7f/062e7f7ae6d8ba893b44f66a08983024.jpg">
        <meta property="og:url" content="https://wikiscrap.xnuvers007.repl.co/">
        <meta name="twitter:card" content="summary_large_image">
        <meta name="twitter:site" content="@xnuvers007">
        <meta name="twitter:creator" content="@xnuvers007">
        <meta name="twitter:title" content="Wikipedia Scraper by Xnuvers007">
        <meta name="twitter:description" content="Wikipedia Scraper">
        <meta name="twitter:image" content="https://i.pinimg.com/564x/06/2e/7f/062e7f7ae6d8ba893b44f66a08983024.jpg">
        <meta name="keywords" content="website, scraper, wikipedia, flask, python, xnuvers007">
        <meta name="description" content="Wikipedia Scraper by Xnuvers007">
        <meta name="color-scheme" content="light">
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }
            h1 {
                text-align: center;
                margin-bottom: 20px;
                color: green;
            }
            h2 {
                margin-top: 40px;
                margin-bottom: 20px;
                color: green;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
                background-color: #f2f2f2;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px #ccc;
                margin-bottom: 20px;
            }
            label {
                text-align: left;
                margin-bottom: 10px;
                width: 100%;
            }
            input[type="text"] {
                padding: 10px;
                font-size: 16px;
                width: 100%;
                border: none;
                border-radius: 5px;
                box-shadow: 2px 2px 10px #ccc;
                margin-bottom: 20px;
                background-image: url(https://via.placeholder.com/70x70.png?text=Search);
                background-repeat: no-repeat;
                background-position: 5px center;
                background-size: 32px 32px;
                padding-left: 40px;

                placeholder: "Country";
            }
            button[type="submit"] {
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            p {
                margin: 0;
                font-size: 16px;
                font-weight: bold;
                color: green;
            }
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f2f2f2;
                color: green;
                text-align: center;
            }
            
            .header{
                position: fixed;
                display: flex;
                justify-content: space-between;
                align-items: center;
                background-color: #dddddd;
                padding: 10px;
            }
            #logo{
                float: left;
            }

            #clock{
                color: yellow;
                margin: 0 auto;
                text-align: center;
                }
                
        </style>
    </head>
    <body style="background-color: black">
        <SCRIPT LANGUAGE="JavaScript">
            var message="Sorry,Right click disabled. Message from Xnuvers007";
            ///////////////////////////////////
            function clickIE() {if (document.all) {alert(message);return false;}}
            function clickNS(e) {if 
            (document.layers||(document.getElementById&&!document.all)) {
            if (e.which==2||e.which==3) {alert(message);return false;}}}
            if (document.layers) 
            {document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS;}
            else{document.onmouseup=clickNS;document.oncontextmenu=clickIE;}

            document.oncontextmenu=new Function("return false")
            // --> 
        </script>

        <!-- This code for disable left click -->

        <script type="text/JavaScript">
            function disableselect(e){
            return false
            }
            function reEnable(){
            return true
            }
            document.onselectstart=new Function ("return false")
            if (window.sidebar){
            document.onmousedown=disableselect
            document.onclick=reEnable
            }
        </script>
        <header>
            <img id="logo" src="https://i.pinimg.com/564x/06/2e/7f/062e7f7ae6d8ba893b44f66a08983024.jpg" alt="logo" width="65" height="65">
            <div id="clock"></div>
            <div style="float:right;">
                <h1 style="color: yellow; font-size: 28px;"><a href="https://github.com/Xnuvers007"> Xnuvers007 </a></h3>
 </h1>
            </div>
        </header>
        <script>
		function displayTime() {
			var date = new Date();
			var time = date.toLocaleTimeString();
			document.getElementById("clock").innerHTML = time;
		}
		setInterval(displayTime, 1000);
        </script>
        <br />
        <h1 style="color: yellow; float:center;">Wikipedia Scraper by Xnuvers007</h1>
        <center>
            <p> By The Way, if you want to good json format with pretty print, you can use <a href="https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa/">this extension (edge/chrome)</a> </p>
            <p> jika kalian ingin melihat isi Json menjadi rapih gunakan <a href="https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa/">ekstensi ini (edge/chrome)</a> </p>
            <br />
            <a href="https://github.com/Xnuvers007/wikiscrape" style="color: white;"><button style="background-color: #3498DB; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;">
  Source code
</button></a>
        </center>

        <h2>English</h2>
        <form action="/en/scrape" method="post">
            <input type="hidden" name="language" value="en">
            <label>
                <p>Article Title: </p>
                <input type="text" name="title" placeholder="World" autocomplete="off">
            </label>
            <button type="submit" class="btn btn-primary">Scrape</button>
        </form>

        <h2>Indonesian</h2>
        <form action="/id/scrape" method="post">
            <input type="hidden" name="language" value="id">
            <label>
                <p>Judul Artikel: </p>
                <input type="text" name="title" placeholder="BPUPKI" autocomplete="off">
            </label>
            <button type="submit" class="btn btn-primary">Scrape</button>
        </form>
        <br />
        <center><button class="btn btn-primary"><a href="https://wikiscrape.xnuvers007.repl.co/speedtest?domain=" style="color: yellow;">check internet & website</a></button></center>
        <hr />
        <div class="footer">
            <p>Copyright &copy; 2023 Xnuvers007. All right reserved</p>
            </div>
    </body>
</html>
    """

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/id/scrape', methods=['POST'])
def scrape_id():
    title = request.form.get('title')
    url = f"https://id.wikipedia.org/wiki/{title}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', id='mw-content-text')
    title = soup.find('h1', id='firstHeading').text
    ps = [p.text.strip() for p in content.find_all('p')]
    # ps = re.sub(r'\[.*\]', '', ps[0])
    # for ps in ps:
    #     ps = re.sub(r'\[.*\]', '', ps)
    h2s = [h2.text.replace('[sunting | sunting sumber]', '') for h2 in content.find_all('h2')]
    links = []
    for tag in soup.find_all(['p', 'h2']):
        for link in tag.find_all('a'):
            links.append(link.get('href'))
            # add it domain
            links[-1] = f"https://id.wikipedia.org{links[-1]}"

    footer = soup.find('ul', {'id': 'footer-info'})
    #footer_content = footer.text if footer else None
    footer_content = ''.join([e.text.strip() for e in footer]) if footer else None
    result = {'judul': title, 'paragraf': ps, 'h2': h2s, 'tautan': links, 'hak_cipta': footer_content}
    return jsonify({'Konten': result})

@app.route('/en/scrape', methods=['POST'])
def scrape_en():
    title = request.form.get('title')
    url = f"https://en.wikipedia.org/wiki/{title}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', id='mw-content-text')
    title = soup.find('h1', id='firstHeading').text
    ps = [p.text.strip() for p in content.find_all('p')]
    # ps = re.sub(r'\[.*\]', '', ps[0])
    # for ps in ps:
    #     ps = re.sub(r'\[.*\]', '', ps)
    h2s = [h2.text.replace('[sunting | sunting sumber]', '') for h2 in content.find_all('h2')]
    links = []
    for tag in soup.find_all(['p', 'h2']):
        for link in tag.find_all('a'):
            links.append(link.get('href'))
            # add it domain
            links[-1] = f"https://id.wikipedia.org{links[-1]}"

    footer = soup.find('ul', {'id': 'footer-info'})
    #footer_content = footer.text if footer else None
    footer_content = ''.join([e.text.strip() for e in footer]) if footer else None
    result = {'title': title, 'paragraph': ps, 'h2': h2s, 'links': links, 'footer': footer_content}
    return jsonify({'Konten': result})

@app.route('/speedtest')
def speedtest():
    domain = request.args.get('domain')
    # if user input domain but not have http or https
    if domain and not domain.startswith('http'):
        domain = 'http://' + domain
    elif domain and domain.startswith('https'):
        domain = 'https://' + domain
    else:
        return jsonify({'error': 'domain is required', 'message': 'this is check speed internet yours and page loading website https://wikiscrape.xnuvers007.repl.co/speedtest?domain=YOUR-WEBSITE'})
    try:
        response = requests.get(domain)
    except:
        return jsonify({'error': 'domain is not valid'})
    if domain:
        st.get_best_server()
        st.download()
        st.upload()
        st.results.share()
        results_dict = st.results.dict()
        # data = {
        #     'speedtest_your_internet': results_dict,
        #     'message': 'success\n',
        #     'Loading_time_website': response.elapsed.total_seconds()
        # }
        # return jsonify(data)
        data = {
            'message': 'success\n',
            'status': 200
        }
        return jsonify({'speedtest_your_internet': results_dict, 'data': data, 'Loading_time_website': response.elapsed.total_seconds()})
    else:
        return jsonify({'error': 'domain is required'})


if __name__ == '__main__':
    app.run(debug=True,
           host='0.0.0.0',
           port=80)

# app.run(host='0.0.0.0', port=81)
