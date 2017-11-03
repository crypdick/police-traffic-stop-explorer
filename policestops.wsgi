#!/Users/duffrind/miniconda3/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/PoliceStops/app")

from app import app
app.secret_key = 'Add your secret key'
app.run(debug=True)
