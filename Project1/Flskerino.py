from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta http-equiv="X-UA-Compatible" content="IE=edge"/>
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,minimal-ui"/>
<link rel="apple-touch-icon" sizes="180x180" href="/favicons/apple-touch-icon.png"/>
<link rel="icon" type="image/png" sizes="32x32" href="/favicons/favicon-32x32.png"/>
<link rel="icon" type="image/png" sizes="16x16" href="/favicons/favicon-16x16.png"/>
<link rel="mask-icon" href="/favicons/safari-pinned-tab.svg" color="#e6195e"/>
<link rel="shortcut icon" href="/favicons/favicon.ico"/>
<meta name="msapplication-TileColor" content="#ffffff"/>
<meta name="theme-color" content="#e6195e"/>
<meta name="msapplication-config" content="/browserconfig.xml"/>
<link rel="manifest" href="/site.webmanifest"/>
<title>Genymotion SaaS</title>
<meta name="description" content="Seriously powerful Android Emulator!"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700,900"/>
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Material+Icons"/>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap" rel="stylesheet"/>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBDhC2hswKYFJyPDBR4-IWzyntyCAaiS48" async defer="defer"></script>
<meta property="og:title" content="Genymotion SaaS"/>
<meta property="og:description" content="Seriously powerful Android Emulator!"/>
<meta property="og:type" content="website"/>
<meta property="og:image" content="/og/image.png"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:site" content="@genymotion"/>
<meta property="twitter:domain" content="cloud.geny.io"/>
<meta property="twitter:url" content="https://cloud.geny.io"/>
<meta name="twitter:title" content="Genymotion SaaS"/>
<meta name="twitter:description" content="Seriously powerful Android Emulator!"/>
<meta name="twitter:image" content="/og/image.png"/>
<script defer="defer" src="/js/chunk-vendors.d8cf38bb.js"></script>
<script defer="defer" src="/js/main.826c88cb.js"></script>
<link href="/css/chunk-vendors.97855e73.css" rel="stylesheet">
<link href="/css/main.1fd58541.css" rel="stylesheet">
</head>
<body>
<noscript><strong>We're sorry but genymotion-cloud-fe-saas-webapp doesn't work properly without JavaScript enabled. Please enable it to continue.</strong></noscript>
<div id="app"></div>
<script src="https://static.zdassets.com/ekr/snippet.js?key=1fe0c88c-b721-4e38-a8d2-5acf1d6df272" id="ze-snippet" async defer="defer"></script>
<script src="https://js.stripe.com/v3/" async defer="defer"></script>
</body>
</html>
"""
if __name__ == "__main__":
    app.run(debug=True)



if __name__ == "__main__":
    app.run(debug=True)
